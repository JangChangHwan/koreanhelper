import controlTypes
import config
import globalPluginHandler
import queueHandler
import speech
import characterProcessing
import NVDAHelper
import api
import textInfos
from NVDAObjects.inputComposition import *
from NVDAObjects.window.edit import *
from NVDAObjects.IAccessible.winword import *
from scriptHandler import script
from logHandler import log


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		NVDAHelper.handleInputCompositionEnd = handleInputCompositionEnd

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, InputComposition):
			clsList.insert(0, KoreanInputComposition)


class KoreanInputCompositionTextInfo(InputCompositionTextInfo):
	def _getSelectionOffsets(self):
		return 0, 1

	def _getCaretOffset(self):
		return 0


class KoreanInputComposition(InputComposition):

	TextInfo = KoreanInputCompositionTextInfo
	repeated = []
	def makeTextInfo(self, position):
		return self.TextInfo(self, position)

	def event_typedCharacter(self, ch):
		if ord(ch) < 128:
			super(KoreanInputComposition, self).event_typedCharacter(ch)


	def event_gainFocus(self):
		pass

	@script(gestures=('kb:shift+upArrow', 'kb:shift+downArrow', 'kb:shift+leftArrow', 'kb:shift+rightArrow', 'kb:control+shift+leftArrow', 'kb:control+shift+rightArrow', 'kb:shift+home', 'kb:shift+end', 'kb:control+shift+home', 'kb:control+shift+end', 'kb:control+a'))
	def script_moveCaret(self, gesture):
		self.focusToParent()
		gesture.send()


	def focusToParent(self):
		oldSpeechMode=speech.speechMode
		speech.speechMode=speech.speechMode_off
		eventHandler.executeEvent("gainFocus", self.parent)
		speech.speechMode=oldSpeechMode


	def _caretMovementScriptHelper(self, gesture, unit):
		self.focusToParent()
		scriptFunc = getattr(self.parent, '_caretMovementScriptHelper', None)
		if scriptFunc:
			scriptFunc(gesture, unit)
		else:
			gesture.send()


	def _backspaceScriptHelper(self,unit,gesture):
		gesture.send()

	def reportNewText(self,oldString,newString):
		if isinstance(self.parent, WordDocument):
			oldString = ''
		elif isinstance(self.parent, RichEdit50):
			oldString = ''
		elif isinstance(self.parent, Edit):
			self.repeated.append(oldString == newString)
			if len(self.repeated) == 2 :
				if self.repeated[0] and self.repeated[1]:
					oldString = ''
				self.repeated.clear()
		super(KoreanInputComposition, self).reportNewText(oldString,newString)


def handleInputCompositionEnd(result):
	from NVDAObjects.inputComposition import InputComposition
	import speech
	focus = api.getFocusObject()
	parent = None
	if isinstance(focus, InputComposition):
		parent = focus.parent
	elif isinstance(focus.parent, InputComposition):
		parent = focus.parent.parent
	else:
		return
	oldSpeechMode=speech.speechMode
	speech.speechMode=speech.speechMode_off
	eventHandler.executeEvent("gainFocus", parent)
	speech.speechMode = oldSpeechMode
