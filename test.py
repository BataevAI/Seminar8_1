
import re
TEXTFILE = 'file.txt'
str_3 =  'Baffie  kot       Bara                | 12445'
# str_4 =  'Gringo Valley Skott            | 345'
lst_5 = ['Gringo', 'Valley', 'Skott', '345', '345345353454']
# print(dict(enumerate(lst_5)))
# функция выделения ФИО и номера телефона из общей строки справочника

def import_words(str_1) -> list:

    str_1 = str_1.replace('|', ' ')    
    lst_0 = (re.split(' +', str_1))
    return list(lst_0)

# print(import_words(str_4))


def change_words1(lst, item, new_item) -> dict:
    dict_1 = dict(enumerate(lst))
    for i in dict_1:
        if i is item:
            dict_1[i] = new_item      
    return dict_1
    
def change_words(lst, item, new_item) -> list:

    list_01 = list(map(lambda t: new_item if t is item else t, lst))
    return list_01

def change_words2(lst, item, new_item) -> dict: 
    dict_new = dict(enumerate(lst))
    list_02 = list(map(lambda v: new_item if v is item else dict_new[v], dict_new))
    return dict(enumerate(list_02))

# print(change_words2(import_words(str_3), 0, 'Batanaaev'))


# dict_2 = {0: 'Terminator', 1: 'T800', 2: '0000'}
# lst_5 = [dict_2.get(i) for i in dict_2]


dict_3 = {0: 'Rambo John                     | 111',
1: 'Joan Linsky                    | 564',
2: 'John Sm                        | 124', 
3: 'Smith John                     | 111'}

# print(dict_3[2])

dict_4 = {0: 'Rambo', 1: 'John', 2: '111'}
# new_num1 = 0
# new_word1 = 'Rob'

# dict_4[new_num1] = new_word1
# print(dict_4)

def string_add(lst):
    lenght_fio = 30
    input_fio = ''
    for i in range(len(lst) - 1):
        input_fio = input_fio + lst.get(i) + ' '
    input_phone = lst.get(len(lst) - 1)

    if len(input_fio) <= lenght_fio:
        input_fio = '' + input_fio + (lenght_fio - len(input_fio)) * ' ' 
        new_str = input_fio + ' | ' + input_phone
    return new_str 

# print(len(dict_4))
# print(dict_4.get(0))
# print(string_add(dict_4))

# def string_add(list_old):
#     lenght_fio = 30
#     input_fio = ''
#     for i in range(len(list_old) - 1):
#         input_fio = input_fio + list_old[i] + ' '
#     input_phone = list_old[len(list_old) - 1]

#     if len(input_fio) <= lenght_fio:
#         input_fio = '' + input_fio + (lenght_fio - len(input_fio)) * ' ' 
#         new_str = input_fio + ' | ' + input_phone
#     return new_str 


# print(string_add(lst_5))

print('      dwfsdfsdf'.strip())

def string_add(list_old):
    lenght_fio = 30
    input_fio = ''
    for i in range(len(list_old) - 1):
        input_fio = input_fio + list_old[i] + ' '
    input_phone = list_old[len(list_old) - 1]

    if len(input_fio) <= lenght_fio:
        input_fio = '' + input_fio + (lenght_fio - len(input_fio)) * ' ' 
        new_str = input_fio + ' | ' + input_phone + '\n'
    return new_str