import psutil
from gui import *
from tinker import *


def check_dota2_process():
    for proc in psutil.process_iter():
        if proc.name() == "dota2.exe":
            return True
    return False


def main():
    gui.init_menu()
    print(f"Это тестовая версия скрипта без интерфейса")
    if check_dota2_process():
        print("Dota 2 запущена")
    else:
        print("Dota 2 не запущена")
    dpg.start_dearpygui()


if __name__ == '__main__':
    gui = GUI()
    main()
