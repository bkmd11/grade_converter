from kivy.app import App
from kivy.uix.button import Button


class GradeCalc(Button):

    def button(self):
        pass


class GradeCalcApp(App):
    def build(self):
        app = GradeCalc()

        return app


if __name__ == '__main__':
    GradeCalcApp().run()