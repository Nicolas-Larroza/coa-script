import random, time, subprocess
from core.drivers import make_driver, Screen_manager, new_action
from config.game_config import Config, Directions
from core.movement import move


driver = make_driver()
screen_manager = Screen_manager()
directions = Directions(screen_manager)
action = new_action(driver)
move(directions.right, 3,action,screen_manager)


driver.quit()

