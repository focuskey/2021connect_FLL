
from Gyro.Gyro_calibrate import gyro_straight,PID_Gyro, resetGyro,fulsh_gyro, turn_angle,compass,Go_Straight_line, Turn_on_position, gyro_turn, gyroDrivePID, turn, lineFollow, lineSquare, colorChecker, button, colorChecker, lineFollow_Stop_on_Cross
from init_head import * #lift_motor, forklift_motor, ev3, left_motor, right_motor, gyro_sensor
from pybricks.tools import wait, StopWatch, DataLog
from threading import Thread
import sys


# In the py. I define each mission a methord, then, we can use the method to chanllenge the mission.
# M11 the my favoriate mission.
###
# M01_Innovation Project
# M02_Unused Capacity
# M03_Unload Cargo Plan
# M04_Transpotation Journey
# M05_Swithch Engine
# M06_Accident Avoidance
# M07_Unload Cargo Ship
# M08_Air Drop
# M09_Train Tracks
# M10_Sorting Center
# M11_Home Delivery
# M12_Large Delivery
# M13_Platooning Trucks
# M14_Bridge
# M15_Load Cargo
# M16_Cargo CONNECT
# M17_Precision
###



def Turn_90():
    # Gyro_Calibrate()
    gyro_turn(90)
    wait(2000)
    # robot.turn(90)
    # robot.turn(-90)
    # print(gyro_sensor.angle())
    gyro_straight(120)
    gyro_turn(90)
    wait(2000)
    gyro_straight(120)
    # print(gyro_sensor.angle())


def task_push_easy_01():
    gyro_straight(789, 150)
    lift_motor.run_time(375,3000)
    forklift_motor.run_time(375,2000)
    wait(10)
    gyro_straight(-789, 150)

def task_011():
    # print('Start moing')
    Gyro_Calibrate()
    # print('Finish codeing')
    # gyro_sensor.reset_angle(0)
    # gyro_turn(-86.06, 65)
    # print('Finish moing')
    # gyro_sensor.reset_angle(0)
    # gyro_straight(233, 150)
    # gyro_turn(-88.65, 65)
    # print("Start to moving")
    # # print(gyro_sensor.angle())
    wait(100)
    gyro_straight(1429, 90)
    wait(100)
    # print("Finishe moving forward")
    # print(gyro_sensor.angle())
    # print("starting to turn")
    gyro_turn(86.66, 65)
    wait(100)
    # print("Finishe Turning")
    # print(gyro_sensor.angle())
    # print("Start to moving2")
    gyro_straight(135, 70)
    wait(100)
    lift_motor.run_time(375,3000)
    forklift_motor.run_time(375,2000)
    wait(10)
    gyro_straight(-135, 70)
    wait(100)
    # print("starting to turn2")
    # print(gyro_sensor.angle())
    # gyro_turn(-88.69, 65)
    gyro_turn(-86.66, 65)
    # print("Finishe Turning2")    
    # print(gyro_sensor.angle())

    wait(100)
    gyro_straight(-1429, 90)

    # gyro_turn(-88.6, 70)
    # gyro_turn(-88.6, 70)
    # gyro_turn(34,50)
    # gyro_turn(-34,50)
    # gyro_straight(-60, 70)
    # lift_motor.run_time(475,3000)
    # forklift_motor.run_time(242,2000)



def task_02():
    gyro_straight(323, 70)
    gyro_turn(334,50)
    gyro_turn(-334,50)
    gyro_straight(-32, 70)
    lift_motor.run_time(475,3000)


def task_01():
    # gyro_straight(233, 150)
    # gyro_turn(-88.65, 65)
    print("Start to moving")
    # print(gyro_sensor.angle())
    robot.straight(1429)
    wait(100)
    robot.turn(86.06)
    wait(100)
    robot.straight(135)
    wait(100)
    lift_motor.run_time(375,3000)
    forklift_motor.run_time(375,2000)
    wait(10)
    robot.straight(-135)
    wait(100)
    robot.turn(-88.69)
    wait(100)
    robot.straight(-1429)


def task_012():
    print(gyro_sensor.angle())
    Gyro_Calibrate()
    print(gyro_sensor.angle())
    gyro_straight(240, 85)
    print(gyro_sensor.angle())
    wait(10)
    gyro_turn(86.66, 65)
    print(gyro_sensor.angle())
    wait(10)
    print(gyro_sensor.angle())
    gyro_straight(832, 85)
    wait(10)
    print(gyro_sensor.angle())
    gyro_turn(-86.66,65)
    wait(10)
    print(gyro_sensor.angle())
    gyro_straight(220, 85)
    wait(10)
    print(gyro_sensor.angle())
    gyro_straight(-220, 85)
    wait(10)
    print(gyro_sensor.angle())
    gyro_turn(86.66,65)
    wait(10)
    print(gyro_sensor.angle())
    gyro_straight(-832, 85)
    wait(10)
    print(gyro_sensor.angle())
    gyro_turn(-86.66, 65)
    wait(10)
    print(gyro_sensor.angle())
    gyro_straight(-240, 85)
    print(gyro_sensor.angle())

    
    
    
    
    # lift_motor.run_time(375,3000)
    # forklift_motor.run_time(375,2000)
    # wait(10)
    # gyro_straight(-789, 150)
    # print(gyro_sensor.angle())
    # gyro_turn(-86.66,65)


def task_Donot_Use_Gyro():
    robot.stop()
    wait(10)
    robot.settings(straight_speed=260 , straight_acceleration=30, turn_rate=80, turn_acceleration=90)
    robot.straight(1429)
    # gyro_straight(1429, 80)
    robot.stop()
    wait(10)
    robot.turn(92.96)
    robot.stop()
    wait(10)
    robot.settings(straight_speed=80 , straight_acceleration=30, turn_rate=80, turn_acceleration=90)
    robot.straight(186)
    robot.stop()
    wait(10)
    lift_motor.run_time(375,3000)
    forklift_motor.run_time(375,2000)
    wait(10)
    robot.straight(-186)
    robot.stop()
    wait(10)
    robot.turn(-92.96)
    robot.stop()
    wait(10)
    robot.settings(straight_speed=350 , straight_acceleration=30, turn_rate=80, turn_acceleration=90)
    robot.straight(-1445)
    # gyro_straight(-1429, 80)
    robot.stop()
    wait(10)


def small_Nav_Squal():
    # Gyro_Calibrate()
    lift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)
    gyroDrivePID(0, 220, 50)
    turn(90, turnType=2, turnSpeed=56)
    gyroDrivePID(90, 600, 56)
    wait(10)
    turn(0, turnType=2, turnSpeed=56)
    wait(10)
    gyroDrivePID(0, 280, 50)
    wait(10)
    # lift_motor.run_time(375,3000)
    lift_motor.run_target(speed=-125, target_angle=-125, then=Stop.HOLD, wait=True)
    # forklift_motor.run_time(375,2000)
    wait(10)
    gyroDrivePID(0, 280, -50)
    wait(10)
    turn(90, turnType=2, turnSpeed=56)
    wait(10)
    gyroDrivePID(90, 600, -56)
    turn(0, turnType=2, turnSpeed=56)
    gyroDrivePID(0, 220, -50)
    # lift_motor.run_target(speed=-125, target_angle=95, then=Stop.HOLD, wait=True)
    lift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)



def M11_Old():
    # At the test stage, make the Robot fininsed the Tredmill, Row machine, Tire Flip(2Tires),Weightlift machine, cell phone, across the bridge
    # there was two line between the robot and line, one is black (right sight), one is white (front side), 
    # Both of them are very small like the hire thick

    #First Adjust the lift_motor and forklift_motor
    lift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)
    forklift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)
    
    # The most import part is calibrate the Gyro Sensor, Make the read method to recalibrate 10 times
    cali_gyro()

    # Gyro_Calibrate()
    # lift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)
    # forklift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)
    robot.stop()
    robot.settings(straight_speed=30, straight_acceleration=10, turn_rate=80, turn_acceleration=80)
    # Once you set Distance_control.limits. It will always control the robot speed.
    # robot.distance_control.limits(speed=30, acceleration=5, actuation=100)
    # robot.heading_control.limits(speed=120, acceleration=10000, actuation=100)
    # robot.heading_control.limits()
    # robot.straight(1650)


    # Setting control the Straight speed.
    ## From the LeftLine, (L')No 7Line on the Wheel. (N') The second Thick Block Line
    # gyroDrivePID(0, 1605, 50)


    gyroDrivePID(0, 760, 50)


    ## 1800 is the max degree of put the forklift to the topest up degree
    forklift_motor.run_angle(speed=-125, rotation_angle=1700, then=Stop.HOLD, wait=True)

    #Changed the robot Setting, ** Stop() First *
    robot.stop()
    robot.settings(straight_speed=70, straight_acceleration=10, turn_rate=80, turn_acceleration=80)
    robot.straight(-95)
    turn(45, turnType=2, turnSpeed=56)
    lift_motor.run_angle(speed=-356, rotation_angle=145, then=Stop.HOLD, wait=True)
    
    robot.straight(-35)
    turn(69, turnType=2, turnSpeed=56)
    lift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)
    turn(146, turnType=2, turnSpeed=56)

    t = Thread(target = reset_forklift)
    t.start()
    # Find the first Trip to flip
    robot.straight(97)
    digTrip()

    robot.straight(-5)
    #The second Trip
    turn(123, turnType=2, turnSpeed=56)
    robot.straight(77)
    digTrip()

    #For the Weight Lefting
    turn(79, turnType=2, turnSpeed=56)
    robot.stop()
    robot.settings(straight_speed=70, straight_acceleration=30, turn_rate=80, turn_acceleration=80)
    robot.straight(505)
    print('this is the stop')
    #For Lift up the Weight
    forklift_motor.run_angle(speed=-125, rotation_angle=1700, then=Stop.HOLD, wait=True)


    #For the Phone catch
    turn(145, turnType=2, turnSpeed=56)
    robot.straight(65)
    lift_motor.run_angle(speed=-556, rotation_angle=136, then=Stop.HOLD, wait=True)
    turn(180, turnType=2, turnSpeed=56)

    t1 = Thread(target = reset_forklift)
    t1.start()

    #For the Bridge
    robot.straight(450)
    turn(270, turnType=2, turnSpeed=56)
    robot.straight(150)
    colorChecker(color=Color.WHITE)
    lineFollow(distance=400, l_r_sensor='l', l_r='l', speed=30)
    lift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)


