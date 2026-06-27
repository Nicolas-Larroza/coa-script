from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput
import random, time, subprocess
def make_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "1663fe56"
    options.automation_name = "UiAutomator2"
    options.newCommandTimeout = 0
    driver = webdriver.Remote(
        "http://localhost:4723",  # Appium server
        options=options
    )
    return driver

def new_action(driver):
    action = ActionChains(driver)
    touch = PointerInput(POINTER_TOUCH, "finger")
    action.w3c_actions.devices.append(touch)
    return action

def adb_command(command):
    result = subprocess.run(command, shell = True, stdout= subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        return result.stdout.decode().strip()
        
    else:
        print("something went wrong\n", result.stderr.decode())

def get_screen_res():
    screen_res = adb_command("adb shell wm size")
    print(screen_res)

def press_interact():
    adb_command("adb shell input tap 1600 870")
    
def get_screenshot():
    adb_command("adb shell screencap /sdcard/game_screenshot.png")
    adb_command("adb pull /sdcard/game_screenshot.png ./game_screenshot.png")

def press_inv():
    adb_command("adb shell input tap 1379 982")

def get_out_of_menu():
    adb_command("adb shell input tap 1 1")

class Screen_manager():
    def __init__(self):
        self.screen_dimensions = self.get_screen_dimensions()
        self.joystick_radius = 11
        self.joystick_center = (47, 36)
    def get_screen_dimensions(self):
        screen_dimensions = adb_command("adb shell wm size")
        x = screen_dimensions.split(":")
        clean_list = x[1].split("x")
        for number in range(2):
            clean_list[number] = int(clean_list[number].strip())
        return clean_list

    def get_coordinates(self, percentages: tuple):
        screen_dimensions = self.screen_dimensions
        coordinates = []
        for number in range(2):
            coordinate = int((percentages[number]*screen_dimensions[number])/100)
            coordinates.append(coordinate)
        return coordinates
    

