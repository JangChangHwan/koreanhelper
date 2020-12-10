import globalPluginHandler
import queueHandler
import speech
import characterProcessing
from NVDAObjects.inputComposition import InputComposition

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, InputComposition):
			clsList.insert(0, KoreanInputComposition)


class KoreanInputComposition(InputComposition):
	def event_gainFocus(self):
		pass