def FindTheCross():
    # colorChecker(color=Color.WHITE)
    # lineFollow(distance=3000, l_r_sensor='l', l_r='l', speed=30)

    #For the first stop in the Linefollow right_sensor detect white
    # robot.straight(75)

    # colorChecker(color=Color.WHITE)
    # lineFollow(distance=3000, l_r_sensor='l', l_r='l', speed=30)
    lineFollow_Stop_on_Cross(distance=3000, l_r_sensor='l', l_r='r', speed=30)



def M11_test():
    # Hit the hellocopt
    # gyro_sensor.reset_angle(90) 
    # lift_motor.run_until_stalled(speed=560, then=Stop.COAST, duty_limit=None) #start
    lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None) #start 
    lift_motor.run_angle(speed=320, rotation_angle=10, then=Stop.HOLD, wait=False)
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None) #start 
    # fork_motor.run_angle(speed=-320, rotation_angle=100, then=Stop.HOLD, wait=False)
    turn_angle(angle=90-90, speed1=60)
    PID_Gyro(angle=90-90, distance=140, speed=-85)

    turn_angle(angle=152-90, speed1=60)
    PID_Gyro(angle=152-90, distance=175, speed=-85)

    wait(200)
    PID_Gyro(angle=152-90, distance=395, speed=85)

    turn_angle(angle=180-90, speed1=60)
    PID_Gyro(angle=180-90, distance=90, speed=85)   

    # turn_angle(angle=202, speed1=60)
    # PID_Gyro(angle=202, distance=60, speed=85)
    wait(200)
    turn_angle(angle=273-90, speed1=60)

    wait(200)
    turn_angle(angle=180-90, speed1=60)
    PID_Gyro(angle=180-90, distance=580, speed=85)


   # Turn 45
    turn_angle(angle=145-90, speed1=50)
    lift_motor.run_angle(speed=-120, rotation_angle=400, then=Stop.HOLD, wait=False)
    PID_Gyro(angle=145-90, distance=250, speed=85)

    turn_angle(angle=183-90, speed1=50)
    PID_Gyro(angle=183-90, distance=700, speed=85)

    # start the next code
    lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start 



    # turn(45, turnType=2, turnSpeed=56)

    # t1 = Thread(target = reset_forklift)
    # t1.start()

    # #For the Bridge
    # robot.straight(455)
    # turn(135, turnType=2, turnSpeed=56)
    # robot.straight(110)
    # colorChecker(color=Color.WHITE)
    # lineFollow(distance=320, l_r_sensor='l', l_r='l', speed=30)


def M11_Faraway_Distance():
    Gyro_Calibrate()
    lift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)
    forklift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)
    robot.stop()
    robot.settings(straight_speed=30, straight_acceleration=50)#, turn_rate=80, turn_acceleration=80)
    # Once you set Distance_control.limits. It will always control the robot speed.
    # robot.distance_control.limits(speed=30, acceleration=5, actuation=100)
    # robot.heading_control.limits(speed=120, acceleration=10000, actuation=100)
    # robot.heading_control.limits()
    # robot.straight(1650)


    # Setting control the Straight speed.
    ## From the LeftLine, (L')No 7Line on the Wheel. (N') The second Thick Block Line
    # gyroDrivePID(0, 1605, 50)


    gyroDrivePID(0, 760, 50)


    ## 1800 is the max degree of put the forklift to the topest up degree
    forklift_motor.run_angle(speed=-125, rotation_angle=1700, then=Stop.HOLD, wait=True)

    #Changed the robot Setting, ** Stop() First *
    robot.stop()
    robot.settings(straight_speed=70, straight_acceleration=10, turn_rate=80, turn_acceleration=80)
    robot.straight(-85)
    turn(45, turnType=2, turnSpeed=56)
    lift_motor.run_angle(speed=-356, rotation_angle=145, then=Stop.HOLD, wait=True)
    
    robot.straight(-35)
    turn(69, turnType=2, turnSpeed=56)
    lift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)
    turn(146, turnType=2, turnSpeed=56)

    t = Thread(target = reset_forklift)
    t.start()
    # Find the first Trip to flip
    robot.straight(97)
    digTrip()

    #The second Trip
    turn(131, turnType=2, turnSpeed=56)
    robot.straight(65)
    digTrip()


    turn(81, turnType=2, turnSpeed=56)
    robot.stop()
    robot.settings(straight_speed=70, straight_acceleration=30, turn_rate=80, turn_acceleration=80)
    robot.straight(576)

    forklift_motor.run_angle(speed=-125, rotation_angle=1700, then=Stop.HOLD, wait=True)






def digTrip():
    lift_motor.run_angle(speed=-556, rotation_angle=136, then=Stop.HOLD, wait=True)
    wait(3)
    robot.stop()
    robot.settings(straight_speed=550, straight_acceleration=550, turn_rate=80, turn_acceleration=80)
    robot.straight(-135)
    lift_motor.run_angle(speed=125, rotation_angle=15, then=Stop.HOLD, wait=True)
    robot.stop()
    robot.settings(straight_speed=70, straight_acceleration=30, turn_rate=80, turn_acceleration=80)
    robot.straight(130)
    lift_motor.run_until_stalled(speed=130, then=Stop.COAST, duty_limit=None)


def reset_forklift():
    forklift_motor.run_angle(speed=125, rotation_angle=1700, then=Stop.HOLD, wait=True)

def M11_old2():
    turn(angle=26, turnType=2, turnSpeed=98)
    gyroDrivePID(angle=26, distance=230, speed=57)
    gyroDrivePID(angle=16, distance=90, speed=57)
    # gyroDrivePID(angle=0, distance=86, speed=57)


    # gyroDrivePID(angle=0, distance=210, speed=57)


    fork_motor.run_until_stalled(speed=-120, then=Stop.HOLD, duty_limit=None)

def M11_from_the_home_aero():
    gyroDrivePID(angle=0, distance=905, speed=85)
    print('L442:degree:{0},  this journey distance:{1}'.format(gyro_sensor.angle(), robot.distance()))
    turn(angle=35, turnType=2, turnSpeed=78)
    print('L444:degree:{0},  this journey distance:{1}'.format(gyro_sensor.angle(), robot.distance()))
    # gyroDrivePID(angle=19, distance=25, speed=57)
    # turn(angle=21, turnType=2, turnSpeed=78)
    gyroDrivePID(angle=34, distance=255, speed=80)
    
    print('L449:degree:{0},  this journey distance:{1}'.format(gyro_sensor.angle(), robot.distance()))
    turn(angle=3, turnType=2, turnSpeed=78)
    gyroDrivePID(angle=0, distance=9, speed=80) 
    print('L452:degree:{0},  this journey distance:{1}'.format(gyro_sensor.angle(), robot.distance()))

    fork_motor.run_until_stalled(speed=-120, then=Stop.HOLD, duty_limit=None)  

def M13_20210916(): #platooning track
    #in function
    turn(angle=-11, turnType=2, turnSpeed=86)
    wait(20)
    
    gyroDrivePID(angle=-11, distance=426, speed=85)#55

    turn(angle=-2, turnType=2, turnSpeed=56)# angle=-3
    wait(1000)

    gyroDrivePID(angle=-2, distance=152, speed=85)#115
    left_motor.stop()
    right_motor.stop()
    wait(1000)

    robot.stop()
    lift_motor.run_angle(speed=-300, rotation_angle=435, then=Stop.HOLD, wait=True)
    # wait(1000)

    turn(angle=-4, turnType=2, turnSpeed=56)# angle=-3

    gyroDrivePID(angle=-4, distance=105, speed=65)
    # wait(200)

    # turn(angle=-3, turnType=2, turnSpeed=36)# angle=-3

    # gyroDrivePID(angle=-3, distance=40, speed=65)
    # wait(200)


    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    turn(angle=5, turnType=2, turnSpeed=66)
    wait(1000)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    gyroDrivePID(angle=5, distance=76, speed=66)
    # wait(300)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)
    # turn(angle=0, turnType=2, turnSpeed=235)

    lift_motor.run_angle(speed=250, rotation_angle=435, then=Stop.HOLD, wait=False)
    # lift_motor.run_angle(speed=250, rotation_angle=419, then=Stop.HOLD, wait=False)
   
    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    # turn(angle=5, turnType=2, turnSpeed=66)
    # wait(200)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    gyroDrivePID(angle=5, distance=105, speed=65)
    # wait(200)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    turn(angle=0, turnType=2, turnSpeed=66)
    # wait(200)

    
    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)    

    gyroDrivePID(angle=0, distance=80, speed=65)
    wait(200)

    # turn(angle=0, turnType=2, turnSpeed=56)
    # wait(200)

    lift_motor.run_angle(speed=-250, rotation_angle=150, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=-250, rotation_angle=120, then=Stop.HOLD, wait=True)
    
    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)   

    gyroDrivePID(angle=0, distance=103, speed=95)
    wait(200)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)


    lift_motor.run_angle(speed=250, rotation_angle=150, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=250, rotation_angle=120, then=Stop.HOLD, wait=True)
    

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    gyroDrivePID(angle=0, distance=85, speed=-95)
    wait(200)
    # button()

def Test(): #test the code
    turn_angle(angle=-13, speed1=65)
    wait(2000)
    turn_angle(angle=0, speed1=65)
    left_motor.hold()
    right_motor.hold()    
    button()

