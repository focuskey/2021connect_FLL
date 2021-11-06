#!/usr/bin/env pybricks-micropython

# from pybricks.tools import wait, StopWatch, DataLog
from init_head import *


# from init_head import lift_motor, forklift_motor, ev3, left_motor, right_motor, robot, gyro_sensor, Show_Screen
from Gyro.task_joy import task_011, task_02, Turn_90, small_Nav_Squal, M13,M12,M10,M11, M05, digTrip, FindTheCross
from Gyro.Gyro_calibrate import resetGyro,button,turn_angle,PID_Gyro, fulsh_gyro, Turn_on_position, calibrate_gyro_offset, gyro_turn, gyro_straight, gyroDrivePID, Show_Screen, Lift_up, Lift_down, turn, lineFollow, lineSquare, lineFollowCC,confirm_half_value


# t = Thread(target = Show_Screen)
# t.start()


resetGyro()

lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start

fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start 

M05() #Swithch Engine  Unload Cargo Ship 
