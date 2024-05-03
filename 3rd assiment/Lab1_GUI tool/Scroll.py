class Scroll:
    def event(self):
        pass

class ScrollDarkMode(Scroll):
    def event(self):
        print("ScrollModeDark")

class ScrollLightMode(Scroll):
    def event(self):
        print("ScrollModeLight")

class ScrollRedMode(Scroll):
    def event(self):
        print("ScrollModeRedMode")

class ScrollBlueMode(Scroll):
    def event(self):
        print("ScrollBlueMode")