def M13(): #platooning truck
    # Turning -12 degree sharply then go straight
    turn_angle(angle=-14, speed1=65)
    PID_Gyro(angle=-14, distance=438, speed=65) #441 13
    # turn_angle(angle=-13, speed1=65)
    # PID_Gyro(angle=-13, distance=323, speed=65)
    # wait(1000)
    wait(200)
    # button()
    # turn(0, turnType=2, turnSpeed=360)
    turn_angle(angle=0,speed1=85)
    left_motor.hold()
    right_motor.hold()
    # button()
    # wait(500)
    # button()
    PID_Gyro(angle=0, distance=134, speed=65) #150 70 60 138+17

    # button()
    #Keeping going forward to connect the second hook
    # gyroDrivePID(angle=-2, distance=158, speed=85)#115
    left_motor.stop()
    right_motor.stop()
    wait(650)
    # wait(100)
    # wait(1500) #formal wait
    # button()
    #Because it will strickly hold continue, so I need turn some contrary dirction to loose the continner 
    # turn_angle(angle=-7, speed=95)
    lift_motor.run_angle(speed=200, rotation_angle=400, then=Stop.HOLD, wait=True) #formal 0, after 400
    left_motor.stop()
    right_motor.stop()
    # button()
    wait(650)
    turn_angle(angle=0,speed1=67)
    PID_Gyro(angle=0, distance=151, speed=75)

    left_motor.hold()
    right_motor.hold()

    # button()
    turn_angle(angle=5, speed1=45)
    PID_Gyro(angle=5, distance=251, speed=75)

    # button()

    # lift_motor.run_angle(speed=250, rotation_angle=205, then=Stop.HOLD, wait=True)
    # # button()
    turn_angle(angle=0,speed1=57)
    
    left_motor.hold()
    right_motor.hold()
    
    PID_Gyro(angle=0, distance=25+17, speed=75) #65

    left_motor.hold()
    right_motor.hold()

    lift_motor.run_angle(speed=-650, rotation_angle=205, then=Stop.HOLD, wait=True) # formal 400-205, after 195
    
    # button()
    turn_angle(angle=0,speed1=57)
    PID_Gyro(angle=0, distance=95, speed=-75)

    # button()
    # # turn_angle(angle=-7, speed=95)
    # # PID_Gyro(angle=-7, distance=50, speed=75)

    # # gyroDrivePID(angle=-7, distance=50, speed=85)
    # # lift_motor.run_angle(speed=250, rotation_angle=435, then=Stop.HOLD, wait=False)

    # turn_angle(angle=3, speed=95)
    # PID_Gyro(angle=3, distance=300, speed=80)

    # lift_motor.run_angle(speed=250, rotation_angle=165, then=Stop.HOLD, wait=True)

    # turn_angle(angle=0, speed=95)
    # PID_Gyro(angle=0, distance=215, speed=75)

    # lift_motor.run_angle(speed=-250, rotation_angle=155, then=Stop.HOLD, wait=True)
  
    # turn_angle(angle=0, speed=95)
    # PID_Gyro(angle=0, distance=85, speed=-75)
    # button()

def M11(): # Package delivery
    #The mission M11 delivery parcage
    left_motor.stop()
    right_motor.stop()
    # Turn_on_position(degree=12, t_rate=35)
    # ev3.speaker.beep()
    # button()
    lift_motor.run_angle(speed=520, rotation_angle=605, then=Stop.HOLD, wait=False) # formal 195+605, after 800

    #replace the PIDline function
    # Go_Straight_line(speed=55,dist=323)
    # button()
    turn_angle(angle=19, speed1=45)
    PID_Gyro(angle=19, distance=299, speed=85) #295

    # button()
    ## This is the sentenses to make the yellow package to slip off the robot
    # lift_motor.run_until_stalled(speed=260, then=Stop.COAST, duty_limit=None)
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)
    turn_angle(angle=23, speed1=45)
    lift_motor.run_angle(speed=-635, rotation_angle=300, then=Stop.HOLD, wait=True) # formal 800, after 700
    fork_motor.run_angle(speed=-535, rotation_angle=100, then=Stop.HOLD, wait=False) # formal 0+100, after 100 False
    lift_motor.run_angle(speed=-655, rotation_angle=400, then=Stop.HOLD, wait=True)# formal 700-700, after 0
    # lift_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True)# formal 500, after 300
    # ev3.speaker.beep()
    wait(580)
    # turn_angle(angle=19, speed1=45)
    # button()
    # wait(20)
    # Go_Straight_line(dist=310, speed=55)
    # turn(angle=29, turnType=2, turnSpeed=56)

    # turn(angle=19, turnType=2, turnSpeed=78)
    # wait(20)
    # Go_Straight_line(dist=25, speed=55)
    # turn(angle=19, turnType=2, turnSpeed=78)

    # turn(angle=8, turnType=2, turnSpeed=78)
    # wait(20)
    # Go_Straight_line(dist=15, speed=55)
    # turn(angle=8, turnType=2, turnSpeed=78)

    # ## This is the sentenses to make the yellow package to slip off the robot
    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None)
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)
    # lift_motor.run_angle(speed=620, rotation_angle=400, then=Stop.HOLD, wait=False)
    # fork_motor.run_angle(speed=-620, rotation_angle=100, then=Stop.HOLD, wait=True) 
    # ev3.speaker.beep()


    # fork_motor.stop()
    # fork_motor.run_angle(speed=-120, rotation_angle=200, then=Stop.HOLD, wait=True)
    # wait(200)
    # # button()


def M12(): #Large Delievery
    left_motor.stop()
    right_motor.stop()
    # gyro_sensor.reset_angle(21)
    # button()
    lift_motor.run_angle(speed=260, rotation_angle=700, then=Stop.HOLD, wait=False) # formal 0, after 800

    print('678, Gyro_sensor.degree = {0}'.format(gyro_sensor.angle()))
    # button()
    turn_angle(angle=19, speed1=45) #85
    PID_Gyro(angle=19, distance=156-15, speed=-85) #168
    # ev3.speaker.beep()

    # button()
    turn_angle(angle=-61, speed1=55) #65
    PID_Gyro(angle=-61, distance=116+7, speed=-85) #113

    # lift_motor.run_angle(speed=250, rotation_angle=500, then=Stop.HOLD, wait=True)
    # PID_Gyro(angle=0, distance=150, speed=-85)

    # button()
    turn_angle(angle=0, speed1=55)
    wait(20)
    PID_Gyro(angle=0, distance=15, speed=-85) #17
    # resetGyro()
    # turn(angle=6, turnType=2, turnSpeed=78)
    # wait(200)
    # Go_Straight_line(dist=-65, speed=65)
    # turn(angle=6, turnType=2, turnSpeed=78)

    # # gyroDrivePID(angle=3, distance=75, speed=-80) 
    # fork_motor.stop()
    # fork_motor.run_angle(speed=120, rotation_angle=500, then=Stop.HOLD, wait=False)

    # turn(angle=25, turnType=2, turnSpeed=78)
    # Go_Straight_line(dist=-35, speed=65)
    # turn(angle=25, turnType=2, turnSpeed=78)
    # # gyroDrivePID(angle=23, distance=110, speed=-80)
    # lift_motor.run_angle(speed=-250, rotation_angle=590, then=Stop.HOLD, wait=False)

    # turn(angle=0, turnType=2, turnSpeed=78)
    # Go_Straight_line(dist=-180, speed=65)
    # turn(angle=0, turnType=2, turnSpeed=78)

    # # gyroDrivePID(angle=0, distance=180, speed=-80)

    # lift_motor.stop()
    # fork_motor.stop()
    # button()
    lift_motor.run_angle(speed=-560, rotation_angle=400, then=Stop.HOLD, wait=True) # formal 800, after 400
    print('658')
    fork_motor.run_angle(speed=-650, rotation_angle=400, then=Stop.HOLD, wait=True)# formal 100 +400, after 500
    print('660')
    wait(1000)
    

    # turn(angle=0, turnType=2, turnSpeed=78)
    # Go_Straight_line(dist=55, speed=65)
    # turn(angle=0, turnType=2, turnSpeed=78)

    # turn(angle=23, turnType=2, turnSpeed=78)
    # Go_Straight_line(dist=-260, speed=65)
    # turn(angle=23, turnType=2, turnSpeed=78)

    # turn(angle=0, turnType=2, turnSpeed=78)
    # Go_Straight_line(dist=-750, speed=65)
    # turn(angle=0, turnType=2, turnSpeed=78)



    # button()

