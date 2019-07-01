import config

#def x_function(multiple, num_children, radius):
#    return lambda x: cos(multiple * (TWO_PI / num_children) + x) * radius

def x_function(*args):
    return lambda t: sum([arg[1]*cos(arg[0]*t + arg[2]) for arg in args])

#def y_function(multiple, num_children, radius):
#    return lambda y: sin(multiple * (TWO_PI / num_children) + y) * radius

def y_function(*args):
    return lambda t: sum([arg[1]*sin(arg[0]*t + arg[2]) for arg in args])

class Element:
    def __init__(self, origin_x, origin_y, own_frequency, own_phase,
                     draw_function, *args):
        self.x = origin_x
        self.y = origin_y
        self.frequency = own_frequency
        self.phase = own_phase
        self.draw_function = draw_function
        self.args = args
    
    def display(self):
        with pushMatrix():
            try:
                translate(self.x(frameCount), 0)
            except TypeError:
                translate(self.x, 0)
            try:
                translate(0, self.y(frameCount))
            except TypeError:
                translate(0, self.y)
            rotate(self.frequency * frameCount + self.phase)
            self.draw_function(*self.args)
