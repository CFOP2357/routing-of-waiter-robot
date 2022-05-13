#!/usr/bin/env pybricks-micropython

import path_manager
import motion_and_perception
from constants import *

motion_and_perception.ev3.speaker.beep()

for goal_position in goal_positions:
    path = path_manager.generate_path((motion_and_perception.y_position, motion_and_perception.x_position), 
                                    motion_and_perception.current_direction, goal_position)
    #print("path generated")
    path_manager.follow_path(path)
    motion_and_perception.ev3.speaker.beep()
    motion_and_perception.ev3.speaker.beep()
    motion_and_perception.ev3.speaker.beep()