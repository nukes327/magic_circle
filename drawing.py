import config

#TODO: Moon needs to be changed to use PGraphics to allow proper clipping if filled, and fill should only create white fill, black fill otherwise to prevent weird clipping inside the crescent itself
def moon(x, y, radius, ratio, filled = False):
    with pushStyle():
        ellipseMode(RADIUS)
        if filled:
            fill(255)
        ellipse(x, y, radius, radius)
        if filled:
            fill(0)
        ellipse(radius - (radius * ratio), 0, radius * ratio, radius * ratio)

def sun():
    pass

def eye():
    pass

def ring(x, y, radius, filled = False):
    if filled is True:
        with pushStyle():
            fill(config.background_color)
            stroke(config.background_color)
            ellipse(x, y, radius, radius)
    ellipse(x, y, radius, radius)

#TODO: Add variations of double ellipse that have assorted fill styles rather than blank between
def double_ring(x, y, radius, gap, solid = False):
    ellipseMode(RADIUS)
    if not solid:
        with pushStyle():
            stroke(config.background_color)
            strokeWeight(gap)
            ellipse(x, y, radius, radius)
    else:
        with pushStyle():
            fill(config.background_color)
            ellipse(x, y, radius + gap/2, radius + gap/2)
    
    ellipse(x, y, radius - (gap/2), radius - (gap/2))
    ellipse(x, y, radius + (gap/2), radius + (gap/2))


# This version of double ring leaks memory like crazy, need to look in to moving a dedicated PGraphics object in to each Element object, to avoid creating a new one per drawn item per frame
# def double_ring(x, y, radius, gap, solid = False):
#     pg = createGraphics(2 * radius + 2 * gap, 2 * radius + 2 * gap)
#     pg.beginDraw()
#     pg.translate(pg.width / 2, pg.height / 2)
#     pg.ellipseMode(RADIUS)
#     pg.stroke(config.stroke_color)
#     pg.strokeWeight(config.stroke_weight)
#     pg.noFill()
#     if not solid:
#         pg.pushStyle()
#         pg.stroke(config.background_color)
#         pg.strokeWeight(gap)
#         pg.ellipse(x, y, radius, radius)
#         pg.popStyle()
#     else:
#         pg.pushStyle()
#         pg.fill(config.background_color)
#         pg.ellipse(x, y, radius + gap/2, radius + gap/2)
#         pg.popStyle()
#     pg.ellipse(x, y, radius - gap/2, radius - gap/2)
#     pg.ellipse(x, y, radius + gap/2, radius + gap/2)
#     pg.endDraw()
#     image(pg, x, y)
        
def clock():
    pass

def n_gon(x, y, n, r, offset = 0):
    with beginClosedShape():
        for vert in xrange(n):
            vertex(cos(vert * (TWO_PI / n) + offset) * r, sin(vert * (TWO_PI / n) + offset) * r)

def n_star(x, y, n, r, jump, offset = 0):
    if jump == n/2.0:
        j = jump + 1
    else:
        j = jump
    with beginShape(LINES):
        for vert in xrange(n):
            vertex(cos(vert * (TWO_PI / n) + offset) * r, sin(vert * (TWO_PI / n) + offset) * r)
            vertex(cos((vert + j) * (TWO_PI / n) + offset) * r, sin((vert + j) * (TWO_PI / n) + offset) * r)

def n_star_concave(x, y, n, ro, ri, offset = 0):
    with beginClosedShape():
        for vert in xrange(n*2):
            if vert % 2 == 0:
                vertex(cos(vert * (TWO_PI / (n*2)) + offset) * ro, sin(vert * (TWO_PI / (n*2)) + offset) * ro)
            else:
                vertex(cos(vert * (TWO_PI / (n*2)) + offset) * ri, sin(vert * (TWO_PI / (n*2)) + offset) * ri)

def n_star_quads():
    pass

def text_arc(x, y, r, start, stop, string, char_size, offset = 0):
    for index, character in zip(xrange(len(string)-1), string[:-1]):
        symbol(x, y, r, character, char_size, (index * ((stop - start)/(len(string)-1))) + offset)
    symbol(x, y, r, string[-1:], char_size, stop + offset)

def text_ring(x, y, r, string, char_size, offset = 0):
    for index, character in zip(xrange(len(string)), string):
        symbol(x, y, r, character, char_size, (index * (TWO_PI/len(string))) + offset)

def symbol(x, y, r, ch, char_size, offset = 0):
    with pushStyle():
        with pushMatrix():
            fill(config.stroke_color)
            rotate(offset)
            textSize(char_size)
            textAlign(CENTER, CENTER) #NOTE 1
            text(ch, x, y - r + textDescent())


def tether(x1, y1, x2, y2):
    try:
        _x1 = x1(frameCount)
    except TypeError:
        _x1 = x1
    
    try:
        _y1 = y1(frameCount)
    except TypeError:
        _y1 = y1
    
    try:
        _x2 = x2(frameCount)
    except TypeError:
        _x2 = x2
    
    try:
        _y2 = y2(frameCount)
    except TypeError:
        _y2 = y2
        
    line(_x1, _y1, _x2, _y2)
    




"""NOTES:
    
    1: Per the documentation - 
    The vertical alignment is based on the value of textAscent(), which many fonts do not specify correctly. 
    It may be necessary to use a hack and offset by a few pixels by hand so that the offset looks correct. 
    To do this as less of a hack, use some percentage of textAscent() or textDescent() so that the hack works even if you change the size of the font. 
"""
