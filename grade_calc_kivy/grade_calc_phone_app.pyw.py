from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class GradeCalc(GridLayout):
    pass


class GradeCalcApp(App):
    def build(self):
        app = GradeCalc()

        return app


if __name__ == '__main__':
    GradeCalcApp().run()