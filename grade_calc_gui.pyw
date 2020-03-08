""" A GUI for the grade converting calculator that I made for my wife"""

import PySimpleGUI as psg
import pyperclip

import grade_calculator


def output(text):
    """The output section of the calculator"""
    return psg.Text(text, key='OUTPUT', size=(12, 0),
                    background_color='dark green', text_color='black', font=('Helvetica', 25), pad=(0, 0))


def input_screen():
    """The input section of the calculator"""
    return psg.Text('', key='INPUT', size=(12, 0), justification='right', font=('Helvetica', 25),
                    background_color='dark green', pad=(0, 0), text_color='black')


def num_button(text):
    """The number buttons"""
    return psg.Button(text, size=(5, 2), pad=None, button_color=('yellow', 'black'), font=('Helvetica', 14, 'bold'))


def calculate_button(text):
    """The magic button"""
    return psg.Button(text, size=(18, 3), pad=(2, 0),  button_color=('yellow', 'black'), font=('Helvetica', 15, 'bold'))


def open_window_message(text):
    """Text for the opening window, tells what this thing does"""
    return psg.Text(text, font=('Helvetica', 15), pad=(0, 0))


def ok_button():
    """A button to push to move past the welcome screen"""
    return psg.Ok(size=(10, 2), pad=(2, 0),  button_color=('yellow', 'black'), font=('Helvetica', 15, 'bold'))


def main():
    dok_grade = ''
    psg.ChangeLookAndFeel('Dark')

    open_window_layout = [[open_window_message('Welcome to the grade calculator!')],
                          [open_window_message('Enter a Depth of Knowledge grade')],
                          [open_window_message('And it will convert for you!')],
                          [open_window_message('It will also copy the grade to')],
                          [open_window_message('the clipboard for convenience')],
                          [ok_button()]]

    layout = [[output('')],
              [input_screen()],
              [num_button(i + 1) for i in range(3)],
              [num_button(i + 4) for i in range(3)],
              [num_button(i + 7) for i in range(3)],
              [num_button(i) for i in ('.', '0', '<-')],
              [calculate_button('CALCULATE')]
              ]

    open_window = psg.Window('Grade Calculator', open_window_layout, element_justification='center')
    main_window = psg.Window('Grade Calculator', layout, return_keyboard_events=True, element_justification='center')

    open_window.read()
    open_window.close()

    while True:
        event, value = main_window.read()
        if event in (None, 'Escape:27'):
            break
        elif event in ('CALCULATE', '\r'):
            grade_percentage = grade_calculator.grade_converter(float(dok_grade))
            main_window['OUTPUT'].update(grade_percentage)
            dok_grade = ''
            pyperclip.copy(grade_percentage)
        elif event in ('<-', 'BackSpace:8'):
            dok_grade = dok_grade[:-1]
        elif event in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
            dok_grade += event

        main_window['INPUT'].update(dok_grade)


if __name__ == '__main__':
    main()
