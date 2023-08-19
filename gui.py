import dearpygui.dearpygui as dpg

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
                                     callback=lambda: self.activate_deactivate_listener(),tag='SS_tinker')
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
                    dpg.add_checkbox(label="Legion", tag="Legion")
                with dpg.tab(label='Roshan'):
                    dpg.add_checkbox(label="Roshan", tag="Roshan")

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
