# coding: UTF-8

import globalPluginHandler
import ui
import textInfos
import controlTypes
from textInfos.offsets import *
from NVDAObjects import NVDAObjectTextInfo
from NVDAObjects.window.edit import Edit, EditTextInfo
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.UIA import UIA


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		# 단순 편집창
		if obj.role == controlTypes.ROLE_EDITABLETEXT and obj.windowClassName == "Edit":
			clsList.insert(0, KoreanEdit)
		# 고정 텍스트
		elif obj.role == controlTypes.ROLE_STATICTEXT:
			clsList.insert(0, KoreanStaticTextIAccessible if isinstance(obj, IAccessible) else KoreanStaticTextUIA)


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




class KoreanNVDAObjectTextInfo(NVDAObjectTextInfo):
	def _getWordOffsets(self, offset):
		paraStart, paraEnd = self._getParagraphOffsets(offset)
		paraText = self._getTextRange(paraStart, paraEnd)
		start = findStartOfWord(paraText, offset - paraStart) + paraStart
		end = findEndOfWord(paraText, offset - paraStart) + paraStart
		return start, end


class KoreanStaticTextIAccessible(IAccessible):
	TextInfo = KoreanNVDAObjectTextInfo


class KoreanStaticTextUIA(UIA):
	TextInfo = KoreanNVDAObjectTextInfo

