import shutil
import logger


def notes_cover():      # обложка приложения "заметки"
    notes_info = ['=' * 41, 'З А М Е Т К И', '=' * 41]
    width = shutil.get_terminal_size().columns
    position = (width - max(map(len, notes_info))) // 2
    for info in notes_info:
        print(info.center(width))


def notes_menu():       # меню заметок
    print('\tМ Е Н Ю')
    print('\t1. Создать новую заметку')
    print('\t2. Редактировать существующую заметку')
    print('\t3. Прочитать заметку')
    print('\t4. Удалить заметку')
    print('\t5. Закрыть приложение')


def user_choice():
    notes_work = True
    while notes_work:
        choice = input('\n\tВыберите пункт меню: ')
        if int(choice) == 1:
            logger.logging.info('User selected item 1')
        elif int(choice) == 2:
            logger.logging.info('User selected item 2')
        elif int(choice) == 3:
            logger.logging.info('User selected item 3')
        elif int(choice) == 4:
            logger.logging.info('User selected item 4')
        elif int(choice) == 5:
            logger.logging.info('User selected item 5')
            print('Закрытие приложения...')
            logger.logging.info('Shutdown')
            notes_work = False
        else:
            print('Вы ввели неверный пункт меню.')
            logger.logging.info('User input an invalid value')
