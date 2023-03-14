TEXTFILE = 'file.txt'
def phonebook_read():
    with open(TEXTFILE, encoding='UTF-8') as file:
        print(file.read())
      
def contact_add():
   
    in_fio = input('Введите Фамилию, Имя, Отчество через пробел')
    in_ph = input('Введите телефон')
    with open(TEXTFILE, 'a', encoding='UTF-8') as file:
        file.write(f'{in_fio} | {in_ph}\n')


def contact_search():
    with open(TEXTFILE, encoding='UTF-8') as file:
        search = input('Введите ФИО или телефон для поиска')
        file_search = file.read().split('\n')
        flag = True
        for i in file_search:
            if search.lower() in i.lower():
                print(i)
                flag = False 
        if flag: 
            print('Ничего не найдено!')    

def main():
  
    while True:
        print('Введите название команды для справочника \n'
                'введите add - для добавления контакта в справочник\n'
                'введите read - для чтения справочника\n'
                'введите search - для поиска в справочнике\n'
                )
        mode = input()
        if mode == 'add': contact_add()
        elif mode == 'read': phonebook_read()
        elif mode == 'search': contact_search()
        elif mode == 'stop': break


if __name__ == '__main__': 
    main()
  