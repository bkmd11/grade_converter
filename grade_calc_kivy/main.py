import grade_calculator

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class GradeCalc(BoxLayout):
    grade_input = ''

    def backspace_button(self, text_input):
        self.display.text = text_input[:-1]

    def calculate_button(self, text_input):
        grade_percentage = grade_calculator.grade_converter(float(text_input.strip()))
        self.result.text = str(grade_percentage)
        self.display.text = ''


class GradeCalcApp(App):
    def build(self):
        app = GradeCalc()

        return app


if __name__ == '__main__':
    GradeCalcApp().run()