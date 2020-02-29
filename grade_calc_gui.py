""" A GUI for the grade converting calculator that I made for my wife"""
# TODO: play around with sizing and colors
#  Make key events effect calc correctly, currently they break it

import PySimpleGUI as psg
import grade_calculator


def button(text):
    return psg.Button(text, size=(8, 4))


def input_screen():
    return psg.InputText(key='INPUT', size=(33, 0), justification='right')


def main():
    dok_grade = ''
    layout = [[psg.Text('', key='OUTPUT')],
              [input_screen()],
              [button(i + 1) for i in range(3)],
              [button(i + 4) for i in range(3)],
              [button(i + 7) for i in range(3)],
              [button(i) for i in ('.', '0', '<-')],
              [psg.Button('CALCULATE', size=(29, 5))]
              ]
    main_window = psg.Window('Grade Calculator', layout)
    while True:
        event, value = main_window.read()
        if event in (None, 'Close'):
            break
        elif event == 'CALCULATE':
            grade_percentage = grade_calculator.grade_converter(float(dok_grade))
            main_window['OUTPUT'].update(grade_percentage)
            dok_grade = ''
        elif event == '<-':
            dok_grade = dok_grade[:-1]
        else:
            dok_grade += event
        main_window['INPUT'].update(dok_grade)


if __name__ == '__main__':
    main()
