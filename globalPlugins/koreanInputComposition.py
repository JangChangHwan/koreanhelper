import globalPluginHandler
import queueHandler
import speech
import characterProcessing
import NVDAHelper
import api
from NVDAObjects.inputComposition import *
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
		func = getattr(self.parent, '_caretMovementScriptHelper', None)
		if func:
			func(gesture, unit)
		else:
			gesture.send()


def handleInputCompositionEnd(result):
	import speech
	import characterProcessing
	from NVDAObjects.inputComposition import InputComposition
	from NVDAObjects.IAccessible.mscandui import ModernCandidateUICandidateItem
	focus=api.getFocusObject()
	result=result.lstrip(u'\u3000 ')
	curInputComposition=None
	if isinstance(focus,InputComposition):
		curInputComposition=focus
		oldSpeechMode=speech.speechMode
		speech.speechMode=speech.speechMode_off
		eventHandler.executeEvent("gainFocus",focus.parent)
		speech.speechMode=oldSpeechMode
	elif isinstance(focus.parent,InputComposition):
		#Candidate list is still up
		curInputComposition=focus.parent
		focus.parent=focus.parent.parent
	if isinstance(focus, ModernCandidateUICandidateItem):
		# Correct focus for ModernCandidateUICandidateItem
		# Find the InputComposition object and
		# correct focus to its parent
		if isinstance(focus.container, InputComposition):
			curInputComposition=focus.container
			newFocus=curInputComposition.parent
		else:
			# Sometimes InputCompositon object is gone
			# Correct to container of CandidateItem
			newFocus=focus.container
		oldSpeechMode=speech.speechMode
		speech.speechMode=speech.speechMode_off
		eventHandler.executeEvent("gainFocus",newFocus)
		speech.speechMode=oldSpeechMode

	if isinstance(focus, InputComposition):
		return
	if curInputComposition and not result:
		result=curInputComposition.compositionString.lstrip(u'\u3000 ')
	if result:
		speech.speakText(result,symbolLevel=characterProcessing.SYMLVL_ALL)