def M05(): #Switch Engine

    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start 
    
    
    #stage1: Lift the motor to across the unused continet
    turn_angle(angle=0, speed1=65) #65

    lift_motor.run_angle(speed=260, rotation_angle=200, then=Stop.HOLD, wait=False) #initial 0+200, after 200
    fork_motor.run_angle(speed=-320, rotation_angle=100, then=Stop.HOLD, wait=False) #initial 0+100, after 100
    # lift_motor.run_angle(speed=260, rotation_angle=345, then=Stop.HOLD, wait=False) #initial 0+345, after 345
    # fork_motor.run_angle(speed=-320, rotation_angle=30, then=Stop.HOLD, wait=False) #initial 0, after 30

    # to come close the cargo airplane tail
    PID_Gyro(angle=0, distance=634, speed=45) #210 , 624,639

    # open the crab for some degree
    # lift_motor.run_angle(speed=-260, rotation_angle=145, then=Stop.HOLD, wait=False) #initial 345-145, after 200
    # fork_motor.run_angle(speed=-320, rotation_angle=70, then=Stop.HOLD, wait=False) #formal 30 + 70, after 100

    # tuning to close the switch
    turn_angle(angle=44, speed1=56) #65
    PID_Gyro(angle=44, distance=172, speed=85) #210
    wait(200)

    # lift_up the switch engine
    fork_motor.run_until_stalled(speed=220, then=Stop.HOLD, duty_limit=None) #formal 100 --, after 0


    # low up  the fork and lift
    # lift_motor.run_angle(speed=-260, rotation_angle=200, then=Stop.HOLD, wait=True) #formal 200-200, after 0

    turn_angle(angle=44, speed1=56) #65
    # PID_Gyro(angle=44, distance=15, speed=85) #126 206
    # wait(500)
    PID_Gyro(angle=44, distance=40, speed=-85) #126 206


    # lift up the motor to put down
    # lift_motor.run_until_stalled(speed=660, then=Stop.COAST, duty_limit=None)# formal 0+820, after 820
    lift_motor.run_angle(speed=660, rotation_angle=620, then=Stop.HOLD, wait=False) #formal 200+620, after 820


    # Stage3 : turning and kick off the Cargo airplane
    # go back again to prepare turning 
    turn_angle(angle=-4, speed1=65) #65
    PID_Gyro(angle=-4, distance=160, speed=-75) #126 206  165
    wait(500)
    turn_angle(angle=-42, speed1=65) #65

    # go forward for a moment
    PID_Gyro(angle=-42, distance=30, speed=85) #126 206      
    turn_angle(angle=-38, speed1=65) #65

    # PID_Gyro(angle=-38, distance=150, speed=-85) #126 206  165

    # put down for catch the container
    lift_motor.run_until_stalled(speed=-860, then=Stop.COAST, duty_limit=None) #formal 820--, after 0
    fork_motor.run_angle(speed=-860, rotation_angle=110, then=Stop.HOLD, wait=True) #formal 0+110, after 110

    wait(300)
    # go back word for a moment
    turn_angle(angle=-42, speed1=65) #65
    PID_Gyro(angle=-42, distance=80, speed=-85) #126 206
    

    # lift up and open up the fork
    lift_motor.run_angle(speed=600, rotation_angle=820, then=Stop.HOLD, wait=False)# formal 0+820, after 820
    fork_motor.run_angle(speed=-600, rotation_angle=400, then=Stop.HOLD, wait=True) #formal 110+400, after 510

    PID_Gyro(angle=-39, distance=40, speed=85) #126 206 42    
    turn_angle(angle=-12, speed1=75) #65    
    # PID_Gyro(angle=-12, distance=10, speed=-85) #126 206 42    
    # wait(200)
    # go down the lift
    lift_motor.run_angle(speed=-680, rotation_angle=750, then=Stop.HOLD, wait=True)#formal 820-750, after 70 #420
    turn_angle(angle=-47, speed1=45) #65 -43
    PID_Gyro(angle=-47, distance=20, speed=-85) #126 206 42    
    lift_motor.run_angle(speed=680, rotation_angle=700, then=Stop.HOLD, wait=True)#formal 70+700, after 770 #420


    #go out of the mat
    turn_angle(angle=-105, speed1=75) #65    
    lift_motor.run_angle(speed=-680, rotation_angle=700, then=Stop.HOLD, wait=True)#formal 770-700, after 70 #420
    PID_Gyro(angle=-105, distance=450, speed=85) #126 206

def M02(): #Innoviaton_projector
    # Turn the orangle light to mean this stage start

    # First turn some degree to make the robot through the tunner.
    turn_angle(angle=-34, speed1=95) #65  
    PID_Gyro(angle=-34, distance=785, speed=85) #126 206 42  

    # Turn some degree to the right position 0
    turn_angle(angle=0, speed1=65) #65  
    PID_Gyro(angle=0, distance=485, speed=85) #126 206 42  

    # Trun some degree to delieve the innovation project
    turn_angle(angle=56, speed1=95) #65  
    PID_Gyro(angle=56, distance=100, speed=85)  

    # Go back some degree
    turn_angle(angle=44, speed1=65) #65  
    PID_Gyro(angle=44, distance=157, speed=-85)  

    # Turn some degree to the circle
    turn_angle(angle=0, speed1=65) #65  
    PID_Gyro(angle=0, distance=243, speed=85) #126 206 42  

    # Laydown the contioneor
    fork_motor.run_angle(speed=-320, rotation_angle=100, then=Stop.HOLD, wait=True) #initial 0, after 100

    # go back to hit the wall
    turn_angle(angle=26, speed1=65) #65  
    PID_Gyro(angle=26, distance=617, speed=-85) 


    # Lift up the fork
    fork_motor.run_angle(speed=320, rotation_angle=100, then=Stop.HOLD, wait=False) #formal 100 - 100, after 0

    # go back to hit the wall
    turn_angle(angle=0, speed1=65) #65  
    PID_Gyro(angle=0, distance=45, speed=-85) 

    # go to the wall
    turn_angle(angle=35, speed1=65) #65  
    PID_Gyro(angle=35, distance=185, speed=85)    

    #hit the crane
    turn_angle(angle=0, speed1=65) #65  
    PID_Gyro(angle=0, distance=545, speed=85) 


#     degree:37,  this journey distance:-14
#     degree:34,  this journey distance:653
# degree:2,  this journey distance:33
# Turn_Finished,Gyro_sensor.angle=0, Robot_distance=2



def M05_20211016():#_1016: #Switch Engine
    #stage1: Lift the motor to across the unused continet
    ev3.light.on(Color.RED)
    lift_motor.run_angle(speed=260, rotation_angle=345, then=Stop.HOLD, wait=False) #initial 0, after 445
    fork_motor.run_angle(speed=-320, rotation_angle=30, then=Stop.HOLD, wait=False) #initial 0, after 30

    # to come close the cargo airplane tail
    turn_angle(angle=0, speed1=65) #65
    PID_Gyro(angle=0, distance=642, speed=45) #210 , 624,639

    # open the crab for some degree
    lift_motor.run_angle(speed=-260, rotation_angle=145, then=Stop.HOLD, wait=False) #initial 445, after 300
    fork_motor.run_angle(speed=-320, rotation_angle=70, then=Stop.HOLD, wait=False) #formal 80, after 100

    # tuning to close the switch
    turn_angle(angle=44, speed1=56) #65
    PID_Gyro(angle=44, distance=165, speed=85) #210
    wait(200)

    # lift_up the switch engine
    fork_motor.run_until_stalled(speed=220, then=Stop.HOLD, duty_limit=None) #formal 100, after 0


    # low down  the fork and lift
    lift_motor.run_angle(speed=-260, rotation_angle=300, then=Stop.HOLD, wait=False) #formal 300, after 0

    turn_angle(angle=44, speed1=56) #65
    PID_Gyro(angle=44, distance=185, speed=-85) #126 206


    # lift up the motor to put down
    lift_motor.run_until_stalled(speed=660, then=Stop.COAST, duty_limit=None)#formal 0, after 820


    # Stage3 : turning and kick off the Cargo airplane
    # go back again to prepare turning 
    turn_angle(angle=19, speed1=75) #65

    button()

    # put down for catch the container
    lift_motor.run_until_stalled(speed=-660, then=Stop.COAST, duty_limit=None) #formal 820, after 0
    fork_motor.run_angle(speed=-660, rotation_angle=500, then=Stop.HOLD, wait=True) #formal 0, after 500

    turn_angle(angle=27, speed1=75) #65    
    fork_motor.run_angle(speed=380, rotation_angle=400, then=Stop.HOLD, wait=False)#formal 500, after 100 #420
    

    turn_angle(angle=13, speed1=75) #65    
    #Stage4: After make the continer down, We should make it to center
    # lift up and close the crab
    # lift_motor.run_angle(speed=260, rotation_angle=200, then=Stop.HOLD, wait=True) #formal 0, after 200

    # button()

    # hold on the continner
    turn_angle(angle=15, speed1=55) #65
    lift_motor.run_angle(speed=-260, rotation_angle=200, then=Stop.HOLD, wait=False)#formal 200, after 0

    PID_Gyro(angle=15, distance=120, speed=-85) #210


    turn_angle(angle=0, speed1=65) #65
    PID_Gyro(angle=0, distance=8, speed=-85) #210
    wait(200)
    # make the cargo plane yellow bar contact the black frame
    # turn_angle(angle=-15, speed1=65) #65
    fork_motor.run_angle(speed=-380, rotation_angle=220, then=Stop.HOLD, wait=False)#formal 80, after 280
    turn_angle(angle=0, speed1=65) #65
    PID_Gyro(angle=0, distance=450, speed=-85) #210


