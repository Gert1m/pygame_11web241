class KeyBoard:
    def __init__(self, *, img: dict, screen: vars, count: int = 0):
        self.screen = screen
        self.img_dict = img
        self.count = count

    def f(self):
        self.screen.fill((0, 0, 0))


class Mouse:
    def __init__(self, *, img: dict, screen: vars):
        self.screen = screen
        self.img_dict = img
