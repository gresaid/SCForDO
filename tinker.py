import random
import time

import dearpygui.dearpygui as dpg
import yaml
from pynput import keyboard

from item import *

with open('config.yaml', 'r') as file:
    # Загружаем содержимое файла в переменную
    data = yaml.safe_load(file)
pressed = False
listener = None

delay = random.uniform(0.05, 0.15)
long_delay = random.uniform(0.1, 0.2)

blink_value_key = data['tinker']['item']['blink']
soul_ring_key = data['tinker']['item']['soul_ring']
ethereal_blade_key = data['tinker']['item']['ethereal_blade']
shiva_guard_key = data['tinker']['item']['shiva_guard']
hex_d_key = data['tinker']['item']['hex_d']

laser_key = data['tinker']['skills']['laser']
rocket_key = data['tinker']['skills']['rocket']
rearm_key = data['tinker']['skills']['rearm']

cansel_button = data['main_conf']['cansel_button']
combo_button = data['tinker']['main_combo_button']
rocket_combo_button = data['tinker']['rocket_combo_button']
rearm_combo_button = data['tinker']['rearm_combo_button']


def main_combo():
    if dpg.get_value("blink_key"):
        blink_dagger(keyboard.KeyCode.from_char(f'{blink_value_key}'))
        time.sleep(delay)
    if dpg.get_value("soul_ring_key"):
        soul_ring(keyboard.KeyCode.from_char(f'{soul_ring_key}'))
        time.sleep(delay)
    if dpg.get_value("Hex_key"):
        hex_d(keyboard.KeyCode.from_char(f'{hex_d_key}'))
        time.sleep(delay)
    if dpg.get_value("Ethereal_key"):
        ethereal_blade(keyboard.KeyCode.from_char(f'{ethereal_blade_key}'))
        time.sleep(delay)
    if dpg.get_value("rocket_key"):
        rocket(keyboard.KeyCode.from_char(f'{rocket_key}'))
        time.sleep(delay)
    if dpg.get_value("Shivas guard"):
        shiva_guard(keyboard.KeyCode.from_char(f'{shiva_guard_key}'))
        time.sleep(long_delay)
    if dpg.get_value("laser_key"):
        laser(keyboard.KeyCode.from_char(f'{laser_key}'))
        time.sleep(0.5)

        laser(keyboard.KeyCode.from_char(f'{cansel_button}'))
    if dpg.get_value("rearm_key"):
        rearm(keyboard.KeyCode.from_char(f'{rearm_key}'))


def rocket_combo():
    if dpg.get_value("blink_key"):
        blink_dagger(keyboard.KeyCode.from_char(f'{blink_value_key}'))
        time.sleep(delay)

    if dpg.get_value("soul_ring_key"):
        soul_ring(keyboard.KeyCode.from_char(f'{soul_ring_key}'))
        time.sleep(delay)

    if dpg.get_value("rocket_key"):
        rocket(keyboard.KeyCode.from_char(f'{rocket_key}'))
        time.sleep(delay)
    if dpg.get_value("Shivas guard"):
        shiva_guard(keyboard.KeyCode.from_char(f'{shiva_guard_key}'))
        time.sleep(long_delay)
    if dpg.get_value("rearm_key"):
        rearm(keyboard.KeyCode.from_char(f'{rearm_key}'))


def rearm_combo():
    if dpg.get_value("Rearm+soul"):
        rearm(keyboard.KeyCode.from_char(f'{rearm_key}'))
        time.sleep(delay)
        soul_ring(keyboard.KeyCode.from_char(f'{soul_ring_key}'))


def on_press(key):
    global pressed
    if key == keyboard.KeyCode.from_char(f'{combo_button}') and not pressed:
        pressed = True
        main_combo()
    if key == keyboard.KeyCode.from_char(f'{rocket_combo_button}') and not pressed:
        pressed = True
        rocket_combo()
    if key == keyboard.KeyCode.from_char(f'{rearm_combo_button}') and not pressed:
        pressed = True
        rearm_combo()


def on_release(key):
    global pressed
    if key == (keyboard.KeyCode.from_char(f'{combo_button}')):
        pressed = False
    if key == (keyboard.KeyCode.from_char(f'{rocket_combo_button}')):
        pressed = False
    if key == (keyboard.KeyCode.from_char(f'{rearm_combo_button}')):
        pressed = False


def start_listener():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()


def stop_listener():
    global listener
    if listener is not None:
        listener.stop()
        listener.join()
