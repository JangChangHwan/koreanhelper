# 한글 입력 / 탐색 도우미 추가기능(KoreanHelper Addon)

## 변경 이력

### 2020-08-10
* KoreanEdit, KoreanEditTextInfo 클래스 작성
- _getWordOffsets를 수정하여 RichEdit와 같은 방식으로 단어 오프셋 값을 가져 오도록 함.
- script_caret_moveByWord를 수정하여 단어 단위 캐럿 이동 방식을 리뷰 단어 입력 방식과 동일하도록 수정함.
* KoreanStaticText, NVDAObjectTextInfo 클래스 작성
- 고정 텍스트에서 리뷰 커서로 탐색할 때 단어 단위 이동시 유니코드 문자를 한 글자만 읽는 오류를 수정함.
* KoreanInputComposition 클래스 작성(InputComposition 상속)
- event_gainFocus를 수정하여 "xx 선택" 메시지를 삭제함.

