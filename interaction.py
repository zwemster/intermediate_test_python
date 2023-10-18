import sys
from user_interface import *


def interaction_method():
    notes_app_wk = True
    while notes_app_wk:
        notes_cover()
        notes_main_menu()
        user_choice()
        sys.exit('Thanks for using an app.')
