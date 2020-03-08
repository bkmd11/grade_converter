""" A GUI for the grade converting calculator that I made for my wife"""

import PySimpleGUI as psg
import grade_calculator


def output(text):
    return psg.Text(text, key='OUTPUT', size=(12, 0),
                    background_color='dark green', text_color='black', font=('Helvetica', 25), pad=(0, 0))


def num_button(text):
    return psg.Button(text, size=(5, 2), pad=None, button_color=('yellow', 'black'), font=('Helvetica', 14, 'bold'))


def calculate_button(text):
    return psg.Button(text, size=(18, 3), pad=(2, 0),  button_color=('yellow', 'black'), font=('Helvetica', 15, 'bold'))


def input_screen():
    return psg.Text('', key='INPUT', size=(12, 0), justification='right', font=('Helvetica', 25),
                    background_color='dark green', pad=(0, 0), text_color='black')


def main():
    dok_grade = ''
    psg.ChangeLookAndFeel('Dark')
    layout = [[output('')],
              [input_screen()],
              [num_button(i + 1) for i in range(3)],
              [num_button(i + 4) for i in range(3)],
              [num_button(i + 7) for i in range(3)],
              [num_button(i) for i in ('.', '0', '<-')],
              [calculate_button('CALCULATE')]
              ]
    main_window = psg.Window('Grade Calculator', layout, return_keyboard_events=True, element_justification='center')
    while True:
        event, value = main_window.read()
        if event in (None, 'Escape:27'):
            break
        elif event in ('CALCULATE', '\r'):
            grade_percentage = grade_calculator.grade_converter(float(dok_grade))
            main_window['OUTPUT'].update(grade_percentage)
            dok_grade = ''
        elif event in ('<-', 'BackSpace:8'):
            dok_grade = dok_grade[:-1]
        elif event in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
            dok_grade += event

        main_window['INPUT'].update(dok_grade)


if __name__ == '__main__':
    main()
