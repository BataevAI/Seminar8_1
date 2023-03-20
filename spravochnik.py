# программа по работе со справочником
import re

TEXTFILE = 'file.txt'
old_string = ''

def phonebook_read():
    with open(TEXTFILE, encoding='UTF-8') as file:
        print(file.read())

def contact_del():
    with open(TEXTFILE, 'r', encoding = 'utf-8') as file:
        book = file.read().split('\n')
        search = input('Введите данные элемента, которые нужно удалить:\n')
        index = 0
        lst = list()
        for i in book:
            if search.lower() in i.lower():
                print(f'Введите {index}, чтобы удалить {i}')
                lst.append(i)
            index += 1
        if bool(lst):
            del_index = int(input(""))
            book.pop(del_index)
            with open(TEXTFILE, 'w', encoding = 'utf-8') as file:
                for i in book:
                    file.writelines(f'{str(i)}\n')
        else:
            print('нет такого контакта')
 
def change_contact():
    with open(TEXTFILE, 'r', encoding = 'utf-8') as file:
        book = file.read().split('\n')
        find = input('Введите данные элемента, которые нужно изменить:\n')
        index = 0
        temp = list()
        new_word = ''
        for i in book:
            if find.lower() in i.lower():
                print(f'Введите {index}, чтобы изменить {i}')
                
                temp.append(i)
            index += 1
        if bool(temp):
            del_index = int(input(""))          
            
            new_word = string_add1()
            book.pop(del_index)
            book.insert(del_index, new_word)
            with open(TEXTFILE, 'w', encoding = 'utf-8') as file:
                for i in book:
                    file.writelines(f'{str(i)}\n')
        else:
            print('нет такого контакта')   
      
def contact_add():
    lenght_fio = 30
    input_fio = input('Введите Фамилию, Имя, Отчество через пробел: \n')
    input_phone = input('Введите телефон: \n')
    with open(TEXTFILE, 'a', encoding='UTF-8') as file:
        if len(input_fio) <= lenght_fio: 
            input_fio = '' + input_fio + (lenght_fio - len(input_fio)) * ' '          
            file.write(f'{input_fio} | {input_phone}')

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

# Создание строки из list по формату справочника

def string_add1():
   
    lenght_fio = 30
    input_fio = input('Введите Фамилию, Имя, Отчество через пробел: \n')
    input_phone = input('Введите телефон: \n')
    
    if len(input_fio) <= lenght_fio: 
        input_fio = '' + input_fio + (lenght_fio - len(input_fio)) * ' '          
        # file.write(f'{input_fio} | {input_phone}\n')

    return input_fio + ' | ' + input_phone


def main():
  
    while True:
        print(' ')
        print(  'Введите название команды для справочника: \n'
                '\n'
                '  введите ad - для добавления контакта в справочник \n'
                '  введите re - для чтения справочника \n'
                '  введите se - для поиска в справочнике \n'
                '  введите st - для завершения работы со справочником \n'
                '  Введите ch - для изменения данных справочника \n'
                '  Введите del - для удаления данных справочника \n')
        mode = input()
        if mode   == 'ad': contact_add()
        elif mode == 're': phonebook_read()
        elif mode == 'se': contact_search()
        elif mode == 'ch': change_contact()
        elif mode == 'del': contact_del()
        elif mode == 'st': break


if __name__ == '__main__': 
    main()
  