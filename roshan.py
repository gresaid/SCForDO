import asyncio
import threading
import time

import dearpygui.dearpygui as dpg


async def count_down():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = 12 - int(elapsed_time)
        min_time = 8 - int(elapsed_time)
        if remaining_time <= 0 and min_time <= 0:
            break

        mins_max, secs_max = divmod(remaining_time, 60)
        mins_min, secs_min = divmod(min_time, 60)
        time_str_max = "{:02d}:{:02d}".format(mins_max, secs_max)
        time_str_min = "{:02d}:{:02d}".format(mins_min, secs_min)

        # обновление текста метки
        dpg.set_value('roshan_timer', 'Max timing ' + f'{time_str_max} ' + 'Min timing ' + f'{time_str_min}')
        await asyncio.sleep(0.1)


def start_timer():
    threading.Thread(target=asyncio.run, args=(count_down(),)).start()


def copy_timer():
    dpg.set_clipboard_text(dpg.get_value('roshan_timer'))
    print(dpg.get_clipboard_text())
