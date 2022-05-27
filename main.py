import time
import colorama
from colorama import Fore
import os
from tqdm import tqdm


def yabychiy_print(string):
    cls = lambda: os.system('cls')
    cls()
    for char in string:
        print(Fore.GREEN + char, end="", flush=True)
        # time.sleep(0.25)


colorama.init()

questions = {'Какой сейчас год?\n': '2022',
             'В каком городе вы находитесь?\n': 'Костуж',
             'Какой национальный состав населения города?\n': 'Отовичане и барсогорцы',
             'Какой адрес очистного сооружения?\n': 'улица 100лет Партизан 3',
             'Напишите код для окончания задания...\n': 'system_init.finish()'}

yabychiy_print('Программа инициации системы сетевого оборудования городского водоканала города Костуж...\n')

for question in questions:
    answer = ''
    yabychiy_print(question)
    while answer.lower() != questions.get(question).lower():
        yabychiy_print('Ожидаю ответ...\n')
        answer = input()
        for i in tqdm(list(range(300))):
            time.sleep(0.1)
    yabychiy_print('Переходим к следующему шагу...\n')

yabychiy_print(
    'Программа инициации системы сетевого оборудования городского водоканала города Костуж завершена...\nДля '
    'успешного завершения подключитесь к сети "Abeb"')
