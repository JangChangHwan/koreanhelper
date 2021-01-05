import globalPluginHandler
import globalCommands
import api
import speech
import eventHandler
from NVDAObjects.inputComposition import InputComposition


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		globalCommands.commands = KoreanCommands()


class KoreanCommands(globalCommands.GlobalCommands):

	def checkInputComposition(self):
		obj = api.getNavigatorObject()
		if isinstance(obj, InputComposition):
			api.setNavigatorObject(obj.parent, isFocus=False)

	def focusSilently(self, obj):
		oldSpeechMode=speech.speechMode
		speech.speechMode=speech.speechMode_off
		eventHandler.executeEvent("gainFocus", obj)
		speech.speechMode=oldSpeechMode


	def script_reportCurrentLine(self,gesture):
		focus = api.getFocusObject()
		if isinstance(focus, InputComposition):
			self.focusSilently(focus.parent)
			super(KoreanCommands, self).script_reportCurrentLine(gesture)
			self.focusSilently(focus)
		else:
			super(KoreanCommands, self).script_reportCurrentLine(gesture)


	def script_review_top(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_top(gesture)

	def script_review_previousLine(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_previousLine(gesture)

	def script_review_currentLine(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_currentLine(gesture)

	def script_review_nextLine(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_nextLine(gesture)

	def script_review_bottom(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_bottom(gesture)

	def script_review_previousWord(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_previousWord(gesture)

	def script_review_currentWord(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_currentWord(gesture)

	def script_review_nextWord(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_nextWord(gesture)

	def script_review_startOfLine(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_startOfLine(gesture)

	def script_review_previousCharacter(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_previousCharacter(gesture)


	def script_review_nextCharacter(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_nextCharacter(gesture)

	def script_review_endOfLine(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_endOfLine(gesture)

	def script_review_sayAll(self,gesture):
		self.checkInputComposition()
		super(KoreanCommands, self).script_review_sayAll(gesture)

	def script_sayAll(self,gesture):
		focus = api.getFocusObject()
		if isinstance(focus, InputComposition):
			self.focusSilently(focus.parent)
		super(KoreanCommands, self).script_sayAll(gesture)

