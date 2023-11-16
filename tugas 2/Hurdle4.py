def turn_right():
    turn_left()
    turn_left()
    turn_left()
def pass_wall():
    turn_left()
    count_wall = 0
    while wall_on_right():
        count_wall+=1
        move()
    turn_right()
    move()
    turn_right()
    while count_wall >0:
        move()
        count_wall-=1
    turn_left()
