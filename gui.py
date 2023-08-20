import dearpygui.dearpygui as dpg

from roshan import count_down
from tinker import start_listener, stop_listener


class GUI:

    def init_menu(self) -> None:
        dpg.create_context()
        self.set_custom_theme()
        dpg.create_viewport(title="D2S", decorated=True, width=600, height=600)

        with dpg.window(tag='w_main'):
            with dpg.tab_bar():
                with dpg.tab(label='News'):
                    dpg.add_checkbox(label="News", tag="News")
                with dpg.tab(label="Tinker"):
                    dpg.add_checkbox(label="Start/Stop",
                                     callback=lambda: self.activate_deactivate_listener(), tag='SS_tinker')
                    dpg.add_checkbox(label="Soul Ring + Rearm", tag="Rearm+soul", default_value=True)
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
                with dpg.tab(label='Legion'):
                    dpg.add_checkbox(label="Start/Stop",
                                     callback=lambda: self.activate_deactivate_listener(), tag='SS_legion')
                    with dpg.collapsing_header(label="Item", default_open=True):
                        dpg.add_checkbox(label="Blink dagger", tag="blink_key")
                        dpg.add_checkbox(label="Blade mail", tag="soul_ring_key")
                        dpg.add_checkbox(label="Blacking bar", tag="blacking_bar_key")
                        dpg.add_checkbox(label="Orchid", tag="orchid_key")
                    with dpg.collapsing_header(label="Skills", default_open=True):
                        dpg.add_checkbox(label="Arrow", tag="arrow_key")
                        dpg.add_checkbox(label="press_attack", tag="press_attack_key")
                        dpg.add_checkbox(label="duel", tag="duel_key")
                with dpg.tab(label='Roshan'):
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="Start timer", tag="roshan_start_button", callback=lambda: count_down(),
                                       width=150, height=150)
                        dpg.add_button(label="Reset timer", tag='reset_roshan_timer', width=150, height=150)
                        dpg.add_button(label="Copy timer", tag='copy_roshan_timer',
                                       width=150, height=150)
                    dpg.add_text(label='time', tag='roshan_timer')

        dpg.bind_theme('base_theme')
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("w_main", True)

    @staticmethod
    def activate_deactivate_listener() -> None:
        value = dpg.get_value('SS_tinker')
        if value:
            start_listener()
        else:
            stop_listener()

    @staticmethod
    def set_custom_theme() -> None:
        dpg.add_theme(tag='base_theme')
        with dpg.theme_component(parent='base_theme'):
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 9)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 9)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 9)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 9)
            dpg.add_theme_style(dpg.mvStyleVar_TabRounding, 7)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 13)
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (0, 170, 50, 130))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (0, 170, 50, 130))
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (0, 255, 0))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 170, 50, 130))
