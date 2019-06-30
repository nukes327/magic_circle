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
    elements.append(Element(0, 0, 1, 0, ellipse, 1, 0, config.radius, config.radius))   
    elements.append(Element(0, 0, 10, 10, drawing.double_ellipse, 0, 0, config.radius + 80, 20))

    elements.append(Element(0, 0, 0, -0.01, drawing.n_star_concave, 0, 0, 12, config.radius + 70, config.radius))


def draw():
    background(config.background_color)
    translate( width / 2, height / 2)
    for element in elements:
        element.display()
    config.rotation += config.rotation_speed

def mousePressed():
    if config.looping == 0:
        config.looping = 1
        loop()
    else:
        config.looping = 0
        noLoop()
