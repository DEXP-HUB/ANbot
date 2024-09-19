import os


def read_about_an():
    with open(os.getcwd() + r'\TextFiles\about_an.txt', 'r', encoding='utf-8') as file:
        return file.read()


def read_what_is_an():
    with open(os.getcwd() + r'\TextFiles\what_is_an.txt', 'r', encoding='utf-8') as file:
        return file.read()


def read_what_happens_an():
    with open(os.getcwd() + r'\TextFiles\what_happens_an.txt', 'r', encoding='utf-8') as file:
        return file.read()


def read_questions_answers():
    with open(os.getcwd() + r'\TextFiles\questions_answers.txt', 'r', encoding='utf-8') as file:
        return file.read()


def read_twelve_steps_an():
    with open(os.getcwd() + r'\TextFiles\twelve_steps_an.txt', 'r', encoding='utf-8') as file:
        return file.read()


def read_twelve_tradition_an():
    with open(os.getcwd() + r'\TextFiles\twelve_tradition_an.txt', 'r', encoding='utf-8') as file:
        return file.read()


def read_twelve_ministries_an():
    with open(os.getcwd() + r'\TextFiles\twelve_ministries_an.txt', 'r', encoding='utf-8') as file:
        return file.read()






