import requests
from bs4 import BeautifulSoup


class GetRequests:
    def __init__(self, url):
        self.url = url

    def response(self):
        page_text = requests.get(self.url).text
        return page_text


class ParsingDiary(GetRequests):
    def get_diary(self):
        diary = BeautifulSoup(self.response(), 'html.parser')
        data = diary.find('table', border='0').find_all('td')
        date, name, description = data[0].text, data[1].text, data[2].text
        basic_text, main_text, just_today = data[3].text, data[4].text, data[5].text
        return date, name, description, basic_text, main_text, just_today

    def visual_diary(self):
        diary = self.get_diary()
        return (f'<i>Дата: {diary[0]}\n \n'
                f'Тема: {diary[1]}\n \n{diary[2]}\n'
                f'\n<u>{diary[3]}</u>\n'
                f'\n{diary[4]}\n \n{diary[5]}</i>\n')


o = ParsingDiary('https://na-russia.org/')
o.visual_diary()

























# def get_diary(self):
    #     diary = BeautifulSoup(self.response(), 'html.parser')
    #     data = diary.find('table', border='0').find_all('td')
    #     date, name, description = data[0].text, data[1].text, data[2].text
    #     basic_text, main_text, just_today = data[3].text, data[4].text, data[5].text
    #     return (f'\n<i>Дата: {data}\n \n'
    #             f'Тема: {name}\n \n{description}\n'
    #             f' \n<u>{basic_text}</u>\n'
    #             f'<b>{main_text}</b>\n \n{just_today}</i>\n')