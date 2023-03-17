# программа по работе со справочником
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

def contact_change():
    with open(TEXTFILE, encoding='UTF-8') as file:
        print('    ')
        search = input('Введите ФИО или телефон для корректировки контакта\n')
        file_search = file.read().split('\n')
        flag = True
        lst_2 = []
        lst_3 = []
        for i in file_search:
            
            if search.lower() in i.lower():
                # print('    ')
                print(i)                
                lst_2.append(i)
                flag = False 
            if flag: 
                print('Ничего не найдено!\n')
        
        print("Введите цифру строки, которую будем менять")
        enum = enumerate(lst_2)
        for id, item in enum:
            print(id, item)

        num_of_str = int(input())
        for id, item in enum:
            if num_of_str == id:
                print(item)
   

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
  