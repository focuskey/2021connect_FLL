#!/usr/bin/env pybricks-micropython

# from pybricks.tools import wait, StopWatch, DataLog
from init_head import *


# from init_head import lift_motor, forklift_motor, ev3, left_motor, right_motor, robot, gyro_sensor, Show_Screen
from Gyro.task_joy import task_011, task_02, Turn_90, small_Nav_Squal,M11_test, M13,M12,M10, M02, M11, M05, Test, digTrip, FindTheCross
from Gyro.Gyro_calibrate import resetGyro, resetGyro_quick, button,turn_angle,PID_Gyro, Record_Data, fulsh_gyro, Turn_on_position, calibrate_gyro_offset, gyro_turn, gyro_straight, gyroDrivePID, Show_Screen, Lift_up, Lift_down, turn, lineFollow, lineSquare, lineFollowCC,confirm_half_value

#At first we should calibarte the Gyro_sensor, Because the gyro degreee is very important.use resetGyro() function 
# to calibarte teh Gyro degaree to zero.



# The function help me record the angle&distance. help position the location to code.

t = Thread(target = Show_Screen)
t.start()

## Start Main
resetGyro()
# resetGyro_quick()
# M11_test()
# wait(909999999)

# fulsh_gyro()
# Turn_on_position(degree=90, t_rate=700)
# turn(angle=90, turnType=2, turnSpeed=76)
# wait(9000)



# calibrate_gyro_offset()
# gyro_sensor.reset_angle(0) #I had include this sentence in the fuction resetGyro()

# Help me to locate the position to modefiy the code
# t1 = Thread(target= Record_Data)
# t1.start()
# # 

# wait until the button left. It's help me to test the code and fix the problem
# while Button.LEFT not in ev3.buttons.pressed():
#     wait(10)
# button()
# gyro_sensor.reset_angle(0)
# wait(9990000)


# To lift Motor, Speed positive(+)numbers means go up,  Negative(-) number means go down.
# The range of lift motor is 0~780 means low to high
# From 0_______820 degree. 

# lift_motor.run_until_stalled(speed=260, then=Stop.COAST, duty_limit=None)
lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
# lift_motor.run_angle(speed=620, rotation_angle=350, then=Stop.HOLD, wait=True)
# ev3.speaker.beep()
# wait(90000)

# To fork Motor, Speed positve(+) means Hold up. Negative(-) means Open the Hands down and open arms
# 0__________560,
# 150 hold totally
fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None) #start 
# wait(5999)
# fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True) 
# button()
# fork_motor.run_until_stalled(speed=720, then=Stop.HOLD, duty_limit=None)
# the hight of tocu continu
# fork_moto r.run_angle(speed=654, rotation_angle=255, then=Stop.HOLD, wait=False)
# PID_Gyro(angle=0, distance=300, speed=-85)




# Lift up the contineon and hand up
 ############################################
# fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start 
# lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
# fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=False)
# lift_motor.run_angle(speed=120, rotation_angle=355, then=Stop.HOLD, wait=True)
# ############################################ Put down the conainer
# lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #Go down lift position
# fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True) #put down the Grab
# ############################################


# IF the full degree of close to open is 0~590,  100 is the perfect degree for hold continor, I mean the front 
# bar is level 0. perfect for lift up
# fork_motor.run_angle(speed=120, rotation_angle=500, then=Stop.HOLD, wait=True)
# fork_motor.run_angle(speed=120, rotation_angle=470, then=Stop.HOLD, wait=True)


# Test()
# PID_Gyro(angle=-15, distance=211, speed=85)
M13()  #platooning truck
M11()  # Package delivery
M12()  #Large Delievery

M10(Position_Blue=3, Position_Green=1)#Sorting Center

#Round2 Switch Electricity, Cargo Airplane, unuscased cased
button()
ev3.light.on(Color.RED)
resetGyro_quick()
M05() #Switch Engine  Unload Cargo Ship 

# Round3 delivery the innovation project
button()
ev3.light.on(Color.ORANGE)
resetGyro_quick()
M02() #Innovation Project
# wait(90000)

