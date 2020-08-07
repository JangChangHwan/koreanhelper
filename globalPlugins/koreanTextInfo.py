# coding: UTF-8

import globalPluginHandler
import ui
import textInfos
from textInfos.offsets import *
from NVDAObjects.window.edit import Edit, EditTextInfo


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName == "Edit":
			clsList.insert(0, KoreanEdit)

class KoreanEditTextInfo(EditTextInfo):
	def _getWordOffsets(self, offset):
		paraStart, paraEnd = self._getParagraphOffsets(offset)
		paraText = self._getTextRange(paraStart, paraEnd)
		start = findStartOfWord(paraText, offset - paraStart) + paraStart
		end = findEndOfWord(paraText, offset - paraStart) + paraStart
		return start, end


class KoreanEdit(Edit):
	TextInfo = KoreanEditTextInfo


	def script_caret_moveByWord(self, gesture):
		info = self.makeTextInfo(position=textInfos.POSITION_CARET)
		direction = 1 if gesture.mainKeyName == 'rightArrow' else -1
		info.move(unit=textInfos.UNIT_WORD, direction=direction)
		info._setCaretOffset(info._startOffset)
		info.expand(unit=textInfos.UNIT_WORD)
		ui.message(info.text)

