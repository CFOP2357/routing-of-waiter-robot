import motion_and_perception as robot

grid = [[0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]]

def follow_path(path):
    """
    follow the path given on a string
    each character indicates some instruction

    'r' = move right
    'l' = move left
    'f' = move front
    'b' = move back
    """
    for instruction in path:
        if instruction == 'f':
            robot.move_front()
        if instruction == 'b':
            robot.move_back()
        if instruction == 'r':
            robot.move_right()
        if instruction == 'l':
            robot.move_left()