__win_width = 800
__diameter = 500.0
__radius = __diameter / 2
__core_thickness = 10
__children = int(random(3, 13))
__core_offset = 1

def setup():
    size(__win_width, __win_width, P2D)
    smooth(8)
    translate(__win_width / 2, __win_width / 2)
    background(0)
    
    rot_offset = random((2*PI)/3)
    
    while(True):
        if __children < 7:
            min_jump = 1
            max_jump = __children
        else:
            min_jump = 2
            max_jump = __children - 1
        jump = int(random(min_jump, max_jump))
        if jump != __children / 2.0:
            break
    
    child_type = random(1)
    line_type = random(1)
    
    for child in xrange(__children):
        #Current ring X and Y
        x1 = cos(child * ((2*PI)/__children) + rot_offset) * (__radius * __core_offset)
        y1 = sin(child * ((2*PI)/__children) + rot_offset) * (__radius * __core_offset)

        #Direct next ring X and Y
        x2 = cos((child + 1) * ((2*PI)/__children) + rot_offset) * (__radius * __core_offset)
        y2 = sin((child + 1) * ((2*PI)/__children) + rot_offset) * (__radius * __core_offset)
        
        #Next line end X and Y
        xj = cos((child + jump) * ((2*PI)/__children) + rot_offset) * (__radius * __core_offset)
        yj = sin((child + jump) * ((2*PI)/__children) + rot_offset) * (__radius * __core_offset)
        
        child_diameter = min(__diameter / 2.5, dist(x1, y1, x2, y2))
        
        
        if child_type < 0.35 and __children < 7:
            ring( x1, y1, child_diameter, __core_thickness )
        elif child_type < 0.66:
            bump( x1, y1, __radius, __radius * __core_offset, (child * ((2*PI)/__children) + rot_offset), child_diameter, __core_thickness )
        else:
            double_bump( x1, y1, __radius, __radius * __core_offset, (child * ((2*PI)/__children) + rot_offset), child_diameter, __core_thickness, 7 )
        if line_type < 0.5:
            chalk_line( x1, y1, xj, yj, __core_thickness * 0.8 )
        else:
            double_line( x1, y1, xj, yj, __core_thickness * 0.8, 7 * 0.8)

    if random(1) < 0.5:
        double_ring(0, 0, __diameter, __core_thickness, 7)
    else:
        ring(0, 0, __diameter, __core_thickness)

def bump(x, y, R, Ro, rot, d, s, c = None):
    if c is None:
        c = color(255)
    r = d/2.0
    pushStyle()
    noFill()
    stroke(c)
    strokeCap(SQUARE)
    strokeWeight(s)
    #theta = abs((PI + acos((((R**2)+(Ro**2)-(r**2))/(2*Ro*R))))/2)
    theta = abs(acos(((R**2)-(Ro**2)-(r**2))/(2*Ro*r)))
    arc(x, y, d, d, -theta + rot, theta + rot)
    popStyle()

def ring(x, y, d, s, c = None):
    if c is None:
        c = color(255)
    pushStyle()
    noFill()
    stroke(c)
    strokeWeight(s)
    ellipse(x, y, d, d)
    popStyle()

def double_ring(x, y, d, s, ss, c = None, cc = None):
    if c is None:
        c = color(255)
    if cc is None:
        cc = color(0)
    ring(x, y, d, s, c)
    ring(x, y, d, s - ss, cc)

def double_bump(x, y, R, Ro, rot, d, s, ss, c = None, cc = None):
    if c is None:
        c = color(255)
    if cc is None:
        cc = color(0)
    bump(x, y, R, Ro, rot, d, s, c)
    bump(x, y, R, Ro, rot, d, s - ss, cc)

def chalk_line(x, y, xx, yy, s, c = None):
    if c is None:
        c = color(255)
    pushStyle()
    stroke(c)
    strokeCap(SQUARE)
    strokeWeight(s)
    line(x, y, xx, yy)
    popStyle()

def double_line(x, y, xx, yy, s, ss, c = None, cc = None):
    if c is None:
        c = color(255)
    if cc is None:
        cc = color(0)
    chalk_line(x, y, xx, yy, s, c)
    chalk_line(x, y, xx, yy, s - ss, cc)

def ref_point(x, y, radius = 8, c = None):
    if c is None:
        c = color(255, 0, 0)
    pushStyle()
    noStroke()
    fill(c)
    ellipse(x, y, radius, radius)
    popStyle()
