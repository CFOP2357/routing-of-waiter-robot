from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


DRIVE_SPEED = 120

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Initialize the color sensor.
left_line_sensor = ColorSensor(Port.S3)
right_line_sensor = ColorSensor(Port.S4)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

def follow_line(speed, direction=1, turn_speed=30):
    """
    Follw black line betwen the two sensors until black in both sensors is detected
    (follow line until sensors on corner)
    """
    while True:
        left_is_white = left_line_sensor.reflection() > 15
        right_is_white = right_line_sensor.reflection() > 15

        if left_is_white and right_is_white:
            robot.drive(speed*direction, 0)
        if left_is_white and not right_is_white:
            robot.drive(speed, turn_speed)
            if direction == -1:
                wait(50)
        if not left_is_white and right_is_white:
            robot.drive(speed, -turn_speed)
            if direction == -1:
                wait(50)
        if not left_is_white and not right_is_white:
            robot.stop(Stop.BRAKE)
            break

        wait(10)

    robot.stop(Stop.BRAKE)

def move_back():
    """
    Robot moves to the corner in the back
    """
    robot.drive(-100, 0)
    wait(1000)
    follow_line(speed = 50, direction = 1, turn_speed = 30)

    robot.drive(-50, 0)
    wait(500)
    follow_line(speed = 50, direction = -1, turn_speed = 10)

def move_front(speed=DRIVE_SPEED):
    """
    Robot moves to the corner in the front
    """
    robot.drive(50, 0)
    wait(500)

    follow_line(speed)

def move_right():
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

def move_left():
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



# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()