def M05_new0919(): #Switch Engine
    #stage1: Lift the motor to across the unused continent
    lift_motor.run_angle(speed=-260, rotation_angle=605, then=Stop.HOLD, wait=False)

    # open the crab for some degree
    fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=False)

    # to come close the cargo airplane tail
    turn(angle=0, turnType=2, turnSpeed=78)
    wait(20)
    Go_Straight_line(dist=644, speed=62)
    turn(angle=0, turnType=2, turnSpeed=78)

    # gyroDrivePID(angle=0, distance=644, speed=80)

    lift_motor.run_angle(speed=260, rotation_angle=605, then=Stop.HOLD, wait=False)

    # turning to close the switch
    turn(angle=44, turnType=2, turnSpeed=63)
    wait(500)
    # gyroDrivePID(angle=44, distance=145, speed=45)
    # turn(angle=44, turnType=2, turnSpeed=65)
    Go_Straight_line(dist=145, speed=62)
    turn(angle=44, turnType=2, turnSpeed=78)

    # lift_up the switch engine
    fork_motor.run_angle(speed=320, rotation_angle=90, then=Stop.HOLD, wait=True)

    # Stage2: go back put the contenen in the center of circle
    turn(angle=44, turnType=2, turnSpeed=62)
    wait(20)
    # gyroDrivePID(angle=44, distance=75, speed=-58)
    Go_Straight_line(dist=-75, speed=58)
    turn(angle=44, turnType=2, turnSpeed=78)

    #move to the center of circle
    turn(angle=37, turnType=2, turnSpeed=78)
    wait(200)

    # open the fork
    fork_motor.run_angle(speed=-170, rotation_angle=300, then=Stop.HOLD, wait=True)

    # close the fork one little, because it's too faraway from the center
    # fork_motor.run_angle(speed=170, rotation_angle=100, then=Stop.HOLD, wait=True)
    
    # lift up the motor to put down
    lift_motor.run_until_stalled(speed=-660, then=Stop.COAST, duty_limit=None)

    # The close the crab again to lift up
    fork_motor.run_angle(speed=120, rotation_angle=300, then=Stop.HOLD, wait=False)

    # Stage3 : turning and kick off the Cargo airplane
    # go back again to prepare tuning 
    turn(angle=37, turnType=2, turnSpeed=78)
    # gyroDrivePID(angle=37, distance=144, speed=-60)
    

    # then turing some degree of put down the cargo plane
    turn(angle=14, turnType=2, turnSpeed=78)


    # put down for catch the container
    lift_motor.run_until_stalled(speed=260, then=Stop.COAST, duty_limit=None)
    wait(300)
    # put down the lift motor 
    fork_motor.run_until_stalled(speed=-950, then=Stop.HOLD, duty_limit=None)

    #Stage4: After make the continer down, We should make it to center
    # lift up and close the crab
    lift_motor.run_angle(speed=-260, rotation_angle=70, then=Stop.HOLD, wait=True)

    # print('666')
    # button()
    # hold on the continner
    turn(angle=14, turnType=2, turnSpeed=78)
    Go_Straight_line(dist=33, speed=80)
    turn(angle=14, turnType=2, turnSpeed=78)

    # gyroDrivePID(angle=14, distance=33, speed=80)

    # button()
    #close the fork and hold on 
    fork_motor.run_angle(speed=220, rotation_angle=550, then=Stop.HOLD, wait=True)
    #turn some degree to make sure the continer in the center of circle
    turn(angle=14, turnType=2, turnSpeed=78)
    # gyroDrivePID(angle=14, distance=88, speed=-80)
    Go_Straight_line(dist=-88, speed=75)
    turn(angle=14, turnType=2, turnSpeed=78)

    turn(angle=5, turnType=2, turnSpeed=78)
    # print('678')
    # button()


    #open the crab and lift up
    fork_motor.run_angle(speed=-320, rotation_angle=350, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=-260, rotation_angle=400, then=Stop.HOLD, wait=False)


    turn(angle=5, turnType=2, turnSpeed=78)
    wait(20)
    Go_Straight_line(dist=-560, speed=80)
    turn(angle=5, turnType=2, turnSpeed=78)


    # gyroDrivePID(angle=5, distance=560, speed=-80)

    # print('690')
    # button()
    # # open the fork to hit the yellow pod

    # # button()
    # # make the fork to hold the continer. First make the lift up a few degree

    # # close the fork to hug the continer
    # # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)

    # # then turn some degree to make the cointrner in the center of circle and go backword
    # turn(angle=14, turnType=2, turnSpeed=78)
    # gyroDrivePID(angle=14, distance=80, speed=-80)

    # # lift up the motor for some degree, because we hit the black frame
    # # lift_motor.run_angle(speed=260, rotation_angle=300, then=Stop.HOLD, wait=False)

    # #open the fork
    # turn(angle=10, turnType=2, turnSpeed=78)
    # fork_motor.run_angle(speed=-320, rotation_angle=350, then=Stop.HOLD, wait=True)
    # # ev3.speaker.beep()

    # # Cause: close to the little plane.

    # # First we go back for some distance
    # turn(angle=10, turnType=2, turnSpeed=78)
    # gyroDrivePID(angle=10, distance=80, speed=-80)


    # # Then we close the fork and lift up .
    # lift_motor.run_angle(speed=-260, rotation_angle=500, then=Stop.HOLD, wait=False)
    # fork_motor.run_angle(speed=320, rotation_angle=350, then=Stop.HOLD, wait=False)

    # # We close to the little plance
    # turn(angle=44, turnType=2, turnSpeed=78)
    # gyroDrivePID(angle=44, distance=150, speed=-80)
    # turn(angle=35, turnType=2, turnSpeed=78)

    # # Put down the lift
    # lift_motor.run_angle(speed=260, rotation_angle=500, then=Stop.HOLD, wait=False)
    # fork_motor.run_angle(speed=320, rotation_angle=200, then=Stop.HOLD, wait=True)

    # turn(angle=-8, turnType=1, turnSpeed=56)


    # button()
    # # put up the lift motor first for the continent height
    # lift_motor.run_angle(speed=-260, rotation_angle=400, then=Stop.HOLD, wait=False)

    # # Then close the fork motor to collect the continnet
    # fork_motor.run_angle(speed=220, rotation_angle=500, then=Stop.HOLD, wait=False)

    # # put up the lift motor first for the continent height
    # lift_motor.run_angle(speed=260, rotation_angle=600, then=Stop.HOLD, wait=False)

  

    # # # go forward for collect the continent
    # gyroDrivePID(angle=44, distance=250, speed=-80)


    # # put up the lift motor first for the continent height
    # lift_motor.run_angle(speed=-260, rotation_angle=300, then=Stop.HOLD, wait=True)

    # # At the same time tuning some degress
    # turn(angle=35, turnType=2, turnSpeed=56)
    
    # # Cointinue to go back push the bule continent out of the mat
    # gyroDrivePID(angle=35, distance=236, speed=-80)




    
    
    
    # pass

def M10(Position_Blue=1, Position_Green=2): #M10_Sorting Center
    lift_motor.run_angle(speed=260, rotation_angle=400, then=Stop.HOLD, wait=False) #formal 400+400, after 800

    fork_motor.run_angle(speed=250, rotation_angle=500, then=Stop.HOLD, wait=False) # formal 500-500, after 0

    turn_angle(angle=-20, speed1=50)
    PID_Gyro(angle=-20, distance=120, speed=85)

    turn_angle(angle=-53, speed1=50)
    PID_Gyro(angle=-53, distance=590-27, speed=85) #35

    turn_angle(angle=0, speed1=50)
    PID_Gyro(angle=0, distance=26+23, speed=85)  # 38Distance decide the position of continen

    lift_motor.run_angle(speed=-260, rotation_angle=800, then=Stop.HOLD, wait=False) #formal 800, after 0
    # fork_motor.run_angle(speed=250, rotation_angle=120, then=Stop.HOLD, wait=False) #formal 120, after 0

    turn_angle(angle=90, speed1=50)

    # button()
    # resetGyro()
    # placing the blue container on the bottom shelf in any of the three bays



    ############################################ Grab the conainer
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start position #formal 0, after 0
    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start position #formal 800, after 0
    fork_motor.run_until_stalled(speed=320, then=Stop.HOLD, duty_limit=None)#start position #formal 0, after 0
    lift_motor.run_until_stalled(speed=-360, then=Stop.COAST, duty_limit=None) #start position #formal 800, after 0
    # fork_motor.run_angle(speed=-120, rotation_angle=91, then=Stop.HOLD, wait=False)
    fork_motor.run_angle(speed=-320, rotation_angle=90, then=Stop.HOLD, wait=False) #formal 0, after 90
    lift_motor.run_angle(speed=320, rotation_angle=483, then=Stop.HOLD, wait=True) #483 formal 0, after 483
    # lift_motor.run_angle(speed=120, rotation_angle=350, then=Stop.HOLD, wait=True) #wait=True
    ############################################
    if(Position_Blue==3):
        degree_blue = 77
    
    if(Position_Blue==2):
        degree_blue = 90
        
    if(Position_Blue==1):
        degree_blue = 103

    # Location=2
    # turn_angle(angle=0, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=85)

    #Location=1
    # turn_angle(angle=13, speed1=50)
    # PID_Gyro(angle=13, distance=200, speed=85)

    #Location=3
    turn_angle(angle=degree_blue, speed1=50)
    PID_Gyro(angle=degree_blue, distance=170, speed=85)

    #Hold up the continer
    fork_motor.run_until_stalled(speed=520, then=Stop.HOLD, duty_limit=None)

    ###### Go back to the first point
    # Location=2
    # turn_angle(angle=0, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=-85)
    
    #Location=1
    # turn_angle(angle=13, speed1=50)
    # PID_Gyro(angle=13, distance=200, speed=-85)

    #Location=3
    turn_angle(angle=degree_blue, speed1=50)
    PID_Gyro(angle=degree_blue, distance=160, speed=-85)


    #turn 180 degree, And go to the blue circle 
    turn_angle(angle=176+90, speed1=75) #174 179
    PID_Gyro(angle=176+90, distance=77, speed=85)

    ############################################ Put down the conainer
    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #Go down lift position
    # fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True) #put down the Grab wait=True
    lift_motor.run_until_stalled(speed=-360, then=Stop.COAST, duty_limit=None) #Go down lift position 0
    fork_motor.run_angle(speed=-320, rotation_angle=100, then=Stop.HOLD, wait=True) #put down the Grab wait=True
    ############################################

    # Go back to the first point 
    turn_angle(angle=176+90, speed1=75)
    PID_Gyro(angle=176+90, distance=77, speed=-85)

    # Hold up the grab, because it will hit the shipmission
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)

    turn_angle(angle=0+90, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=-85)

    ### the Second grab the Green continer
    ##########################################################
    fork_motor.run_angle(speed=-620, rotation_angle=91, then=Stop.HOLD, wait=False) #92
    lift_motor.run_angle(speed=320, rotation_angle=365+10, then=Stop.HOLD, wait=True) # formal 0, after 365
    # fork_motor.run_angle(speed=-120, rotation_angle=91, then=Stop.HOLD, wait=False) #92
    # lift_motor.run_angle(speed=120, rotation_angle=365, then=Stop.HOLD, wait=True) # wait=True 360

    if(Position_Green==1):
        degree_green = 13+90

    if(Position_Green==2):
        degree_green = 0+90

    if(Position_Green==3):
        degree_green = -13+90

    # Location=2
    turn_angle(angle=degree_green, speed1=50)
    PID_Gyro(angle=degree_green, distance=89, speed=85) #87
    #Hold up the continer
    fork_motor.run_until_stalled(speed=620, then=Stop.HOLD, duty_limit=None)
        
    # Location=2 go back
    turn_angle(angle=degree_green, speed1=50)
    PID_Gyro(angle=degree_green, distance=89+30, speed=-85)

