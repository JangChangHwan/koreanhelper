# 한글 입력 / 탐색 도우미 추가기능(KoreanHelper Addon)

## 변경 이력

### v0.6: 2021-01-06
한글 입력 시 리뷰 커서를 이동할 때 부모 객체를 탐색하도록 수정함.
- koreanCommands.py 모듈을 새로 작성함.


### v0.5: 2021-01-05
- 입력 구성을 마칠 때, 방향키 등으로 캐럿 위치를 이동하는 경우 정상적으로 읽지 못하는 문제를 수정함.
- KoreanInputComposition와 KoreanTextInfo가 중첩되지 않도록 수정함.
- 부모객체가 편집창이 아닌 경우 포커스 이동 결과 읽기를 정상적으로 출력하도록 수정함.


### v0.4: 2021-01-05
- 입력 구성을 마칠 때, 텍스트 블록 설정을 할 경우 정상적으로 읽지 못하는 문제를 수정함.


###  v0.3: 2021-01-04
- KoreanInputComposition 클래스에서 event_typedCharacter 메소드를 재작성하여 메모장 등 Edit 객체에서 한글 입력 시 입력이 완료된 이전 글자를 읽어 주는 불필요한 동작을 제거함.
- NVDAHelper 모듈의 handleInputCompositionEnd 함수를 약간 수정하는 선에서 재작성하여 입력 구성을 마칠 때 불피요하게 한글 한 글자를 읽어주는 동작을 제거함.


###  v0.2: 2020-12-10
- KoreanInputCompositionTextInfo 작성: _getSelectionOffsets, _getCaretOffset를 재작성함
- KoreanTextInfo에서 KoreanStaticText 클래스를 IaAccessible와 UIA에 따라 두 가지로 분리함.


### v0.1: 2020-08-10
* KoreanEdit, KoreanEditTextInfo 클래스 작성
- _getWordOffsets를 수정하여 RichEdit와 같은 방식으로 단어 오프셋 값을 가져 오도록 함.
- script_caret_moveByWord를 수정하여 단어 단위 캐럿 이동 방식을 리뷰 단어 입력 방식과 동일하도록 수정함.
* KoreanStaticText, NVDAObjectTextInfo 클래스 작성
- 고정 텍스트에서 리뷰 커서로 탐색할 때 단어 단위 이동시 유니코드 문자를 한 글자만 읽는 오류를 수정함.
* KoreanInputComposition 클래스 작성(InputComposition 상속)
- event_gainFocus를 수정하여 "xx 선택" 메시지를 삭제함.

