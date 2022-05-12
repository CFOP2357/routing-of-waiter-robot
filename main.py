#!/usr/bin/env pybricks-micropython

import path_manager
import motion_and_perception
from constants import *

motion_and_perception.ev3.speaker.beep()
motion_and_perception.ev3.speaker.beep()

path = path_manager.generate_path((8, 0), FRONT, (0, 3))
path_manager.follow_path(path)

motion_and_perception.ev3.speaker.beep()
motion_and_perception.ev3.speaker.beep()
motion_and_perception.ev3.speaker.beep()

path = path_manager.generate_path((motion_and_perception.y_position, motion_and_perception.x_position), 
                                   motion_and_perception.current_direction, (8, 0))
path_manager.follow_path(path)

motion_and_perception.ev3.speaker.beep()
motion_and_perception.ev3.speaker.beep()