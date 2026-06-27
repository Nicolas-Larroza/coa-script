
def move(direction, time_moving,action,screen_manager):
    center = screen_manager.get_coordinates(screen_manager.joystick_center)
    direction = screen_manager.get_coordinates(direction)
    action.w3c_actions.pointer_action.move_to_location(center[0], center[1])
    action.w3c_actions.pointer_action.pointer_down()
    action.w3c_actions.pointer_action.move_to_location(direction[0], direction[1])
    action.w3c_actions.pointer_action.pause(time_moving)
    action.w3c_actions.pointer_action.pointer_up()
    action.perform()