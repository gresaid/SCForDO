from tinker import *

dpg.create_context()
dpg.create_viewport(title='D2S', width=500, height=500)


def activate_deactivate_listener(Sender):
    value = dpg.get_value(Sender)
    if value:
        start_listener()
    else:
        stop_listener()


with dpg.window(label="Tinker", width=500, height=500):
    dpg.add_checkbox(label="Start/Stop Listening",
                     callback=activate_deactivate_listener)
    dpg.add_checkbox(label="Soul Ring + Rearm", tag="Rearm+soul")
    dpg.add_slider_int(label="Level Rearm", default_value=1,
                       max_value=3, min_value=1, tag="lvl_rearm")
    with dpg.collapsing_header(label="Item", default_open=True):
        dpg.add_checkbox(label="Blink dagger", tag="blink_key")
        dpg.add_checkbox(label="Soul Ring", tag="soul_ring_key")
        dpg.add_checkbox(label="Ethereal blade", tag="Ethereal_key")
        dpg.add_checkbox(label="Shiva`s Guard", tag="Shivas guard")
        dpg.add_checkbox(label="Hex", tag="Hex_key")
    with dpg.collapsing_header(label="Skills", default_open=True):
        dpg.add_checkbox(label="Laser", tag="laser_key")
        dpg.add_checkbox(label="Rocket", tag="rocket_key")
        dpg.add_checkbox(label="Rearm", tag="rearm_key")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


# def check_dota2_process():
#     for proc in psutil.process_iter():
#         if proc.name() == "dota2.exe":
#             return True
#     return False


def main():
    # if check_dota2_process():
    #     print("Dota 2 запущена")
    # else:
    #     print("Dota 2 не запущена")
    on_press()


if __name__ == '__main__':
    main()