# Hit the hellocopt
    # gyro_sensor.reset_angle(90) 
    # lift_motor.run_until_stalled(speed=560, then=Stop.COAST, duty_limit=None) #start
    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None) #start 
    lift_motor.run_angle(speed=-120, rotation_angle=355, then=Stop.HOLD, wait=False)  # Formal 365 -355 after 10
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None) #start 
    # fork_motor.run_angle(speed=-320, rotation_angle=100, then=Stop.HOLD, wait=False)
    turn_angle(angle=90, speed1=60)
    PID_Gyro(angle=90, distance=140, speed=-85)

    turn_angle(angle=152, speed1=60)
    PID_Gyro(angle=152, distance=174, speed=-85)

    wait(200)
    PID_Gyro(angle=152, distance=415, speed=85)

    turn_angle(angle=180, speed1=60)
    PID_Gyro(angle=180, distance=90, speed=85)   

    turn_angle(angle=230, speed1=60)
    PID_Gyro(angle=230, distance=53, speed=-85)  #53

    # turn_angle(angle=202, speed1=60)
    # PID_Gyro(angle=202, distance=60, speed=85)
    wait(200)
    # Hit and push the crane
    turn_angle(angle=279, speed1=160)

    wait(200)
    #  Go back to the straight

    # To hit the stop board
    turn_angle(angle=209, speed1=60)
    lift_motor.run_angle(speed=120, rotation_angle=200, then=Stop.HOLD, wait=False) #Formal 10 +200 after 210
    PID_Gyro(angle=209, distance=389, speed=85)   #409  

    # Hit the yellow wall
    wait(200)

    turn_angle(angle=207, speed1=60)
    wait(200)
    turn_angle(angle=209, speed1=60)
    PID_Gyro(angle=209, distance=200, speed=-85)

    # Go back to the home aero
    turn_angle(angle=158, speed1=50)
    PID_Gyro(angle=158, distance=770, speed=85)

#     button()


#     # Up the lift becasue will hit the little plane
#     # lift_motor.run_angle(speed=120, rotation_angle=700, then=Stop.HOLD, wait=False) #Formal 10  after 710

#     PID_Gyro(angle=180, distance=550, speed=85)


#    # Turn 45
#     turn_angle(angle=145, speed1=50)
#     lift_motor.run_angle(speed=-120, rotation_angle=700, then=Stop.HOLD, wait=False) #Formal 710 -700 after 10
#     PID_Gyro(angle=145, distance=250, speed=85)

    turn_angle(angle=193, speed1=50)
    PID_Gyro(angle=193, distance=600, speed=85)

    # start the next code
    lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start 


    # button()

    # #################

    # # Hit the hellocopt
    # turn_angle(angle=90, speed1=60)
    # PID_Gyro(angle=90, distance=120, speed=-85)

    # turn_angle(angle=152, speed1=60)
    # PID_Gyro(angle=152, distance=175, speed=-85)

    # wait(200)
    # PID_Gyro(angle=152, distance=340, speed=85)

    # turn_angle(angle=180, speed1=60)
    # PID_Gyro(angle=180, distance=65, speed=85)   

    # # turn_angle(angle=202, speed1=60)
    # # PID_Gyro(angle=202, distance=60, speed=85)
    # wait(200)
    # turn_angle(angle=252, speed1=60)

    # wait(200)
    # turn_angle(angle=180, speed1=60)
    # PID_Gyro(angle=180, distance=700, speed=85)




    # # Turn 90
    # turn_angle(angle=180, speed1=50)
    # lift_motor.run_angle(speed=120, rotation_angle=400, then=Stop.HOLD, wait=False)
    # PID_Gyro(angle=180, distance=980-15, speed=85)

    # Turn 45
    # turn_angle(angle=145, speed1=50)
    # lift_motor.run_angle(speed=-120, rotation_angle=400, then=Stop.HOLD, wait=False)
    # PID_Gyro(angle=145, distance=97, speed=85)

    # turn_angle(angle=183, speed1=50)
    # PID_Gyro(angle=183, distance=700, speed=85)

    # # start the next code
    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start 
    # button()

    # wait(100000)

    # lift_motor.run_angle(speed=260, rotation_angle=400, then=Stop.HOLD, wait=False) #formal 400, after 800

    # fork_motor.run_angle(speed=250, rotation_angle=280, then=Stop.HOLD, wait=False) # formal 380, after 100

    # turn_angle(angle=-20, speed1=50)
    # PID_Gyro(angle=-20, distance=100, speed=85)

    # turn_angle(angle=-55, speed1=50)
    # PID_Gyro(angle=-55, distance=500, speed=85)


    # Distance=210, Position=3
    # Distance=120, Position=2
    # Distance=20, Position=1

    # wait(200)
    # turn_angle(angle=0, speed1=50)
    # if Position_Blue==1:
    #     Distance1=18
    # elif Position_Blue==2:
    #     Distance1=120
    # elif Position_Blue==3:
    #     Distance1=200
    
    # PID_Gyro(angle=0, distance=Distance1, speed=85)  # Distance decide the position of continen


    # wait(200)
    # turn_angle(angle=90, speed1=50)

    # lift_motor.run_angle(speed=-260, rotation_angle=600, then=Stop.HOLD, wait=True) #formal 800, after 100
    # PID_Gyro(angle=90, distance=111, speed=85)

    
    # button()
    # fork_motor.run_angle(speed=620, rotation_angle=230, then=Stop.HOLD, wait=False) 
    # lift_motor.run_angle(speed=-620, rotation_angle=800, then=Stop.HOLD, wait=True)
    # wait(3000)

    # PID_Gyro(angle=0, distance=1230, speed=85)

    # turn_angle(angle=-55, speed1=50)
    # PID_Gyro(angle=-55, distance=511, speed=85)

    # wait(200)
    # turn_angle(angle=0, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=85)

    # wait(200)
    # turn_angle(angle=90, speed1=50)
    # PID_Gyro(angle=90, distance=111, speed=85)
    # wait(99999999)
    # # turn_angle(angle=30, speed=160)  
    # turn(angle=30, turnType=2, turnSpeed=650)
    # wait(3000)
    # # compass(30, 117, speed=50)
    # gyroDrivePID(angle=30, distance=117, speed=50)

    # # turn_angle(angle=60, speed=160)
    # # gyroDrivePID(angle=60, distance=300, speed=70)
    # # compass(60, 300, speed=50)
    # #   
    # # ev3.speaker.beep()
    # # wait(3000)
    # # button()
    # # wait(500)
    # # gyro_sensor.reset_angle(30)
 
    # # gyro_sensor.reset_angle(30) 
    # # print('1059: angle={0}'.format(gyro_sensor.angle()))

    # wait(9999999)


    # # Go straight to the turning point with the degreee O
    # gyroDrivePID(angle=0, distance=1255, speed=70)#55
    # # wait(90000)
    # # Turning 45degree, because 90 will hit the bridge or the continner
    # turn(angle=-55, turnType=2, turnSpeed=35)
    # wait(800)
    # # go straigght and arrive the beginning point
    # gyroDrivePID(angle=-55, distance=500, speed=55)#55

    # #turng the because point
    # # turn(angle=0, turnType=2, turnSpeed=650)
    # ev3.speaker.beep()
    # # Prepare the crab the cotinner
    # turn(angle=90, turnType=2, turnSpeed=650)
    # wait(1000)
    # fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True)

    # turn(angle=90, turnType=2, turnSpeed=35)
    # gyroDrivePID(angle=90, distance=100, speed=55)



    # if(blue==1):
    #     distance = 515
    #     degree = -55
    #     pass

    # if(blue==2):
    #     pass

    # if(blue==3):
    #     pass

    # if(green==1):
    #     pass

    # if(green==2):
    #     pass

    # if(green==3):
    #     pass

