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

	jamoDict = {
		"ㄱ": "초성 기역", "ㄲ": "초성 쌍기역", "ㄴ": "초성 니은", "ㄷ": "초성 디귿", "ㄸ": "초성 쌍디귿", "ㄹ": "초성 리을", "ㅁ": "초성 미음", "ㅂ": "초성 비읍", "ㅃ": "초성 쌍비읍", "ㅅ": "초성 시옷", "ㅆ": "초성 쌍시옷", "ㅇ": "초성 이응", "ㅈ":"초성 지읒", "ㅉ": "초성 쌍지읒", "ㅊ":"초성 치읓", "ㅋ":"초성 키읔", "ㅌ":"초성 티읕", "ㅍ":"초성 피읖", "ㅎ":"초성 히읗",
		}

	def event_gainFocus(self):
		pass
