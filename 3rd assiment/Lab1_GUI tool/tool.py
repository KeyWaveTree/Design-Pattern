#설계도부터 생각

#틀을 어떻게 구성해서 Api로 뭐가 되야 될까?

#각 공장당 특정 기능을 어떻게 추상 공장 패턴으로 이끌 수 있을까?
#구성 요소들
#모드 별로 확장을 해야함.

#먼저 버튼, 스크롤, 체크박스, 슬라이더, 덱스트는 모두 포함 되어 있음. -팩토리 인터페이스
#테마는 다크모드, 라이트, 레드, 블루 생성 - 팩토리

import Button as b
import CheckBox as cb
import Scroll as sr
import TextBox as tb

class GUIItemFactory:
    def createWhite(self):
        pass
    def createBlack(self):
        pass
    def createBlue(self):
        pass
    def createRed(self):
        pass


class ButtonFactory(GUIItemFactory):
    def createWhite(self):
        return b.WhiteButton()

    def createBlack(self):
        return b.BlackButton()

    def createBlue(self):
        return b.BlueButton()

    def createRed(self):
        return b.RedButton()


class ScrollBoxFactory(GUIItemFactory):
    def createWhite(self):
        return sr.ScrollLightMode()

    def createBlack(self):
        return sr.ScrollDarkMode()

    def createBlue(self):
        return sr.ScrollBlueMode()

    def createRed(self):
        return sr.ScrollRedMode()


class CheckBoxFactory(GUIItemFactory):
    def createWhite(self):
        return cb.ClickLightMode()
    def createBlack(self):
        return cb.ClickDarkMode()
    def createBlue(self):
        return cb.ClickBlueMode()
    def createRed(self):
        return cb.ClickRedMode()

class TextBoxFactory(GUIItemFactory):
    def createWhite(self):
        return tb.TextBoxLightMode()
    def createBlack(self):
        return tb.TextBoxDarkMode()
    def createBlue(self):
        return tb.TextBoxBlueMode()
    def createRed(self):
        return tb.TextBoxRedMode()