def M10_20211102(Position_Blue=1, Position_Green=2): #M10_Sorting Center
    lift_motor.run_angle(speed=260, rotation_angle=400, then=Stop.HOLD, wait=False) #formal 400, after 800

    fork_motor.run_angle(speed=250, rotation_angle=500, then=Stop.HOLD, wait=False) # formal 500, after 0

    turn_angle(angle=-20, speed1=50)
    PID_Gyro(angle=-20, distance=120, speed=85)

    turn_angle(angle=-53, speed1=50)
    PID_Gyro(angle=-53, distance=590-35, speed=85)

    turn_angle(angle=0, speed1=50)
    PID_Gyro(angle=0, distance=26+22, speed=85)  # 38Distance decide the position of continen

    lift_motor.run_angle(speed=-260, rotation_angle=800, then=Stop.HOLD, wait=False) #formal 800, after 0
    # fork_motor.run_angle(speed=250, rotation_angle=120, then=Stop.HOLD, wait=False) #formal 120, after 0

    turn_angle(angle=90, speed1=50)

    # button()
    # resetGyro()
    # placing the blue container on the bottom shelf in any of the three bays



    ############################################ Grab the conainer
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start position #formal 0, after 0
    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start position #formal 800, after 0
    fork_motor.run_until_stalled(speed=320, then=Stop.HOLD, duty_limit=None)#start position #formal 0, after 0
    lift_motor.run_until_stalled(speed=-360, then=Stop.COAST, duty_limit=None) #start position #formal 800, after 0
    # fork_motor.run_angle(speed=-120, rotation_angle=91, then=Stop.HOLD, wait=False)
    fork_motor.run_angle(speed=-320, rotation_angle=90, then=Stop.HOLD, wait=False) #formal 0, after 87
    lift_motor.run_angle(speed=320, rotation_angle=485, then=Stop.HOLD, wait=True) #470 formal 0, after 353
    # lift_motor.run_angle(speed=120, rotation_angle=350, then=Stop.HOLD, wait=True) #wait=True
    ############################################
    if(Position_Blue==3):
        degree_blue = 77
    
    if(Position_Blue==2):
        degree_blue = 90
        
    if(Position_Blue==1):
        degree_blue = 103

    # Location=2
    # turn_angle(angle=0, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=85)

    #Location=1
    # turn_angle(angle=13, speed1=50)
    # PID_Gyro(angle=13, distance=200, speed=85)

    #Location=3
    turn_angle(angle=degree_blue, speed1=50)
    PID_Gyro(angle=degree_blue, distance=170, speed=85)

    #Hold up the continer
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)

    ###### Go back to the first point
    # Location=2
    # turn_angle(angle=0, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=-85)
    
    #Location=1
    # turn_angle(angle=13, speed1=50)
    # PID_Gyro(angle=13, distance=200, speed=-85)

    #Location=3
    turn_angle(angle=degree_blue, speed1=50)
    PID_Gyro(angle=degree_blue, distance=160, speed=-85)


    #turn 180 degree, And go to the blue circle 
    turn_angle(angle=174+90, speed1=75)
    PID_Gyro(angle=174+90, distance=77, speed=85)

    ############################################ Put down the conainer
    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #Go down lift position
    # fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True) #put down the Grab wait=True
    lift_motor.run_until_stalled(speed=-360, then=Stop.COAST, duty_limit=None) #Go down lift position
    fork_motor.run_angle(speed=-320, rotation_angle=100, then=Stop.HOLD, wait=True) #put down the Grab wait=True
    ############################################

    # Go back to the first point 
    turn_angle(angle=174+90, speed1=75)
    PID_Gyro(angle=174+90, distance=77, speed=-85)

    # Hold up the grab, because it will hit the shipmission
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)

    turn_angle(angle=0+90, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=-85)

    ### the Second grab the Green continer
    ##########################################################
    fork_motor.run_angle(speed=-320, rotation_angle=91, then=Stop.HOLD, wait=False) #92
    lift_motor.run_angle(speed=320, rotation_angle=365, then=Stop.HOLD, wait=True) # wait=True 360
    # fork_motor.run_angle(speed=-120, rotation_angle=91, then=Stop.HOLD, wait=False) #92
    # lift_motor.run_angle(speed=120, rotation_angle=365, then=Stop.HOLD, wait=True) # wait=True 360

    if(Position_Green==1):
        degree_green = 13+90

    if(Position_Green==2):
        degree_green = 0+90

    if(Position_Green==3):
        degree_green = -13+90

    # Location=2
    turn_angle(angle=degree_green, speed1=50)
    PID_Gyro(angle=degree_green, distance=85, speed=85)
    #Hold up the continer
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)
        
    # Location=2 go back
    turn_angle(angle=degree_green, speed1=50)
    PID_Gyro(angle=degree_green, distance=85+30, speed=-85)

    button()

    #################

    # Hit the hellocopt
    turn_angle(angle=90, speed1=60)
    PID_Gyro(angle=90, distance=120, speed=-85)

    turn_angle(angle=152, speed1=60)
    PID_Gyro(angle=152, distance=175, speed=-85)

    wait(200)
    PID_Gyro(angle=152, distance=340, speed=85)

    turn_angle(angle=180, speed1=60)
    PID_Gyro(angle=180, distance=65, speed=85)   

    # turn_angle(angle=202, speed1=60)
    # PID_Gyro(angle=202, distance=60, speed=85)
    wait(200)
    turn_angle(angle=252, speed1=60)

    wait(200)
    turn_angle(angle=180, speed1=60)
    PID_Gyro(angle=180, distance=700, speed=85)




    # # Turn 90
    # turn_angle(angle=180, speed1=50)
    # lift_motor.run_angle(speed=120, rotation_angle=400, then=Stop.HOLD, wait=False)
    # PID_Gyro(angle=180, distance=980-15, speed=85)

    # Turn 45
    turn_angle(angle=145, speed1=50)
    lift_motor.run_angle(speed=-120, rotation_angle=400, then=Stop.HOLD, wait=False)
    PID_Gyro(angle=145, distance=97, speed=85)

    turn_angle(angle=183, speed1=50)
    PID_Gyro(angle=183, distance=700, speed=85)

    # start the next code
    lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start 
    # button()

    # wait(100000)

    # lift_motor.run_angle(speed=260, rotation_angle=400, then=Stop.HOLD, wait=False) #formal 400, after 800

    # fork_motor.run_angle(speed=250, rotation_angle=280, then=Stop.HOLD, wait=False) # formal 380, after 100

    # turn_angle(angle=-20, speed1=50)
    # PID_Gyro(angle=-20, distance=100, speed=85)

    # turn_angle(angle=-55, speed1=50)
    # PID_Gyro(angle=-55, distance=500, speed=85)


    # Distance=210, Position=3
    # Distance=120, Position=2
    # Distance=20, Position=1

    # wait(200)
    # turn_angle(angle=0, speed1=50)
    # if Position_Blue==1:
    #     Distance1=18
    # elif Position_Blue==2:
    #     Distance1=120
    # elif Position_Blue==3:
    #     Distance1=200
    
    # PID_Gyro(angle=0, distance=Distance1, speed=85)  # Distance decide the position of continen


    # wait(200)
    # turn_angle(angle=90, speed1=50)

    # lift_motor.run_angle(speed=-260, rotation_angle=600, then=Stop.HOLD, wait=True) #formal 800, after 100
    # PID_Gyro(angle=90, distance=111, speed=85)

    
    # button()
    # fork_motor.run_angle(speed=620, rotation_angle=230, then=Stop.HOLD, wait=False) 
    # lift_motor.run_angle(speed=-620, rotation_angle=800, then=Stop.HOLD, wait=True)
    # wait(3000)

    # PID_Gyro(angle=0, distance=1230, speed=85)

    # turn_angle(angle=-55, speed1=50)
    # PID_Gyro(angle=-55, distance=511, speed=85)

    # wait(200)
    # turn_angle(angle=0, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=85)

    # wait(200)
    # turn_angle(angle=90, speed1=50)
    # PID_Gyro(angle=90, distance=111, speed=85)
    # wait(99999999)
    # # turn_angle(angle=30, speed=160)  
    # turn(angle=30, turnType=2, turnSpeed=650)
    # wait(3000)
    # # compass(30, 117, speed=50)
    # gyroDrivePID(angle=30, distance=117, speed=50)

    # # turn_angle(angle=60, speed=160)
    # # gyroDrivePID(angle=60, distance=300, speed=70)
    # # compass(60, 300, speed=50)
    # #   
    # # ev3.speaker.beep()
    # # wait(3000)
    # # button()
    # # wait(500)
    # # gyro_sensor.reset_angle(30)
 
    # # gyro_sensor.reset_angle(30) 
    # # print('1059: angle={0}'.format(gyro_sensor.angle()))

    # wait(9999999)


    # # Go straight to the turning point with the degreee O
    # gyroDrivePID(angle=0, distance=1255, speed=70)#55
    # # wait(90000)
    # # Turning 45degree, because 90 will hit the bridge or the continner
    # turn(angle=-55, turnType=2, turnSpeed=35)
    # wait(800)
    # # go straigght and arrive the beginning point
    # gyroDrivePID(angle=-55, distance=500, speed=55)#55

    # #turng the because point
    # # turn(angle=0, turnType=2, turnSpeed=650)
    # ev3.speaker.beep()
    # # Prepare the crab the cotinner
    # turn(angle=90, turnType=2, turnSpeed=650)
    # wait(1000)
    # fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True)

    # turn(angle=90, turnType=2, turnSpeed=35)
    # gyroDrivePID(angle=90, distance=100, speed=55)



    # if(blue==1):
    #     distance = 515
    #     degree = -55
    #     pass

    # if(blue==2):
    #     pass

    # if(blue==3):
    #     pass

    # if(green==1):
    #     pass

    # if(green==2):
    #     pass

    # if(green==3):
    #     pass


