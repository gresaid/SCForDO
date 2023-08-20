import time

import dearpygui.dearpygui as dpg
import pyperclip as pyperclip


def count_down():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = 12 * 60 - int(elapsed_time)
        min_time = 8 * 60 - int(elapsed_time)
        if remaining_time <= 0 and min_time <= 0:
            break

        mins_max, secs_max = divmod(remaining_time, 60)
        mins_min, secs_min = divmod(min_time, 60)
        time_str_max = "{:02d}:{:02d}".format(mins_max, secs_max)
        time_str_min = "{:02d}:{:02d}".format(mins_min, secs_min)

        # обновление текста метки
        dpg.set_value('roshan_timer', 'Max timing ' + f'{time_str_max} ' + 'Min timing ' + f'{time_str_min}')
        time.sleep(0.1)