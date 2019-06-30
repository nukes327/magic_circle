import config

def x_function(multiple, num_children, radius):
    return lambda x: cos(multiple * (TWO_PI / num_children) + x) * radius

def y_function(multiple, num_children, radius):
    return lambda y: sin(multiple * (TWO_PI / num_children) + y) * radius

class Element:
    def __init__(self, origin_x, origin_y,  rot_coefficient, own_rot_speed,
                     draw_function, *args):
        self.x = origin_x
        self.y = origin_y
        self.rot_c = rot_coefficient
        self.rot_speed = own_rot_speed
        self.own_rot = 0
        self.draw_function = draw_function
        self.args = args
    
    def display(self):
        with pushMatrix():
            try:
                translate(self.x(config.rotation * self.rot_c), 0)
            except TypeError:
                translate(self.x, 0)
            try:
                translate(0, self.y(config.rotation * self.rot_c))
            except TypeError:
                translate(0, self.y)
            rotate(self.own_rot)
            self.own_rot += self.rot_speed
            self.draw_function(*self.args)
