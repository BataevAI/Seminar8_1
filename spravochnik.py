# программа по работе со справочником
import re
TEXTFILE = 'file.txt'
def phonebook_read():
    with open(TEXTFILE, encoding='UTF-8') as file:
        print(file.read())
      
def contact_add():
    lenght_fio = 30
    input_fio = input('Введите Фамилию, Имя, Отчество через пробел: \n')
    input_phone = input('Введите телефон: \n')
    with open(TEXTFILE, 'a', encoding='UTF-8') as file:
        if len(input_fio) <= lenght_fio: 
            input_fio = '' + input_fio + (lenght_fio - len(input_fio)) * ' '          
            file.write(f'{input_fio} | {input_phone}\n')
def string_add(lst):
    ...

# функция выделения ФИО и номера телефона из общей строки справочника

def import_words(str_1) -> list:

    str_1 = str_1.replace('|', ' ')    
    lst_0 = (re.split(' +', str_1))
    return list(lst_0)

# функция заменты элемента списка по номеру

def change_words2(lst, item, new_item): 
    dict_new = dict(enumerate(lst))
    list_02 = list(map(lambda v: new_item if v is item else dict_new[v], dict_new))
    return list_02

def change_words3(lst, item, new_item) -> dict: 
    dict_new = dict(enumerate(lst))
    list_02 = list(map(lambda v: new_item if v is item else dict_new[v], dict_new))
    return dict(enumerate(list_02))

def change_list_to_dict(lst) -> dict: 
    dict_new = dict(enumerate(lst))
    return dict_new
    


def contact_search():
    with open(TEXTFILE, encoding='UTF-8') as file:
        print('    ')
        search = input('Введите ФИО или телефон для поиска\n')
        file_search = file.read().split('\n')
        flag = True
        lst_2 = []
        for i in file_search:
            if search.lower() in i.lower():
                print('    ')
                print(i)
                lst_2.append(i)
                flag = False 
        if flag: 
            print('Ничего не найдено!\n')
        return lst_2
    
def print_dict(lst):
    for i in lst:
        print(f'номер элемента: {i}, элемент: {lst[i]}')   

# Создание строки из dict по формату справочника
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

def contact_change():
    with open(TEXTFILE, encoding='UTF-8') as file:
        
        search = input('Введите ФИО или телефон для корректировки контакта\n')
        file_search = file.read().split('\n')
        
        lst_2 = []
        
        for i in file_search:
            
            if search.lower() in i.lower():
                                
                lst_2.append(i)                

    if len(lst_2) == 1:
        lst_2 = change_list_to_dict(import_words(str(*lst_2)))
        print_dict(lst_2)
        new_num = int(input('Введите номер элемента, который хотите изменить:\n'))
        new_word = input('Введите элемент, который хотите изменить:\n')
        lst_2[new_num] = new_word
        lst_2 = string_add(lst_2)
        print(f'Строка справочника после изменений будет выглядеть:\n {lst_2} \n')
         
    elif len(lst_2) > 1:
        lst_2 = change_list_to_dict(lst_2)
        print_dict(lst_2)        
        new_num = int(input('Введите номер строки, которую хотите изменить:\n'))
        lst_2 = change_list_to_dict(import_words(lst_2.get(new_num)))
        print_dict(lst_2)
        new_num1 = int(input('Введите номер элемента, которое хотите изменить:\n'))
        new_word1 = input('Введите элемент, который хотите изменить:\n')
        lst_2[new_num1] = new_word1
        lst_2 = string_add(lst_2)
        print(f'Строка справочника после изменений будет выглядеть так:\n {lst_2} \n')
    elif len(lst_2) == 0:
        print('Ничего не найдено!\n')


def main():
  
    while True:
        print(' ')
        print(  'Введите название команды для справочника: \n'
                '\n'
                '  введите ad - для добавления контакта в справочник \n'
                '  введите re - для чтения справочника \n'
                '  введите se - для поиска в справочнике \n'
                '  введите st - для завершения работы со справочником \n'
                '  Введите ch - для название изменения данных справочника \n')
        mode = input()
        if mode   == 'ad': contact_add()
        elif mode == 're': phonebook_read()
        elif mode == 'se': contact_search()
        elif mode == 'ch': contact_change()
        elif mode == 'st': break


if __name__ == '__main__': 
    main()
  