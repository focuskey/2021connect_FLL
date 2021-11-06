from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from pybricks.iodevices import Ev3devSensor

import sys
import os
from threading import Thread


# from Gyro_test import Gyro_Calibrate, gyro_turn, gyro_straight
# from Gyro.Gyro_calibrate import Gyro_Calibrate, gyro_turn, gyro_straight


# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialize the motors connected to the drive wheels.
# Initialize the motors.
# motorA = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
# motorB = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
# left_motor = motorA
# right_motor = motorB
# Sometime the left or right motor be recongnized as medium motor. we should unplug, and replug in
# left_motor.control.limits(speed=600, acceleration=35, actuation=100)
# right_motor.control.limits(speed=600, acceleration=35, actuation=100)
# the positive number + means go down.
# the negative number - means go up.
lift_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
fork_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
# gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
# gyro_sensor.reset_angle(0)
left_color_sensor = ColorSensor(Port.S1)
right_color_sensor = ColorSensor(Port.S2)
# back_color_sensor = ColorSensor(Port.S3)
# sensor = Ev3devSensor(Port.S4)

# color_sensor = Ev3devSensor(Port.S3)
# gyro_sensor = GyroSensor(Port.S4)

#Sometimes the Brick recongise the Large motor to Medieum motor. The solution is to unplug the motor, and repulg in
# robot = DriveBase(left_motor, right_motor)
# robot = DriveBase(left_motor,right_motor,wheel_diameter=92.85,axle_track=158.56)   #The Big round Tire, I found it's slip on the surface
# robot = DriveBase(left_motor, right_motor, wheel_diameter=81.68, axle_track=179)   #formal wheel_diameter=81.68

# After I use rubble and tape on the wheel
# robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=265)   #formal wheel_diameter=81.68 axle=356 axle=112.8
# robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=265)   #formal wheel_diameter=81.68 axle=356 axle=112.8
# robot = DriveBase(left_motor, right_motor, wheel_diameter=81.6, axle_track=110) # The new chris robot
robot = DriveBase(left_motor, right_motor, wheel_diameter=94.2, axle_track=116)   # The New Danny's robot
# robot.settings(straight_speed=200 , straight_acceleration=30, turn_rate=160, turn_acceleration=180) 
# robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=100, turn_acceleration=35)
robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=120)
# robot.distance_control.limits(speed=650, acceleration=35, actuation=100)
# robot.heading_control.limits(speed=650, acceleration=35, actuation=100)
# robot.heading_control.target_tolerances(position=0)
# robot.distance_control.target_tolerances(position=0)
gyro_sensor= GyroSensor(Port.S4)
gyro_sensor.reset_angle(0)
left_motor.reset_angle(0)
right_motor.reset_angle(0)
lift_motor.reset_angle(0)
fork_motor.reset_angle(0)
# robot.reset()
# Initialize the motors.


# colorDetector = ColorSensor(Port.S4)
# gyro_sensor = GyroSensor(Port.S2)

# gyro_sensor_4 = GyroSensor(Port.S4, Direction.CLOCKWISE)

# The GYRO_CALIBRATION_LOOP_COUNT is very important. Control the offset of Gyro, The big of count, the small of Drift.
# the formal value is 600
GYRO_CALIBRATION_LOOP_COUNT = 900
# GYRO_OFFSET_FACTOR is 0.0009
GYRO_OFFSET_FACTOR = 0.0009
TARGET_LOOP_PERIOD = 15  # ms
WHITE_REFLECT_L = 100
BLACK_REFLECT_L = 17
HALF_VLAUE_L = 57
WHITE_REFLECT_R= 75
BLACK_REFLECT_R = 9
HALF_VLAUE_R = 50.5

# ARM_MOTOR_SPEED = 600  # deg/s
gyro_offset =0
# gyro_offset_4 =0

big_font = Font(size=50, bold=True)