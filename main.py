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
def move_backward(speed):
    """
    Robot moves backward following a line to the next corner on the back
    """
    robot.drive(-50, 0)
    wait(500)
    while True:
        left_is_white = left_line_sensor.reflection() > 15
        right_is_white = right_line_sensor.reflection() > 15

        if left_is_white and right_is_white:
            robot.drive(-speed, 0)
        if left_is_white and not right_is_white:
            robot.drive(-speed, 30)
        if not left_is_white and right_is_white:
            robot.drive(-speed, -30)
        if not left_is_white and not right_is_white:
            robot.stop(Stop.BRAKE)
            break

        wait(10)

def move_forward(speed):
    """
    Robot moves forward following a line to the next corner on the front
    """
    robot.drive(50, 0)
    wait(500)
    while True:
        left_is_white = left_line_sensor.reflection() > 15
        right_is_white = right_line_sensor.reflection() > 15

        if left_is_white and right_is_white:
            robot.drive(speed, 0)
        if left_is_white and not right_is_white:
            robot.drive(speed, 30)
        if not left_is_white and right_is_white:
            robot.drive(speed, -30)
        if not left_is_white and not right_is_white:
            robot.stop(Stop.BRAKE)
            break

        wait(10)

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()

for x in range(1, 8):
    move_forward(DRIVE_SPEED)