import shutil
import logger
from menu_functions import *


app_name = ['=' * 41, 'N O T E S', '=' * 41]


def notes_cover():          # обложка приложения "заметки"
    width = shutil.get_terminal_size().columns
    position = (width - max(map(len, app_name))) // 2
    for info in app_name:
        print(info.center(width))


def notes_main_menu():      # главное меню заметок
    print(app_name)
    print('\tM E N U')
    print('\t1. Add new note')
    print('\t2. Edit note')
    print('\t3. Read note')
    print('\t4. Delete note')
    print('\t5. Quit app')


def notes_editor_submenu():        # подменю заметок
    print(app_name)
    print('N O T E   E D I T O R\t')
    print('\t1. Show all notes')
    print('\t2. Select note to edit')


def notes_reader_submenu():
    print(app_name)
    print('N O T E   R E A D E R\t')
    print('\t1. Show all notes')
    print('\t2. Select note')


def notes_delete_submenu():
    print(app_name)
    print('N O T E   D E L E T E R\t')
    print('\t1. Show all notes')
    print('\t2. Select note to delete')


def get_valid_choice(prompt, min_value, max_value):
    while True:
        try:
            choice = int(input(prompt))
            if min_value <= choice <= max_value:
                return choice
            else:
                print('Please, input the number from {} to {}.'.format(min_value, max_value))
        except ValueError:
            print('Please, input correct number.')


def user_choice():
    notes_work = True
    while notes_work:
        main_menu_choice = get_valid_choice('\n\tSelect menu item: ')
        if int(main_menu_choice) == 1:
            logger.logging.info('User selected main menu item 1')
            title = input('Input the name of note: ')
            body = input('Input the note: ')
            add_note(file_name, title, body)
        elif int(main_menu_choice) == 2:
            logger.logging.info('User selected main menu 2')
            notes_editor_submenu()
            editor_submenu_choice = get_valid_choice('\n\tSelect menu item: ')
            if int(editor_submenu_choice == 1):
                logger.logging.info('User selected editor submenu item 1')
                list_notes(file_name)
            elif int(editor_submenu_choice == 2):
                logger.logging.info('User selected editor submenu item 2')
                note_title_to_edit = input('Input title of a note to edit: ')
                new_title = input('Input new title: ')
                new_note = input('Input new note: ')
                edit_note(note_title_to_edit, new_title, new_note)
            else:
                print('Wrong item. Try again.')
        elif int(main_menu_choice) == 3:
            logger.logging.info('User selected main menu item 3')
            notes_reader_submenu()
            reader_submenu_choice = get_valid_choice('\n\tSelect menu item: ')
            if int(reader_submenu_choice == 1):
                logger.logging.info('User selected reader submenu item 1')
                list_notes(file_name)
            elif int(reader_submenu_choice == 2):
                logger.logging.info('User selected reader submenu item 2')
                note_title_to_read = input('Input title of a note to edit: ')
                read_note(file_name, note_title_to_read)
            else:
                print('Wrong item. Try again.')
        elif int(main_menu_choice) == 4:
            logger.logging.info('User selected main menu item 4')
            notes_delete_submenu()
            delete_menu_choice = get_valid_choice("\n\tSelect menu item: ")
            if int(delete_menu_choice == 1):
                logger.logging.info('User selected delete submenu item 1')
                list_notes(file_name)
            elif int(delete_menu_choice == 2):
                logger.logging.info('User selected delete submenu item 2')
                note_title_to_delete = input()
                delete_note(file_name, note_title_to_delete)
            else:
                print('Wrong item. Try again.')
        elif int(main_menu_choice) == 5:
            logger.logging.info('User selected main menu item 5')
            print('Quiting app...')
            logger.logging.info('Shutdown')
            notes_work = False
        else:
            print('Wrong item.')
            logger.logging.info('User input an invalid value')
