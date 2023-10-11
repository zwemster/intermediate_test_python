import shutil


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
