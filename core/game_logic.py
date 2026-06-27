def ore_present():
    get_screenshot()
    ores = find_minable_ore() 
    if ores:
        return True
    else:
        return False

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