import shutil
import logger


app_name = ['=' * 41, 'З А М Е Т К И', '=' * 41]


def notes_cover():          # обложка приложения "заметки"
    width = shutil.get_terminal_size().columns
    position = (width - max(map(len, app_name))) // 2
    for info in app_name:
        print(info.center(width))


def notes_main_menu():      # главное меню заметок
    print(app_name)
    print('\tМ Е Н Ю')
    print('\t1. Создать новую заметку')
    print('\t2. Редактировать существующую заметку')
    print('\t3. Прочитать заметку')
    print('\t4. Удалить заметку')
    print('\t5. Закрыть приложение')


def notes_editor_submenu():        # подменю заметок
    print(app_name)
    print('Р Е Д А К Т И Р О В А Н И Е   З А М Е Т О К\t')
    print('\t1. Показать все заметки')
    print('\t2. Выполнить поиск по заголовку')
    print('\t3. Выберите заметку для редактирования')


def notes_reader_submenu():
    print(app_name)
    print('Ч Т Е Н И Е   З А М Е Т О К\t')
    print('\t1. Показать все заметки')
    print('\t2. Выполнить поиск по заголовку')
    print('\t3. Выберите заметку')


def notes_delete_submenu():
    print(app_name)
    print('У Д А Л Е Н И Е   З А М Е Т О К\t')
    print('\t1. Показать все заметки')
    print('\t2. Выберите заметку для удаления')


def user_choice():
    notes_work = True
    while notes_work:
        main_menu_choice = input('\n\tВыберите пункт меню: ')
        if int(main_menu_choice) == 1:
            logger.logging.info('User selected main menu item 1')
        elif int(main_menu_choice) == 2:
            logger.logging.info('User selected main menu 2')
            notes_editor_submenu()
            editor_submenu_choice = int('\n\tВыберите пункт меню: ')
            if int(editor_submenu_choice == 1):
                logger.logging.info('User selected editor submenu item 1')
            elif int(editor_submenu_choice == 2):
                logger.logging.info('User selected editor submenu item 2')
            elif int(editor_submenu_choice == 3):
                logger.logging.info('User selected editor submenu item 3')
            else:
                print('Вы указали неверный пункт. Повторите попытку.')
        elif int(main_menu_choice) == 3:
            logger.logging.info('User selected main menu item 3')
            notes_reader_submenu()
            reader_submenu_choice = int('\n\tВыберите пункт меню: ')
            if int(reader_submenu_choice == 1):
                logger.logging.info('User selected reader submenu item 1')
            elif int(reader_submenu_choice == 2):
                logger.logging.info('User selected reader submenu item 2')
            elif int(reader_submenu_choice == 3):
                logger.logging.info('User selected reader submenu item 3')
            else:
                print('Вы указали неверный пункт. Повторите попытку.')
        elif int(main_menu_choice) == 4:
            logger.logging.info('User selected main menu item 4')
            notes_delete_submenu()
            delete_menu_choice = int("\n\tВыберите пункт меню: ")
            if int(delete_menu_choice == 1):
                logger.logging.info('User selected delete submenu item 1')
            elif int(delete_menu_choice == 2):
                logger.logging.info('User selected delete submenu item 2')
            elif int(delete_menu_choice == 3):
                logger.logging.info('User selected delete submenu item 3')
            else:
                print('Вы указали неверный пункт. Повторите попытку.')
        elif int(main_menu_choice) == 5:
            logger.logging.info('User selected main menu item 5')
            print('Закрытие приложения...')
            logger.logging.info('Shutdown')
            notes_work = False
        else:
            print('Вы ввели неверный пункт меню.')
            logger.logging.info('User input an invalid value')
