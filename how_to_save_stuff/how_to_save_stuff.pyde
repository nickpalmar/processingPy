mouth_x = 200
x_velocity = 1

def setup():
    size(400, 400)
    
def draw():
    global mouth_x
    global x_velocity
    mouth_x += x_velocity
    
    if mouth_x >= 350:
        x_velocity = -1
    if mouth_x <= 50:
        x_velocity = 1
    
    background(255)
    noStroke()
    
    # face 
    fill(255, 255, 0)
    ellipse(mouth_x, 200, 280, 300)
    
    # left eye
    fill(255)
    ellipse(mouth_x - 50, 150, 75, 95)
    # iris
    fill(0, 100, 0)
    ellipse(mouth_x - 30, 160, 30, 30)
    
    # right eye
    fill(255)
    ellipse(mouth_x + 50, 160, 75, 95)
    # iris
    fill(0, 100, 0)
    ellipse(mouth_x + 40, 140, 30, 30)
    
    # mouth
    fill(0)
    ellipse(mouth_x, 270, 90, 120)
    
    
    