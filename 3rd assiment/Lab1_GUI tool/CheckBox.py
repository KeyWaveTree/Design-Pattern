class CheckBox:
    def on_button(self):
        pass
    def off_button(self):
        pass

class ClickDarkMode(CheckBox):
    def on_button(self):
        print("OnClickModeDark")
    def off_button(self):
        print("OffClickModeDark")

class ClickLightMode(CheckBox):
    def on_button(self):
        print("OnClickModeLight")
    def off_button(self):
        print("OffClickModeLight")

class ClickRedMode(CheckBox):
    def on_button(self):
        print("OnClickModeRedMode")
    def off_button(self):
        print("OffClickModeRedMode")

class ClickBlueMode(CheckBox):
    def on_button(self):
        print("OnClickModeBlueMode")
    def off_button(self):
        print("OffClickModeBlueMode")