# robot.stop()
# robot.settings(straight_speed=0, straight_acceleration=0, turn_rate=800, turn_acceleration=800)
# gyro_turn(angle=-23, speed=800)



# t1 = Thread(target = Lift_up)
# t1.start()
# button()
# gyro_sensor.reset_angle(0)
# turn(angle=45, turnType=2, turnSpeed=65)
# wait(500)
# gyroDrivePID(0, 675, 75)
# wait(10000)


# t = Thread(target = Lift_down)
# t.start()

# gyroDrivePID(15, 505, 95)
# gyroDrivePID(0, 205, 95)


# robot.drive(130, 100)
# I can do the two thread at same time, And more import transfer the arguments to thread. can more 
# t1 = Thread(target=robot.straight, args=(300,))
# t1.start()
# gyro_turn(-36)

# #in function

# It's very import to use the two sentence to adjust the state of robot.
# make the robot to the urgent turning.
# robot.stop()
# robot.settings(straight_speed=150, straight_acceleration=50, turn_rate=220, turn_acceleration=80)
# gyroDrivePID(0, 120, 150)

# robot.stop()
# robot.settings(straight_speed=330, straight_acceleration=80, turn_rate=0, turn_acceleration=0)
# robot.straight(60)



# robot.stop()
# robot.settings(straight_speed=150, straight_acceleration=50, turn_rate=220, turn_acceleration=80)
# turn(-23, turnType=2, turnSpeed=640)



# t = Thread(target = Lift_up)
# t.start()

# robot.stop()
# robot.settings(straight_speed=150, straight_acceleration=50, turn_rate=560, turn_acceleration=56)
# robot.straight(360)

# robot.stop()
# robot.settings(turn_rate=800, turn_acceleration=87)
# robot.turn(-45)

# turn(26, turnType=2, turnSpeed=120)
# gyroDrivePID(26, 300, 95)

# robot.straight(300)

# for i in range(10):
#     robot.turn(36)
#     wait(3000)
#     robot.turn(-36)





# When arrive the later truck, go up the lift, and the keep going for 200mm
# gyroDrivePID(-21, 200, 80)
# t1 = Thread(target = Lift_up)
# t1.start()

# lift_motor.run_angle(speed=-150, rotation_angle=900, then=Stop.HOLD, wait=True)

# turn(-23, turnType=2, turnSpeed=120)


# turn(0, turnType=2, turnSpeed=120)
# lift_motor.run_angle(speed=-150, rotation_angle=560, then=Stop.HOLD, wait=True)

# robot.straight(100)
# robot.turn(360)
# wait(9000)

# ev3.speaker.beep()
# robot.turn(60)
# ev3.speaker.beep()
# wait(3000)
# ev3.speaker.beep()
# turn(30, turnType=2, turnSpeed=120)
# gyroDrivePID(30, 420, 150)

# wait(9000)
# lift_motor.run_angle(speed=-150, rotation_angle=560, then=Stop.HOLD, wait=True)

# robot.turn(36)

# 
# t1 = Thread(target=gyro_turn, args=(36,))
# t1.start()
# lift_motor.run_until_stalled(speed=150, then=Stop.COAST, duty_limit=None)
# # gyro_turn(36)
# # lift_motor.run_target(speed=150, target_angle= 90, then=Stop.HOLD, wait=False)
# gyroDrivePID(36, 440, 150)


# robot.straight(420)
# robot.turn(360)
# lift_motor.run_until_stalled(speed=30, then=Stop.COAST, duty_limit=None)


# lift_motor.run_until_stalled(speed=150, then=Stop.COAST, duty_limit=None)
# lift_motor.run_until_stalled(speed=-150, then=Stop.COAST, duty_limit=None)
# robot.straight(300)

# for i in range(3000):
#     lift_motor.run_until_stalled(speed=-150, then=Stop.COAST, duty_limit=None)
#     lift_motor.run_until_stalled(speed=150, then=Stop.COAST, duty_limit=None)



# wait(99000)
# ev3.speaker.beep()
# wait(1000)



def lift_up():
    lift_motor.run_angle(speed=-150, rotation_angle=900, then=Stop.HOLD, wait=False)