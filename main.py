import dearpygui.dearpygui as dpg
import psutil

from tinker import *

dpg.create_context()
dpg.create_viewport(title='D2S', width=1000, height=1000)

with dpg.window(label="Tinker", width=500, height=500):
    dpg.add_checkbox(label="Start/Stop Listening", callback=start_listener)
    dpg.add_slider_int(label="Level Rearm", default_value=1, max_value=3,min_value=1)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


def check_dota2_process():
    for proc in psutil.process_iter():
        if proc.name() == "dota2.exe":
            return True
    return False


def main():
    print(f"Это тестовая версия скрипта без интерфейса")
    if check_dota2_process():
        print("Dota 2 запущена")
    else:
        print("Dota 2 не запущена")
    # on_press()


if __name__ == '__main__':
    main()
