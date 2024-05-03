class TextBox:
    def write(self):
        pass

class TextBoxDarkMode(TextBox):
    def write(self):
        print("TextBoxModeDark")

class TextBoxLightMode(TextBox):
    def write(self):
        print("TextBoxModeLight")

class TextBoxRedMode(TextBox):
    def write(self):
        print("TextBoxModeRedMode")

class TextBoxBlueMode(TextBox):
    def write(self):
        print("TextBoxBlueMode")