def M10_show(Position_Blue=1, Position_Green=2): #M10_Sorting Center
    lift_motor.run_angle(speed=260, rotation_angle=400, then=Stop.HOLD, wait=False) #formal 400, after 800

    fork_motor.run_angle(speed=250, rotation_angle=500, then=Stop.HOLD, wait=False) # formal 500, after 0

    turn_angle(angle=-20, speed1=50)
    PID_Gyro(angle=-20, distance=120, speed=85)

    turn_angle(angle=-53, speed1=50)
    PID_Gyro(angle=-53, distance=590, speed=85)

    turn_angle(angle=0, speed1=50)
    PID_Gyro(angle=0, distance=46, speed=85)  # 38Distance decide the position of continen

    lift_motor.run_angle(speed=-260, rotation_angle=800, then=Stop.HOLD, wait=False) #formal 800, after 0
    # fork_motor.run_angle(speed=250, rotation_angle=120, then=Stop.HOLD, wait=False) #formal 120, after 0

    turn_angle(angle=90, speed1=50)

    # # button()
    # # resetGyro()
    # # placing the blue container on the bottom shelf in any of the three bays



    ############################################ Grab the conainer
    # fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start position #formal 0, after 0
    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start position #formal 800, after 0
    fork_motor.run_until_stalled(speed=320, then=Stop.HOLD, duty_limit=None)#start position #formal 0, after 0
    lift_motor.run_until_stalled(speed=-360, then=Stop.COAST, duty_limit=None) #start position #formal 800, after 0
    # fork_motor.run_angle(speed=-120, rotation_angle=91, then=Stop.HOLD, wait=False)
    fork_motor.run_angle(speed=-320, rotation_angle=90, then=Stop.HOLD, wait=False) #formal 0, after 87
    lift_motor.run_angle(speed=320, rotation_angle=490, then=Stop.HOLD, wait=True) #470 formal 0, after 353
    # lift_motor.run_angle(speed=120, rotation_angle=350, then=Stop.HOLD, wait=True) #wait=True
    ############################################
    if(Position_Blue==3):
        degree_blue = 77
    
    if(Position_Blue==2):
        degree_blue = 90
        
    if(Position_Blue==1):
        degree_blue = 103

    # Location=2
    # turn_angle(angle=0, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=85)

    #Location=1
    # turn_angle(angle=13, speed1=50)
    # PID_Gyro(angle=13, distance=200, speed=85)

    #Location=3
    turn_angle(angle=degree_blue, speed1=50)
    PID_Gyro(angle=degree_blue, distance=170, speed=85)

    #Hold up the continer
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)

    ###### Go back to the first point
    # Location=2
    # turn_angle(angle=0, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=-85)
    
    #Location=1
    # turn_angle(angle=13, speed1=50)
    # PID_Gyro(angle=13, distance=200, speed=-85)

    #Location=3
    turn_angle(angle=degree_blue, speed1=50)
    PID_Gyro(angle=degree_blue, distance=160, speed=-85)


    #turn 180 degree, And go to the blue circle 
    turn_angle(angle=174+90, speed1=75)
    PID_Gyro(angle=174+90, distance=77, speed=85)

    ############################################ Put down the conainer
    # lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #Go down lift position
    # fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True) #put down the Grab wait=True
    lift_motor.run_until_stalled(speed=-360, then=Stop.COAST, duty_limit=None) #Go down lift position
    fork_motor.run_angle(speed=-320, rotation_angle=100, then=Stop.HOLD, wait=True) #put down the Grab wait=True
    ############################################

    # Go back to the first point 
    turn_angle(angle=174+90, speed1=75)
    PID_Gyro(angle=174+90, distance=77, speed=-85)

    # Hold up the grab, because it will hit the shipmission
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)

    turn_angle(angle=0+90, speed1=50)
    # PID_Gyro(angle=0, distance=200, speed=-85)

    ### the Second grab the Green continer
    ##########################################################
    fork_motor.run_angle(speed=-320, rotation_angle=91, then=Stop.HOLD, wait=False) #92
    lift_motor.run_angle(speed=320, rotation_angle=365, then=Stop.HOLD, wait=True) # wait=True 360
    # fork_motor.run_angle(speed=-120, rotation_angle=91, then=Stop.HOLD, wait=False) #92
    # lift_motor.run_angle(speed=120, rotation_angle=365, then=Stop.HOLD, wait=True) # wait=True 360

    if(Position_Green==1):
        degree_green = 13+90

    if(Position_Green==2):
        degree_green = 0+90

    if(Position_Green==3):
        degree_green = -13+90

    # Location=2
    turn_angle(angle=degree_green, speed1=50)
    PID_Gyro(angle=degree_green, distance=80, speed=85)
    #Hold up the continer
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)
        
    # Location=2 go back
    turn_angle(angle=degree_green, speed1=50)
    PID_Gyro(angle=degree_green, distance=80+30, speed=-85)

    # Turn 90
    turn_angle(angle=180, speed1=50)
    lift_motor.run_angle(speed=120, rotation_angle=400, then=Stop.HOLD, wait=False)
    PID_Gyro(angle=180, distance=980+20, speed=85)

    # Turn 45
    turn_angle(angle=135, speed1=50)
    lift_motor.run_angle(speed=-120, rotation_angle=400, then=Stop.HOLD, wait=False)
    PID_Gyro(angle=135, distance=700, speed=85)

    # start the next code
    lift_motor.run_until_stalled(speed=-260, then=Stop.COAST, duty_limit=None) #start
    fork_motor.run_until_stalled(speed=120, then=Stop.HOLD, duty_limit=None)#start 
    button()




    wait(100000)

    lift_motor.run_angle(speed=260, rotation_angle=400, then=Stop.HOLD, wait=False) #formal 400, after 800

    fork_motor.run_angle(speed=250, rotation_angle=280, then=Stop.HOLD, wait=False) # formal 380, after 100

    turn_angle(angle=-20, speed1=50)
    PID_Gyro(angle=-20, distance=100, speed=85)

    turn_angle(angle=-55, speed1=50)
    PID_Gyro(angle=-55, distance=500, speed=85)


    # Distance=210, Position=3
    # Distance=120, Position=2
    # Distance=20, Position=1

    wait(200)
    turn_angle(angle=0, speed1=50)
    if Position_Blue==1:
        Distance1=18
    elif Position_Blue==2:
        Distance1=120
    elif Position_Blue==3:
        Distance1=200
    
    PID_Gyro(angle=0, distance=Distance1, speed=85)  # Distance decide the position of continen


    wait(200)
    turn_angle(angle=90, speed1=50)

    lift_motor.run_angle(speed=-260, rotation_angle=600, then=Stop.HOLD, wait=True) #formal 800, after 100
    PID_Gyro(angle=90, distance=111, speed=85)

    
    button()
    fork_motor.run_angle(speed=620, rotation_angle=230, then=Stop.HOLD, wait=False) 
    lift_motor.run_angle(speed=-620, rotation_angle=800, then=Stop.HOLD, wait=True)
    wait(3000)

    PID_Gyro(angle=0, distance=1230, speed=85)

    turn_angle(angle=-55, speed1=50)
    PID_Gyro(angle=-55, distance=511, speed=85)

    wait(200)
    turn_angle(angle=0, speed1=50)
    PID_Gyro(angle=0, distance=200, speed=85)

    wait(200)
    turn_angle(angle=90, speed1=50)
    PID_Gyro(angle=90, distance=111, speed=85)
    wait(99999999)
    # turn_angle(angle=30, speed=160)  
    turn(angle=30, turnType=2, turnSpeed=650)
    wait(3000)
    # compass(30, 117, speed=50)
    gyroDrivePID(angle=30, distance=117, speed=50)

    # turn_angle(angle=60, speed=160)
    # gyroDrivePID(angle=60, distance=300, speed=70)
    # compass(60, 300, speed=50)
    #   
    # ev3.speaker.beep()
    # wait(3000)
    # button()
    # wait(500)
    # gyro_sensor.reset_angle(30)
 
    # gyro_sensor.reset_angle(30) 
    # print('1059: angle={0}'.format(gyro_sensor.angle()))

    wait(9999999)


    # Go straight to the turning point with the degreee O
    gyroDrivePID(angle=0, distance=1255, speed=70)#55
    # wait(90000)
    # Turning 45degree, because 90 will hit the bridge or the continner
    turn(angle=-55, turnType=2, turnSpeed=35)
    wait(800)
    # go straigght and arrive the beginning point
    gyroDrivePID(angle=-55, distance=500, speed=55)#55

    #turng the because point
    # turn(angle=0, turnType=2, turnSpeed=650)
    ev3.speaker.beep()
    # Prepare the crab the cotinner
    turn(angle=90, turnType=2, turnSpeed=650)
    wait(1000)
    fork_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True)
    lift_motor.run_angle(speed=-120, rotation_angle=100, then=Stop.HOLD, wait=True)

    turn(angle=90, turnType=2, turnSpeed=35)
    gyroDrivePID(angle=90, distance=100, speed=55)



    if(blue==1):
        distance = 515
        degree = -55
        pass

    if(blue==2):
        pass

    if(blue==3):
        pass

    if(green==1):
        pass

    if(green==2):
        pass

    if(green==3):
        pass



def M13_no_attachemnt():
    #in function
    turn(angle=-19, turnType=2, turnSpeed=86)
    wait(20)
    
    gyroDrivePID(angle=-20, distance=396, speed=55)#55
    wait(20)

    turn(angle=0, turnType=2, turnSpeed=25)
    wait(1000)

    gyroDrivePID(angle=0, distance=95, speed=85)#115
    wait(200)

    robot.stop()
    lift_motor.run_angle(speed=-200, rotation_angle=443, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=-200, rotation_angle=419, then=Stop.HOLD, wait=True)
    wait(20)

    lift_motor.run_angle(speed=250, rotation_angle=443, then=Stop.HOLD, wait=False)
    # lift_motor.run_angle(speed=250, rotation_angle=419, then=Stop.HOLD, wait=False)
    gyroDrivePID(angle=0, distance=100, speed=65)
    gyroDrivePID(angle=0, distance=215, speed=65)


    lift_motor.run_angle(speed=-250, rotation_angle=150, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=-250, rotation_angle=120, then=Stop.HOLD, wait=True)
    gyroDrivePID(angle=0, distance=135, speed=95)
 

    lift_motor.run_angle(speed=250, rotation_angle=150, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=250, rotation_angle=120, then=Stop.HOLD, wait=True)
    gyroDrivePID(angle=0, distance=59, speed=-95)
    # wait(5000)



def M11_old():
    robot.stop()
    robot.settings(straight_speed=0, straight_acceleration=0, turn_rate=800, turn_acceleration=400)
    robot.turn(28)

    robot.stop()
    robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=220, turn_acceleration=80)    
    gyroDrivePID(24, 230, 95)

    
    robot.stop()
    robot.settings(straight_speed=0, straight_acceleration=0, turn_rate=800, turn_acceleration=400)
    robot.turn(-30)

    robot.stop()
    robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=220, turn_acceleration=80)    
    gyroDrivePID(-7, 42, 95)

    fork_motor.run_until_stalled(speed=-120, then=Stop.HOLD, duty_limit=None)

def M11_doctment(): # I had test five times. it works perfect for M11
    #in function
    turn(angle=-11, turnType=2, turnSpeed=86)
    wait(20)
    
    gyroDrivePID(angle=-11, distance=426, speed=85)#55

    turn(angle=-2, turnType=2, turnSpeed=56)# angle=-3
    wait(1000)

    gyroDrivePID(angle=-2, distance=152, speed=85)#115
    left_motor.stop()
    right_motor.stop()
    wait(1000)

    robot.stop()
    lift_motor.run_angle(speed=-300, rotation_angle=435, then=Stop.HOLD, wait=True)
    # wait(1000)

    turn(angle=-4, turnType=2, turnSpeed=56)# angle=-3

    gyroDrivePID(angle=-4, distance=105, speed=65)
    # wait(200)

    # turn(angle=-3, turnType=2, turnSpeed=36)# angle=-3

    # gyroDrivePID(angle=-3, distance=40, speed=65)
    # wait(200)


    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    turn(angle=5, turnType=2, turnSpeed=66)
    wait(1000)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    gyroDrivePID(angle=5, distance=76, speed=66)
    # wait(300)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)
    # turn(angle=0, turnType=2, turnSpeed=235)

    lift_motor.run_angle(speed=250, rotation_angle=435, then=Stop.HOLD, wait=False)
    # lift_motor.run_angle(speed=250, rotation_angle=419, then=Stop.HOLD, wait=False)
   
    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    # turn(angle=5, turnType=2, turnSpeed=66)
    # wait(200)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    gyroDrivePID(angle=5, distance=105, speed=65)
    # wait(200)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    turn(angle=0, turnType=2, turnSpeed=66)
    # wait(200)

    
    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)    

    gyroDrivePID(angle=0, distance=80, speed=65)
    wait(200)

    # turn(angle=0, turnType=2, turnSpeed=56)
    # wait(200)

    lift_motor.run_angle(speed=-250, rotation_angle=150, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=-250, rotation_angle=120, then=Stop.HOLD, wait=True)
    
    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)   

    gyroDrivePID(angle=0, distance=103, speed=95)
    wait(200)

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)


    lift_motor.run_angle(speed=250, rotation_angle=150, then=Stop.HOLD, wait=True)
    # lift_motor.run_angle(speed=250, rotation_angle=120, then=Stop.HOLD, wait=True)
    

    # while Button.LEFT not in ev3.buttons.pressed():
    #     wait(10)

    gyroDrivePID(angle=0, distance=85, speed=-95)
    wait(200)