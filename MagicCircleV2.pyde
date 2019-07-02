from Element import x_function, y_function, Element
import drawing
import words
import config

def setup():
    if config.seed:
        seed = config.seed
        randomSeed(seed)
    else:
        seed = int(random(10000))
        randomSeed(seed)
    print 'Random seed is: {}'.format(seed)
    size(config.w_width, config.w_height)
    smooth(8)
    ellipseMode(RADIUS)
    imageMode(CENTER)
    noFill()
    frameRate(config.framerate)
    strokeWeight(config.stroke_weight)
    stroke(config.stroke_color)
    strokeCap(SQUARE)
    strokeJoin(ROUND)
    if config.font:
        textFont(createFont(config.font, config.font_clarity))
    if config.looping == 0:
        noLoop()
    
    global elements
    elements = []
    

    #Core Ring
    if random(1.0) > 0.5:
        print 'Standard Core'
        elements.append(Element(0, 0, 0, 0, 0, ellipse, 0, 0, config.radius, config.radius))
    else:
        print 'Double Core'
        font_point = 18
        elements.append(Element(0, 0, 0, 0, 0, drawing.double_ring, 0, 0, config.radius, font_point + 4))
        core_word_list = []
        for i in xrange(int(random(2,10))):
            core_word_list.append(words.elements[int(random(len(words.elements)))])
        core_string = ' '.join(core_word_list)
        core_string += ' '
        print 'Core string is: {}'.format(core_string)
        elements.append(Element(0, 0, 1, config.base_frequency, random(TWO_PI), drawing.text_ring, 0, 0, config.radius, core_string, font_point))
    
    #Child Related
    child_frequency = random(config.base_frequency/4, config.base_frequency)
    child_phase = random(TWO_PI)
    child_radius = config.radius / 3
    num_children = int(random(3, 10))
    
    print 'Frequency, Phase, Num are respectively: {}, {}, {}'.format(child_frequency, child_phase, num_children)
    
    star_type = random(1.0)
    if star_type > 0.80:
        print 'N star with quads NOT YET IMPLEMENTED'
    elif star_type > 0.60:
        print 'N_star'
        elements.append(Element(0, 0, -1, child_frequency, child_phase, drawing.n_star, 0, 0, num_children, config.radius, int(random(num_children))))
    elif star_type > 0.40:
        print 'N_star_concave'
        elements.append(Element(0, 0, -1, child_frequency, child_phase, drawing.n_star_concave, 0, 0, num_children, config.radius, random(0.3, 0.55) * config.radius))
    elif star_type > 0.20:
        print 'N_gon'
        elements.append(Element(0, 0, -1, child_frequency, child_phase, drawing.n_gon, 0, 0, num_children, config.radius))
    else:
        print 'No center star'
        pass
    
    for child in xrange(num_children):
        child_type = random(1.0)
        if child_type > 0.1:
            #elements.append(Element(x_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), y_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), 2, 0, 0,
            #                        drawing.ring, 0, 0, child_radius, True))
            elements.append(Element(x_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), y_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), 2, 0, 0,
                                    drawing.double_ring, 0, 0, child_radius-5, 10, True))
            if child_type > 0.1:
                elements.append(Element(x_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), y_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), 3,
                                        random(-config.base_frequency, config.base_frequency), random(TWO_PI),
                                        drawing.n_star, 0, 0, int(random(5,13)), child_radius-10, int(random(2,5))))
                pass
            else:
                print 'symbol'
                pass
                #symbol
        else:
            elements.append(Element(x_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), y_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), 2, 0, 0,
                                    drawing.ring, 0, 0, child_radius, True))
            elements.append(Element(x_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), y_function((child_frequency, config.radius, ((child-1)*(TWO_PI/num_children) + child_phase))), 3,
                                    random(-config.base_frequency, config.base_frequency), random(TWO_PI),
                                    drawing.moon, 0, 0, child_radius * 0.9, 0.85))
            pass
            #moon
    
    
    elements.sort(key = lambda element: element.z)


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
