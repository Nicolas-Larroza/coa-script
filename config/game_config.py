class Config():
    def __init__(self):
        pass
class Directions():
    def __init__(self, screen_manager):
        center = screen_manager.joystick_center
        r = screen_manager.joystick_radius
        self.right = (center[0] + r, center[1])
        self.left = (center[0] - r, center[1])
        self.down = (center[0], center[1] + r)
        self.up = (center[0], center[1] - r)