from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput
import random, time, subprocess
from cv_lib import find_minable_ore, search_for_x



def adb_command(command):
    result = subprocess.run(command, shell = True, stdout= subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        pass
        
    else:
        print("something went wrong\n", result.stdout.decode())
        

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
    adb_command("adb shell wm density")

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

def go_to():
    action = new_action()
    action.w3c_actions.pointer_action.move_to_location(391 + + random.randint(-1, 1), 1000+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pointer_down()

    action.w3c_actions.pointer_action.move_to_location(816+ random.randint(-1, 1), 1043)
    action.w3c_actions.pointer_action.pause(0.9)  


    action.w3c_actions.pointer_action.move_to_location(882, 1036+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pause(2) 


    action.w3c_actions.pointer_action.move_to_location(882+ random.randint(-1, 1), 1010)
    action.w3c_actions.pointer_action.pause(1.3)

    action.w3c_actions.pointer_action.move_to_location(948, 866+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pause(3)  


    action.w3c_actions.pointer_action.move_to_location(1100+ random.randint(-1, 1), 1000+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pause(2.8)


    action.w3c_actions.pointer_action.pointer_up()

    action.perform()
    action.reset_actions()
    time.sleep(random.uniform(2,3))
    press_interact()
    time.sleep(random.uniform(2,3))
    action.w3c_actions.pointer_action.move_to_location(333, 972)
    action.w3c_actions.pointer_action.pointer_down()
    action.w3c_actions.pointer_action.move_to_location(200, 1031+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pause(0.7)
    action.w3c_actions.pointer_action.move_to_location(172+ random.randint(-1, 1), 1054)
    action.w3c_actions.pointer_action.pause(0.6)
    action.w3c_actions.pointer_action.move_to_location(145, 988)
    action.w3c_actions.pointer_action.pause(0.2)
    action.w3c_actions.pointer_action.pointer_up()
    action.perform()
    action.reset_actions()
def go_back():
    action = new_action()
    action.w3c_actions.pointer_action.move_to_location(440+ random.randint(-1, 1), 922+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pointer_down()
    action.w3c_actions.pointer_action.move_to_location(706+ random.randint(-1, 1), 871)
    action.w3c_actions.pointer_action.pause(0.7)
    action.w3c_actions.pointer_action.move_to_location(751, 871+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pause(0.5)
    action.w3c_actions.pointer_action.pointer_up()
    action.perform()
    action.reset_actions()
    time.sleep(random.uniform(2,3))
    press_interact()
    time.sleep(random.uniform(2,3))
    action.w3c_actions.pointer_action.move_to_location(357+ random.randint(-1, 1), 811+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pointer_down()
    action.w3c_actions.pointer_action.move_to_location(139+ random.randint(-1, 1), 800+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pause(1)
    action.w3c_actions.pointer_action.move_to_location(125+ random.randint(-1, 1), 871)
    action.w3c_actions.pointer_action.pause(0.5)
    action.w3c_actions.pointer_action.move_to_location(46, 885)
    action.w3c_actions.pointer_action.pause(5.4)
    action.w3c_actions.pointer_action.move_to_location(40, 824+ random.randint(-1, 1))
    action.w3c_actions.pointer_action.pause(1.9)
    # a nudge to the left
    action.w3c_actions.pointer_action.move_to_location(20+ random.randint(-1, 1), 850)
    action.w3c_actions.pointer_action.pause(0.6)
    action.w3c_actions.pointer_action.pointer_up()
    action.perform()
    action.reset_actions()
    
def look_for_more_obsidian():
    action = new_action()
    action.w3c_actions.pointer_action.move_to_location(391, 1000)
    action.w3c_actions.pointer_action.pointer_down()
    action.w3c_actions.pointer_action.move_to_location(591, 1000)
    action.w3c_actions.pointer_action.pause(2)
    action.w3c_actions.pointer_action.pointer_up()
    action.perform()
    action.reset_actions()
    time.sleep(2)
    action.w3c_actions.pointer_action.move_to_location(391, 1000)
    action.w3c_actions.pointer_action.pointer_down()
    action.w3c_actions.pointer_action.move_to_location(100, 989)
    action.w3c_actions.pointer_action.pause(2.2)
    action.w3c_actions.pointer_action.pointer_up()
    action.perform()
    action.reset_actions()
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


driver.quit()

