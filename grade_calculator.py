""" A grade calculator that takes depth of knowledge grade and translates it into a percentage,
based on a lopsided scale, so that a more traditional grade can be entered into powerschool"""
import numpy
import pyperclip

"""
PD = 3.5-4 = 90-100     len(51)
P = 2.5-3.4 = 75-89     len(91)
BP = 2-2.4 = 65-74      len(41)
I = 1.5-1.9 = 55-64     len(41)
N = 0-1.4 = 0-54        len(141)

"""

"""Setting my constant lists to reflect the score ranges referenced above"""
PD_RANGE_LIST = [i for i in numpy.arange(90, 100, .198).round(decimals=1)]
PD_GRADE_RANGE = [i for i in numpy.arange(3.5, 4.01, .01).round(decimals=2)]

P_RANGE_LIST = [i for i in numpy.arange(75, 89, .14).round(decimals=1)]
P_GRADE_RANGE = [i for i in numpy.arange(2.5, 3.49, .01).round(decimals=2)]

BP_RANGE_LIST = [i for i in numpy.arange(65, 74, .18).round(decimals=1)]
BP_GRADE_RANGE = [i for i in numpy.arange(2, 2.49, .01).round(decimals=2)]

I_RANGE_LIST = [i for i in numpy.arange(55, 64, .185).round(decimals=1)]
I_GRADE_RANGE = [i for i in numpy.arange(1.5, 1.99, .01).round(decimals=2)]

N_RANGE_LIST = [i for i in numpy.arange(0, 54, .363).round(decimals=1)]
N_GRADE_RANGE = [i for i in numpy.arange(0, 1.49, .01).round(decimals=2)]


""" These functions all work by taking the depth of knowledge grade and finding its index on 
the list for the depth of knowledge letter scale, which is referenced above"""


def pd_range(depth_of_knowledge_grade):
    index_number = PD_GRADE_RANGE.index(depth_of_knowledge_grade)

    return PD_RANGE_LIST[index_number]


def p_range(depth_of_knowledge_grade):
    index_number = P_GRADE_RANGE.index(depth_of_knowledge_grade)

    return P_RANGE_LIST[index_number]


def bp_range(depth_of_knowledge_grade):
    index_number = BP_GRADE_RANGE.index(depth_of_knowledge_grade)

    return BP_RANGE_LIST[index_number]


def i_range(depth_of_knowledge_grade):
    index_number = I_GRADE_RANGE.index(depth_of_knowledge_grade)

    return I_RANGE_LIST[index_number]


def n_range(depth_of_knowledge_grade):
    index_number = N_GRADE_RANGE.index(depth_of_knowledge_grade)

    return N_RANGE_LIST[index_number]


def grade_converter(depth_of_knowledge_grade):
    """Takes the grade level descriptor and the DKG and finds the percentage range it will be in"""
    if 3.5 <= depth_of_knowledge_grade <= 4:
        grade_percentage = pd_range(depth_of_knowledge_grade)
    elif 2.5 <= depth_of_knowledge_grade <= 3.49:
        grade_percentage = p_range(depth_of_knowledge_grade)
    elif 2 <= depth_of_knowledge_grade <= 2.49:
        grade_percentage = bp_range(depth_of_knowledge_grade)
    elif 1.5 <= depth_of_knowledge_grade <= 1.99:
        grade_percentage = i_range(depth_of_knowledge_grade)
    elif 0 <= depth_of_knowledge_grade <= 1.49:
        grade_percentage = n_range(depth_of_knowledge_grade)
    else:
        grade_percentage = 'DOK grade out of range'

    return grade_percentage


def main():
    while True:
        depth_of_knowledge_grade = input('Enter the DOK grade or "q" to quit: ')
        if depth_of_knowledge_grade == 'q':
            break
        percentage = grade_converter(float(depth_of_knowledge_grade))
        if isinstance(percentage, float):
            pyperclip.copy(percentage)
            print(f'{percentage} - copied to cipboard')
        else:
            print(percentage)


def test_script():
    spam = [i for i in numpy.arange(0, 4.1, .1).round(decimals=1)]
    for i in spam:
        print(f'{i} - {grade_converter(float(i))}')


if __name__ == '__main__':
    main()
