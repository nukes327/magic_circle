from Element import x_function, y_function, Element
import drawing
import config

def setup():
    size(config.w_width, config.w_height, P2D)
    smooth(8)
    ellipseMode(RADIUS)
    noFill()
    frameRate(config.framerate)
    strokeWeight(config.stroke_weight)
    stroke(config.stroke_color)
    strokeCap(SQUARE)
    strokeJoin(ROUND)
    if config.font:
        textFont(createFont(config.font, config.font_clarity))
    
    noLoop()
    
    global elements
    elements = []
    elements.append(Element(0, 0, 0, 0, ellipse, 1, 0, config.radius, config.radius))   
    elements.append(Element(0, 0, 0, 0, drawing.double_ellipse, 0, 0, config.radius + 80, 20))

    elements.append(Element(0, 0, config.base_frequency, 0, drawing.n_star_concave, 0, 0, 12, config.radius + 70, config.radius))
    
    moon = Element(x_function((config.base_frequency, config.radius / 2, 0)), y_function((config.base_frequency, config.radius / 5, 0)), config.base_frequency, PI, drawing.moon, 0, 0, config.radius / 4, 0.85)
    elements.append(moon)
    
    
    elements.append(Element(0, 0, 0, 0, drawing.tether, 0, 0, x_function((config.base_frequency, config.radius / 2, 0),(config.base_frequency, config.radius / 4, PI)), 
                            y_function((config.base_frequency, config.radius / 5, 0), (config.base_frequency, config.radius / 4, PI))))


def draw():
    background(config.background_color)
    translate( width / 2, height / 2)
    for element in elements:
        element.display()

def mousePressed():
    if config.looping == 0:
        config.looping = 1
        loop()
    else:
        config.looping = 0
        noLoop()
