#!/usr/bin/env pybricks-micropython

import motion_and_perception as robot

#la pista mide 9x4

robot.move_front()
robot.move_back()

for x in range(0, 4):
    robot.turn_left()
    robot.move_front()

ev3.speaker.beep()
