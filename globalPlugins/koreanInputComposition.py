import globalPluginHandler
import queueHandler
import speech
import characterProcessing
from NVDAObjects.inputComposition import InputComposition

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
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

	def event_gainFocus(self):
		pass
