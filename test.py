
import re
TEXTFILE = 'file.txt'
TEXTFILE_TOTAL = 'file.txt2'
TEXTFILE_for_correct = 'file.txt1'
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

# def string_add(lst):
#     lenght_fio = 30
#     input_fio = ''
#     for i in range(len(lst) - 1):
#         input_fio = input_fio + lst.get(i) + ' '
#     input_phone = lst.get(len(lst) - 1)

#     if len(input_fio) <= lenght_fio:
#         input_fio = '' + input_fio + (lenght_fio - len(input_fio)) * ' ' 
#         new_str = input_fio + ' | ' + input_phone
#     return new_str 

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

# print('      dwfsdfsdf'.strip())

# def string_add(list_old):
#     lenght_fio = 30
#     input_fio = ''
#     for i in range(len(list_old) - 1):
#         input_fio = input_fio + list_old[i] + ' '
#     input_phone = list_old[len(list_old) - 1]

#     if len(input_fio) <= lenght_fio:
#         input_fio = '' + input_fio + (lenght_fio - len(input_fio)) * ' ' 
#         new_str = input_fio + ' | ' + input_phone + '\n'
#     return new_str
# f = open('file.txt',"r") 
# lines = f.readlines()
# f.close()

# with open('file.txt1') as TEXTFILE_for_correct: ## Открываем файл
#     my_lines = list(TEXTFILE_for_correct) ## Помещаем в список.
# ## Выводим нужные строки (Помним, что массив начинается с 0, так что все указатели на 1 меньше)
#     f1_total = open('file.txt2',"w")

#     for line in lines: 
#         if line != str(my_lines[2]): 
#             f1_total.write(line)
#     f1_total.close()



    # print(my_lines[1])
# -----------------
# f = open('file.txt',"r") 
# lines = f.readlines()
# f.close()

# file_correct = open(TEXTFILE_for_correct,"r")
# lines1 = file_correct.readlines()
# file_correct.close()



    # /------------------
# for line in lines: 
#     if line is not lines1 in file_correct + "\n": f_total.write(line)
    
# f.close() 
# def string_add(list_old):
#     lenght_fio = 30
#     input_fio = ''
#     for i in range(len(list_old) - 1):
#         input_fio = input_fio + list_old[i] + ' '
#     input_phone = list_old[len(list_old) - 1]

#     if len(input_fio) <= lenght_fio:
#         input_fio = '' + input_fio + (lenght_fio - len(input_fio)) * ' ' 
#         new_str = '' + input_fio + ' | ' + input_phone
#     return new_str

# def string_change(str_old, str_new):
#     with open ('file.txt', 'r') as f:
#         old_data = f.read()
#         # str_old = string_add(['Roman', 'Bolgarin', '1223545'])
#         # str_new = 'Harley Davidson                | 567'
#         new_data = old_data.replace(str_old, str_new)

#     with open ('file.txt', 'w') as f:
#         f.write(new_data)

new_word = input('Введите элементы, через пробел, на которые хотите изменить:\n')
new_word = list(map(str, new_word.split()))
print(new_word)
