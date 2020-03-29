from kivy.app import App
from kivy.uix.widget import Widget


class GradeCalc(Widget):


class GradeCalcApp(App):
    def build(self):
        app = GradeCalc()

        return app

if __name__ == '__main__':
    GradeCalc().run()