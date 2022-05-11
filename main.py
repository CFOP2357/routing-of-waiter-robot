#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Initialize the color sensor.
left_line_sensor = ColorSensor(Port.S3)
right_line_sensor = ColorSensor(Port.S4)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

DRIVE_SPEED = 120

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

def follow_line(speed, direction=1):
    while True:
        left_is_white = left_line_sensor.reflection() > 15
        right_is_white = right_line_sensor.reflection() > 15

        if left_is_white and right_is_white:
            robot.drive(speed*direction, 0)
        if left_is_white and not right_is_white:
            robot.drive(speed*direction, 30)
        if not left_is_white and right_is_white:
            robot.drive(speed*direction, -30)
        if not left_is_white and not right_is_white:
            robot.stop(Stop.BRAKE)
            break

        wait(10)

def move_back():
    """
    Robot moves to the corner in the back
    """
    robot.drive(-50, 0)
    wait(500)

    follow_line(50, direction = -1)

def move_front():
    """
    Robot moves to the corner in the front
    """
    robot.drive(50, 0)
    wait(500)

    follow_line(DRIVE_SPEED)

def turn_right():
    """
    Robot moves to the corner in the right
    """
    robot.drive(50, 50)
    wait(1000)

    left_is_white = left_line_sensor.reflection() > 15
    while left_is_white:
        left_is_white = left_line_sensor.reflection() > 15
        robot.drive(50, 50)

    follow_line(DRIVE_SPEED)
    robot.stop(Stop.BRAKE)

def turn_left():
    """
    Robot moves to the corner in the left
    """
    robot.drive(50, -50)
    wait(1000)

    right_is_white = right_line_sensor.reflection() > 15
    while right_is_white:
        right_is_white = right_line_sensor.reflection() > 15
        robot.drive(50, -50)

    follow_line(DRIVE_SPEED)
    robot.stop(Stop.BRAKE)



# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

move_front()
move_back()

for x in range(0, 4):
    turn_left()
    move_front()

ev3.speaker.beep()
