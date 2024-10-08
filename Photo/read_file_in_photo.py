import os


def read_banner():
    with open(os.getcwd() + r'/Photo/banner-2.jpg', 'rb') as file_banner:
        return file_banner.read()


def read_beginner_category():
    with open(os.getcwd() + r'/Photo/beginner.jpg', 'rb') as file_beginner:
        return file_beginner.read()


def read_participant_category():
    with open(os.getcwd() + r'/Photo/participant.jpg', 'rb') as file_participant:
        return file_participant.read()


def read_society_category():
    with open(os.getcwd() + r'/Photo/society.jpg', 'rb') as file_society:
        return file_society.read()
    
    
def read_what_happens_an_p():
    with open(os.getcwd() + r'/Photo/what_happens_an.jpg', 'rb') as file_happens_an:
        return file_happens_an.read()
    

    

