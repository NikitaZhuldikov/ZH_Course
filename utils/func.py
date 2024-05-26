import json
from datetime import datetime

def loading_file(file_name):
    """Функция загрузки файла и возврата в виде списка"""
    with open(file_name, 'r', encoding='utf-8') as load_file:
        return json.load(load_file)

def filter_list(load_file):
    """Функция фильтрует список в соответствии с фильтрами"""
    json_adjective = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', load_file))
    return json_adjective

def sorts_date(json_adjective):
    """Функция сортирует список в соответствии с фильтрами"""
    json_sort = sorted(json_adjective,key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return json_sort

def get_date(date):
    """Функия формирует даты по фильтрам"""
    obj_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(obj_date, '%d.%m.%Y')

def hidden_number(number):
    """Функция принимает номер карты и шифрует его"""
    requisites = number.split()
    if requisites[0] == "Счет":
        return "Счет **" + number[-4:]
    else:
        card_name = " ".join(requisites[:-1])
        return card_name + " " + requisites[-1][:4] + " " + requisites[-1][4:6] + "** **** " + requisites[-1][-4:]

def get_summa(cheque):
    """Функция формирует сумму в соответствии с фильтрами"""
    return f"{cheque["operationAmount"]["amount"]} {cheque["operationAmount"]["currency"]["name"]}"


def get_main(num_operations=5):
    """Функция выводит операцию"""
    load_json = loading_file("OperationAmount.json")
    filtration = filter_list(load_json)
    sorting = sorts_date(filtration)
    for operation in sorting:
        if num_operations == 0:
            break
        print(get_date(operation["date"]), operation["description"])
        if operation["description"] != "Открытие вклада":
            print(hidden_number(operation["from"]) + " -> ", end="")
        print(hidden_number(operation["to"]))
        print(get_summa(operation), "\n")
        num_operations -= 1










