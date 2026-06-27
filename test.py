from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput
import random, time, subprocess
from cv_lib import find_minable_ore, search_for_x

class Config():
    def __init__(self):
        self.screen_dimensions = get_screen_dimensions()
        self.joystick_radius = 11
        self.joystick_center = (47, 36)
class Directions():
    def __init__(self, config_object):
        center = config_object.joystick_center
        r = config_object.joystick_radius
        self.right = (center[0] + r, center[1])
        self.left = (center[0] - r, center[1])
        self.down = (center[0], center[1] + r)
        self.up = (center[0], center[1] - r)

def adb_command(command):
    result = subprocess.run(command, shell = True, stdout= subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        return result.stdout.decode().strip()
        
    else:
        print("something went wrong\n", result.stderr.decode())

def get_screen_dimensions():
    screen_dimensions = adb_command("adb shell wm size")
    x = screen_dimensions.split(":")
    clean_list = x[1].split("x")
    for number in range(2):
        clean_list[number] = int(clean_list[number].strip())
    return clean_list

def get_coordinates(percentages: tuple):
    screen_dimensions = config.screen_dimensions
    coordinates = []
    for number in range(2):
        coordinate = int((percentages[number]*screen_dimensions[number])/100)
        coordinates.append(coordinate)
    return coordinates


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

driver = make_driver()

def get_screen_res():
    screen_res = adb_command("adb shell wm size")
    print(screen_res)

def new_action():
    action = ActionChains(driver)
    touch = PointerInput(POINTER_TOUCH, "finger")
    action.w3c_actions.devices.append(touch)
    return action

def press_interact():
    adb_command("adb shell input tap 1600 870")
    
def get_screenshot():
    adb_command("adb shell screencap /sdcard/game_screenshot.png")
    adb_command("adb pull /sdcard/game_screenshot.png ./game_screenshot.png")

config = Config()
directions = Directions(config)
#direction must be a direction from the class "Directions", such as:
# directions.right
def move(direction, time_moving):
    center = get_coordinates(config.joystick_center)
    direction = get_coordinates(direction)
    action = new_action()
    action.w3c_actions.pointer_action.move_to_location(center[0], center[1])
    action.w3c_actions.pointer_action.pointer_down()
    action.w3c_actions.pointer_action.move_to_location(direction[0], direction[1])
    action.w3c_actions.pointer_action.pause(time_moving)
    action.w3c_actions.pointer_action.pointer_up()
    action.perform()

def ore_present():
    get_screenshot()
    ores = find_minable_ore() 
    if ores:
        return True
    else:
        return False

def press_inv():
    adb_command("adb shell input tap 1379 982")
def get_out_of_menu():
    adb_command("adb shell input tap 1 1")
def is_inv_full():
    press_inv()
    get_screenshot()
    get_out_of_menu()
    if search_for_x("obsidian_inv_ore") > 34:
        return True
    else:
        return False
def empty_inv():
    time.sleep(random.uniform(0.3,0.5))
    press_interact()
    #presses first ore in inv
    time.sleep(random.uniform(2,3))
    adb_command("adb shell input tap 340 340")
    time.sleep(random.uniform(1,2))
    get_out_of_menu()

def mine():
    inv_not_full = True
    if ore_present():
        press_interact()
        time.sleep(5)
    while inv_not_full:
        
        present = ore_present()
        inv_status = is_inv_full()
        #add a check to see if its mining already
        if present and not inv_status:
            press_interact()
            time.sleep(random.randint(8,15))
            action = new_action()
            
        elif inv_status:
            time.sleep(1)
            inv_not_full = False
        elif not present:
            time.sleep(1)
            action = new_action()
            print("no ore found, loser.")
            #look_for_more_obsidian()
            time.sleep(5)


move(directions.right, 3)

"""         
state = 1

def main():
    try:
        global state
        if state == 1:
            go_to()
            state += 1
        if state == 2:
            time.sleep(1)
            mine()
            state += 1
        if state == 3:
            time.sleep(2)
            go_back()
            state += 1
        if state == 4:
            time.sleep(2)
            empty_inv()
            time.sleep(2)
            state = 1
    except Exception as e:
        print(f"an error ocurred, {e}")
        global driver
        driver = make_driver()
        print(state)
        if state == 1 or 3:
            action = new_action()
            action.w3c_actions.pointer_action.move_to_location(0,0)
            action.w3c_actions.pointer_action.pointer_up()
            action.perform()
            action.reset_actions()

for i in range(1,51):
    time.sleep(1)
    print(f"vuelta numero {i}!")
    main()
    print(f"vuelta numero {i} terminada!")
"""

driver.quit()

