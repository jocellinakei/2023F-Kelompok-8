def walk():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    
def jump():
    move()
    walk()
    
while not at_goal():
    jump()
