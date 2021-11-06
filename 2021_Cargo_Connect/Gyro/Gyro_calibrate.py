# from Gyro.head import *
from init_head import *
import time


###The function of calbirate the gyro
# make the Gyro Sensor Calibrate because call 'GYRO-CAL'
# Another question is how to pull the value of RGB, Each R, G, B, Then check the value of real line
# I just find when use Gyro-cal the value always drift. But when I use Gyro-rate, it can calibrate the gyro
# then I just cyro-cal, last I use mode cyro-ang, beacuse I will use the degree.

def resetGyro(): #Danny_robot
    # gyro_sensor = InfraredSensor(Port.S4)
    global gyro_sensor
    my_sensor = Ev3devSensor(Port.S4)

    for i in range(13): # At first 6 times loop
    # for i in range(1): # For test At first 6 times loop
        wait(2)
        my_sensor.read('GYRO-CAL')
    # print(my_sensor.read('GYRO-ANG'))
    
    # wait(1300)
    gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)

    # for i in range(1):
    for i in range(21):
        gyro_sensor.reset_angle(0)    
    # print('Gyro detected')
    print(my_sensor.read('GYRO-ANG'))
    print(gyro_sensor.angle())
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    lift_motor.reset_angle(0)
    fork_motor.reset_angle(0)

def resetGyro_quick(): #Danny_robot
    # gyro_sensor = InfraredSensor(Port.S4)
    global gyro_sensor
    my_sensor = Ev3devSensor(Port.S4)

    for i in range(6): # At first 6 times loop
    # for i in range(1): # For test At first 6 times loop
        wait(2)
        my_sensor.read('GYRO-CAL')
    # print(my_sensor.read('GYRO-ANG'))
    
    # wait(1300)
    gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)

    # for i in range(1):
    for i in range(3):
        gyro_sensor.reset_angle(0)    
    # print('Gyro detected')
    print(my_sensor.read('GYRO-ANG'))
    print(gyro_sensor.angle())
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    lift_motor.reset_angle(0)
    fork_motor.reset_angle(0)

def resetGyro_1001():
    # gyro_sensor = InfraredSensor(Port.S4)
    global gyro_sensor
    my_sensor = Ev3devSensor(Port.S4)
    # for i in range(5)
        # print(my_sensor.read('GYRO-CAL'))
    print(my_sensor.read('GYRO-ANG'))
    # # wait(500)
    for i in range(11): # At first 6 times loop
        wait(20)
        print(my_sensor.read('GYRO-RATE'))
        # print(my_sensor.read('GYRO-G&A'))
    # #     print(my_sensor.read('GYRO-FAS'))
        # print(my_sensor.read('GYRO-G&A'))
        # print(my_sensor.read('GYRO-ANG'))
    # # # my_sensor.read('GYRO-RATE')
    # wait(1300)
    # print(my_sensor.read('GYRO-CAL'))
    # my_sensor.read('GYRO-G&A')
    # my_sensor.read('TILT-ANG')
    # wait(1300)
    print(my_sensor.read('GYRO-ANG'))
    wait(1300)
    gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
    for i in range(11): # At first 6 times loop
    # wait(200)
        gyro_sensor.reset_angle(0)
    print('Gyro detected')
    print(my_sensor.read('GYRO-ANG'))
    print(gyro_sensor.angle())

def PID_Gyro_100101(angle, distance, speed=-85):
    Kp=3.78; Ki=0.02050313433408737; Kd=174.2221429072542
    robot.reset()
    robot.stop()
    robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
    Td = distance # target distance
    Ts = speed # target speed of robot in mm/s
    integral = 0 # initialize
    derivative = 0 # initialize
    lastError = 0 # initialize
    while (abs(robot.distance()) < Td):
        error = gyro_sensor.angle() - angle # proportional 
        if (error == 0):
            integral = 0
        else:
            integral = integral + error    
        
        derivative = error - lastError  
        
        correction = (Kp*(error) + Ki*(integral) ++ Kd*derivative) * 1
        robot.drive(Ts, correction)
        lastError = error
    robot.stop()
    # robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=100, turn_acceleration=35)

def PID_Gyro(angle, distance, speed=-85):
    # # Kp=5.399999999999999; Ki=0.0001506896893501282; Kd=48377.56339826046; Ts=-70;
    # Kp=10.8; Ki=0.07534795236181951; Kd=387.0045447283584; 
    # Kp=6.6; Ki=0.00930939049243927; Kd=1169.786572906619
    # Kp=8.4; Ki=0.01185956522941589; Kd=1487.406971399474
    # Kp=11.28; Ki=0.03924857102394104; Kd=810.465175422479
    # Kp=10.28; Ki=0.04002982812881469; Kd=712.3587917549314 
    # Ts=-70;
    # Kp=9.0; Ki=0.0271624002456665; Kd=745.5158534169192
    # Kp=9.0; Ki=0.03099368047714234; Kd=653.3589973263828
    # Kp=5.399999999999999; Ki=0.01775880158885141; Kd=410.5006727805608

    ##The new car
    #inputs: Kc=90; dT=0.001304409909248352; Pc=0.5600000000000001  Ts=120
    # recommended PID parms: Kp=54.0; Ki=0.2515647682121822; Kd=2897.862070197069
    # inputs: Kc=55; dT=0.001294039416313171; Pc=0.5600000000000001
    # recommended PID parms: Kp=33.0; Ki=0.1525117883511952; Kd=1785.107911613224
    # inputs: Kc=35; dT=0.00136441011428833; Pc=0.5600000000000001
    # recommended PID parms: Kp=21.0; Ki=0.1023307585716247; Kd=1077.388671196377
    left_motor.hold()
    right_motor.hold()
    
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)


    # Kp=3.78; Ki=0.02050313433408737; Kd=174.2221429072542
    Kp=10.8; Ki=0.05294958932059151; Kd=550.7124866152643
    robot.reset()
    robot.stop()
    robot.settings(straight_speed=speed, straight_acceleration=75, turn_rate=750, turn_acceleration=99999)
    # robot.distance_control.limits(speed=650, acceleration=35, actuation=100)
    # robot.heading_control.limits(speed=650, acceleration=35, actuation=100)
    # robot.heading_control.target_tolerances(position=0)
    # robot.distance_control.target_tolerances(position=0)


    # print('101')
    # Kp=18; Ki=0; Kd=0; Ts=speed;
    Td = distance # target distance

    if speed>=0:
        Ts = speed + 40# target speed of robot in mm/s + to improve the speed
    else:
        Ts = speed - 40# target speed of robot in mm/s + to improve the speed
    # Kp = 3 #  the Constant 'K' for the 'p' proportional controller

    integral = 0 # initialize
    # Ki = 0.025 #  the Constant 'K' for the 'i' integral term
    derivative = 0 # initialize
    lastError = 0 # initialize
    # Kd = 3 #  the Constant 'K' for the 'd' derivative term
    # print('112, gyro_sensor.angle()= {0}, angle={1}'.format(gyro_sensor.angle(), angle))
    while (abs(robot.distance()) < Td):
        error = gyro_sensor.angle() - angle # proportional 
        if (error == 0):
            integral = 0
        else:
            integral = integral + error    
        
        derivative = error - lastError  
        
        correction = (Kp*(error) + Ki*(integral) ++ Kd*derivative) * -1
        # some times the chris robot use -1, Danny robot use 1
        robot.drive(Ts, correction)
        lastError = error
    
    # print("error " + str(error) + "; integral " + str(integral) + "; correction " + str(correction)  )    
    print('131, Finish PID_Gyro, distance= {0}, angle={1}'.format(robot.distance(), gyro_sensor.angle()))
    robot.stop()
    robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=120, turn_acceleration=35)
    left_motor.hold()
    right_motor.hold()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

def turn_angle(angle, speed1=65):
    left_motor.hold()
    right_motor.hold()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    robot.reset() # ADD becaue 0 turn always float
    robot.stop()
    robot.settings(straight_speed=0, straight_acceleration=0, turn_rate=9999999, turn_acceleration=9999999)
    # robot.distance_control.limits(speed=0, acceleration=0, actuation=100)
    # robot.distance_control.limits(acceleration=0, actuation=100)
    robot.distance_control.target_tolerances(position=0)
    # robot.heading_control.limits(speed=800, acceleration=9999, actuation=100)
    # robot.heading_control.target_tolerances(position=0)
    # robot.distance_control.target_tolerances(position=0)
    
    # #Motor Control 
    # left_motor.control.limits(speed=9999, acceleration=9999, actuation=100)
    # right_motor.control.limits(speed=9999, acceleration=9999, actuation=100)
    # left_motor.control.target_tolerances(position=0)
    # right_motor.control.target_tolerances(position=0)
    # if angle < 0:
    # if gyro_sensor.angle() < angle:
    left_motor.stop()
    right_motor.stop()
    # print('gyro_angle()={0}, angle={1}'.format(gyro_sensor.angle(), angle))
    # print(gyro_sensor.angle())
    # print(angle)
    # if gyro_sensor.angle()<0 and angle>=0:
    #     while angle > gyro_sensor.angle():
    #         left_motor.run(speed= speed1)
    #         # left_motor.hold()
    #         right_motor.run(speed=(-1 * speed1))
    #         # left_motor.dc(38)
    #         # right_motor.dc(-38)
    #         print('185')
    #     left_motor.hold()
    #     right_motor.hold()        
#****************************
    if gyro_sensor.angle() > angle:
        while gyro_sensor.angle() > angle:
            left_motor.run(speed=(-1 * speed1))
            right_motor.run(speed= speed1)
        left_motor.hold()
        right_motor.hold()
    # elif gyro_sensor.angle() >= angle:  
    elif gyro_sensor.angle() < angle:  
        while gyro_sensor.angle() < angle:
            left_motor.run(speed= speed1)
            right_motor.run(speed=(-1 * speed1))
        left_motor.hold()
        right_motor.hold()
    else:
        print("196 gyro_sensor.angle()=angle={0}".format(angle))

    print('Turn_Finished,Gyro_sensor.angle={0}, Robot_distance={1}'.format(gyro_sensor.angle(), robot.distance()))
    robot.stop()
    robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=100, turn_acceleration=35)
    # robot.distance_control.limits(speed=650, acceleration=35, actuation=100)
    # robot.distance_control.target_tolerances(position=0)
    # robot.heading_control.limits(speed=650, acceleration=35, actuation=100)
    # robot.heading_control.target_tolerances(position=0)

    # Mortor Control
    # left_motor.control.limits(speed=650, acceleration=35, actuation=100)5
    # right_motor.control.limits(speed=650, acceleration=35, actuation=100)
    # # left_motor.control.target_tolerances(speed=speed1, position=0)
    # right_motor.control.target_tolerances(speed=speed1, position=0)

    left_motor.hold()
    right_motor.hold()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    wait(50)

def Record_Data():
    while True:
        if Button.CENTER in ev3.buttons.pressed():
        # if pressed:
            print('degree=:{0},  this journey distance:{1}'.format(gyro_sensor.angle(), robot.distance()))
            print(gyro_sensor.angle())
            robot.reset()
            wait(1000)
            continue

def PID_Gyro_1001(angle, distance, speed=-70):
    # # Kp=5.399999999999999; Ki=0.0001506896893501282; Kd=48377.56339826046; Ts=-70;
    # Kp=144.0; Ki=0.8202338607788086; Kd=6320.148737919469
    Kp=11;Ki=0;Kd=0;
    Ts=speed
    robot.reset()
    robot.stop()
    # robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
    robot.settings(straight_speed=speed, straight_acceleration=35, turn_rate=120, turn_acceleration=35)
    left_motor.hold()
    right_motor.hold()
    # gyro_sensor.reset_angle(0)

    # Kp=67; Ki=0; Kd=0; Ts=speed;
    Td = distance # target distance
    # Ts = 50 # target speed of robot in mm/s
    # Kp = 3 #  the Constant 'K' for the 'p' proportional controller
    #******************************PID Control Method
    lastError = 0
    integral = 0
    derivative = 0
    #when robot go forwar speed positive. When go backward, speed is negative.
    while abs(robot.distance()) < distance:
        error = gyro_sensor.angle()-angle
        integral += error
        steering = (Kp*error + Ki*integral + + Kd*derivative)*-1
        robot.drive(speed, steering)
        # reset the degree
        # cali_gyro_0()
        # print('reset the degree')
        # gyro_sensor.reset_angle(angle) # I want test Keep The Degree
        derivative = error - lastError

    ##************************************************************************
    # integral = 0 # initialize
    # # Ki = 0.025 #  the Constant 'K' for the 'i' integral term

    # derivative = 0 # initialize
    # lastError = 0 # initialize
    # # Kd = 3 #  the Constant 'K' for the 'd' derivative term
    # print(gyro_sensor.angle())
    # print(angle)
    # while (abs(robot.distance()) < Td):
    #     error = gyro_sensor.angle()- angle # proportional 
        
    #     if (error == 0):
    #         integral = 0
    #     else:
    #         integral = integral + error    
        
    #     derivative = error - lastError  
        
    #     correction = (Kp*(error) + Ki*(integral) ++ Kd*derivative) * 1
        
    #     robot.drive(Ts, correction)

    #     lastError = error
    
    # # print("error " + str(error) + "; integral " + str(integral) + "; correction " + str(correction)  )    
        
    robot.stop()
    robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=120, turn_acceleration=35)
    left_motor.hold()
    right_motor.hold()
    # gyro_sensor.reset_angle(angle)

def calibrate_gyro_offset():
    global gyro_offset

    gyro_minimum_rate = 0
    gyro_maximum_rate = 2

    iteration = 0
    while (gyro_maximum_rate - gyro_minimum_rate) >= 1:
        gyro_minimum_rate = 440
        gyro_maximum_rate = -440
        gyro_sum = 0.0
        for i in range(200):
            gyro_sensor_value = gyro_sensor.angle()

            gyro_sum += gyro_sensor_value
            if gyro_sensor_value > gyro_maximum_rate:
                gyro_maximum_rate = gyro_sensor_value
            if gyro_sensor_value < gyro_minimum_rate:
                gyro_minimum_rate = gyro_sensor_value
            wait(10)

        # log.debug("Calibrating gyro iteration: {:2d}, gyro_sum: {:4.2f}, gyro_minimum_rate: {:4.2f}, gyro_maximum_rate: {:4.2f}".format(
        #     iteration, gyro_sum, gyro_minimum_rate, gyro_maximum_rate))

        iteration += 1

    gyro_offset = gyro_sum / 200.0

def resetGyro_change():
    global gyro_sensor
    my_sensor = Ev3devSensor(Port.S4)
    wait(1000)
    my_sensor.read('GYRO-CAL')
    wait(2000)
    for i in range(9):
        wait(200)
        my_sensor.read('GYRO-RATE')

    my_sensor.read('GYRO-ANG')
    wait(1100)
    gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
    gyro_sensor.reset_angle(0)
    print('Gyro detected')

def resetGyro_oldGyro():
    # Calibrate the gyro offset. This makes sure that the robot is perfectly
# still by making sure that the measured rate does not fluctuate more than
#  2 deg/s. Gyro drift can cause the rate to be non-zero even when the robot
# is not moving, so we save that value for use later.
    gyro_sensor.reset_angle(0)
    while True:
        # gyro_minimum_rate, gyro_maximum_rate = 440, -400
        gyro_minimum_rate, gyro_maximum_rate =  32767, - 32767
        gyro_sum = 0
        print('Now We Start the Gyro_Calibrate')
        for _ in range(GYRO_CALIBRATION_LOOP_COUNT):
            gyro_sensor_value = gyro_sensor.angle()
            gyro_sum += gyro_sensor_value
            if gyro_sensor_value > gyro_maximum_rate:
                gyro_maximum_rate = gyro_sensor_value
            if gyro_sensor_value < gyro_minimum_rate:
                gyro_minimum_rate = gyro_sensor_value
            wait(2)
        if gyro_maximum_rate - gyro_minimum_rate <0.0000001: #formar value is 2
            break
    
    print("the Port_2 Groy offset =")
    gyro_offset = gyro_sum / GYRO_CALIBRATION_LOOP_COUNT
    print(gyro_offset)
    ev3.light.on(Color.GREEN)
    print('Now We had finished the Gyro_Calibrate')
    gyro_sensor.reset_angle(0)


def resetGyro_0929():
    global gyro_sensor
    # gyro_sensor = InfraredSensor(Port.S4)
    my_sensor = Ev3devSensor(Port.S4)
    # my_sensor.read('GYRO-CAL')
    # my_sensor.read('GYRO-ANG')
    gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
    for i in range(5):
        gyro_sensor.reset_angle(0)
    # wait(1000)
    for i in range(5): # At first 6 times loop
        wait(200)
        print(my_sensor.read('GYRO-CAL'))
        # print(my_sensor.read('GYRO-FAS'))
        # print(my_sensor.read('GYRO-G&A'))
        # v = my_sensor.read('GYRO-ANG')
        # my_sensor.read('GYRO-CAL')
        # v = my_sensor.read('GYRO-ANG')
    # my_sensor.read('GYRO-CAL') # At first I didn't use, but I think I shold make it stay completet quietly. befor and after 1second
    # But When I unplug and plug in, It seems no work. So I have to delete this sentence
    # wait(1000)
    wait(500)
    # my_sensor.read('GYRO-CAL')  # This is the new mode
    # gyro_sensor = InfraredSensor(Port.S4)
    my_sensor.read('GYRO-ANG')
    # wait(1100)
    wait(500)
    gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
    gyro_sensor.reset_angle(0)
    print('Gyro detected')

def resetGyro_0920(): # For the old Gyro_sensor 
    global gyro_sensor
    # gyro_sensor = InfraredSensor(Port.S4)
    my_sensor = Ev3devSensor(Port.S4)

    for i in range(11): # At first 6 times loop

        # wait(200)
        wait(200)
        # print(my_sensor.read('GYRO-CAL'))
        print(my_sensor.read('GYRO-RATE'))
        # print(my_sensor.read('GYRO-FAS'))
        # print(my_sensor.read('GYRO-G&A'))
        # wait(1000) #make a short time

        # wait(200)
        # v = my_sensor.read('GYRO-ANG')
        # print(v)
        # wait(200)
        # my_sensor.read('GYRO-CAL')
        # wait(200)
        # v = my_sensor.read('GYRO-ANG')
        # print(v)
        # wait(200)
    # wait(1000)
    # my_sensor.read('GYRO-CAL') # At first I didn't use, but I think I shold make it stay completet quietly. befor and after 1second
    # But When I unplug and plug in, It seems no work. So I have to delete this sentence
    # wait(1000)
    # wait(1000)
    # my_sensor.read('GYRO-CAL')  # This is the new mode
    # gyro_sensor = InfraredSensor(Port.S4)
    my_sensor.read('GYRO-ANG')
    # wait(1100)
    wait(1300)
    gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
    gyro_sensor.reset_angle(0)
    # calibrate_gyro_offset()
    print('Gyro detected')
    # if the drift will always extent, Then the last way we can do is unplog in the cable, and then replug in Port4

    
        

def resetGyro_old_version():
    global gyro_sensor
    my_sensor = Ev3devSensor(Port.S4)
    # my_sensor.read('GYRO-CAL')
    # wait(1000)
    for i in range(6): # At first 6 times loop

        # wait(200)
        wait(200)
        # print(my_sensor.read('GYRO-CAL'))
        print(my_sensor.read('GYRO-RATE'))
        # print(my_sensor.read('GYRO-FAS'))
        # print(my_sensor.read('GYRO-G&A'))
        # wait(1000) #make a short time

        # wait(200)
        # v = my_sensor.read('GYRO-ANG')
        # print(v)
        # wait(200)
        # my_sensor.read('GYRO-CAL')
        # wait(200)
        # v = my_sensor.read('GYRO-ANG')
        # print(v)
        # wait(200)
    # wait(1000)
    # my_sensor.read('GYRO-CAL') # At first I didn't use, but I think I shold make it stay completet quietly. befor and after 1second
    # But When I unplug and plug in, It seems no work. So I have to delete this sentence
    wait(1000)
    my_sensor.read('GYRO-ANG')
    gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
    gyro_sensor.reset_angle(0)
    print('Gyro detected')

def Gyro_Calibration():
    # while True
    pass


# # I want define a new method, We I input the angle, The Robot Turn Add the angle. Not the 
# def gyro_turn(angle, speed):
#     # gyro_sensor.reset_angle(0)
#     Degree=gyro_sensor.angle()

#     if angle < 0:
#         while gyro_sensor.angle() > (Degree + angle):
#             left_motor.run(speed=(-1 * speed))
#             right_motor.run(speed=speed)
#             wait(10)
#     elif angle > 0:  
#         while gyro_sensor.angle() < (Degree + angle):
#             left_motor.run(speed=speed)
#             right_motor.run(speed=(-1 * speed))
#             wait(10)  
#     else:
#         print("Error: no angle chosen")

#     left_motor.brake()
#     right_motor.brake() 



# def gyro_straight(distance, robotSpeed):
#     robot.reset() 
#     # gyro_sensor.reset_angle(0)
#     wait(3)
#     # print("This is the Gyro_sensor, Speed and angle")
#     # print(gyro_sensor.speed())
#     # I define a Degree, Then Make the Robot Keeping this degree to go forward
#     Degree=gyro_sensor.angle()
#     # print(gyro_sensor.angle())
#     PROPORTIONAL_GAIN = 1.1
#     if distance < 0: # move backwards
#         while robot.distance() > distance:
#             reverseSpeed = -1 * robotSpeed        
#             angle_correction = -1 * PROPORTIONAL_GAIN * ( gyro_sensor.angle() - Degree)
#             robot.drive(reverseSpeed, angle_correction) 
#             wait(10)
#     elif distance > 0: # move forwards             
#         while robot.distance() < distance:
#             angle_correction = -1 * PROPORTIONAL_GAIN * ( gyro_sensor.angle() - Degree)
#             robot.drive(robotSpeed, angle_correction) 
#             wait(10)            
#     robot.stop()

def gyro_turn(angle, speed=50):
    # Gyro_Calibrate()
    # gyro_sensor.reset_angle(0)
    # gyro_sensor_4.reset_angle(0)
    initial_degree = gyro_sensor.angle()
    # print("dfsdf")
    # print(angle)
    # print(gyro_sensor.angle())
    # Port2_offset = 2
    # Port4_offset = -1
    if angle < 0:
        while gyro_sensor.angle() > initial_degree + angle:
            # left_motor.run(speed=(-1 * speed))
            # right_motor.run(speed=speed)
            robot.turn(-1)
            wait(10)
    elif angle > 0:  
        while gyro_sensor.angle() < initial_degree + angle:
            # left_motor.run(speed=speed)
            # right_motor.run(speed=(-1 * speed))
            robot.turn(1)
            wait(10)  
    else:
        print("Error: no angle chosen")

    left_motor.brake()
    right_motor.brake() 



#the basic make robot move straight
#the function was replaced by the new Gyro PID degree following the line
def gyro_straight(distance, robotSpeed=80):
    robot.reset() 
    initial = gyro_sensor.angle()
    # gyro_sensor.reset_angle(0)
    wait(3)
    # print("This is the Gyro_sensor, Speed and angle")
    # print(gyro_sensor.speed())
    # gyro_sensor.reset_angle(0)
    # gyro_sensor_4.reset_angle(0)
    # print(gyro_sensor.angle())
    PROPORTIONAL_GAIN = 1.5
    # if(gyro_offset_4==0):
    #     gyro_sensor_Who = gyro_sensor_4
    
    # if(gyro_offset ==0):
    #     gyro_sensor_Who = gyro_sensor

    if distance < 0: # move backwards
        while robot.distance() > distance:
            reverseSpeed = -1 * robotSpeed        
            angle_correction = -1 * PROPORTIONAL_GAIN * (gyro_sensor.angle()-initial)
            robot.drive(reverseSpeed, angle_correction) 
            wait(10)
    elif distance > 0: # move forwards             
        while robot.distance() < distance:
            angle_correction = -1 * PROPORTIONAL_GAIN * (gyro_sensor.angle()-initial)
            robot.drive(robotSpeed, angle_correction) 
            wait(10)            
    robot.stop()




def confirm_half_value():
    ev3.screen.print('Left White color')
    ev3.screen.print('Press LEFT button')
    ev3.speaker.say('Left White color')
    while Button.LEFT not in ev3.buttons.pressed():
        wait(10)
    ev3.screen.clear()
    ev3.screen.print(left_color_sensor.reflection())
    WHITE_REFLECT_L = left_color_sensor.reflection()

    wait(2000)
    ev3.screen.clear()
    ev3.screen.print('Left Black color')
    ev3.screen.print('Press RIGHT button')
    ev3.speaker.say('Left Black color')
    while Button.RIGHT not in ev3.buttons.pressed():
        wait(10)
    ev3.screen.clear()
    ev3.screen.print(left_color_sensor.reflection())
    BLACK_REFLECT_L = left_color_sensor.reflection()

    global HALF_VLAUE_L
    HALF_VLAUE_L = (BLACK_REFLECT_L + WHITE_REFLECT_L )/2
    print(HALF_VLAUE_L)

    wait(2000)
    ev3.screen.clear()
    ev3.screen.print('Right White color')
    ev3.screen.print('Press UP button')
    ev3.speaker.say('Right White color')
    while Button.UP not in ev3.buttons.pressed():
        wait(10)
    ev3.screen.clear()
    ev3.screen.print(right_color_sensor.reflection())
    WHITE_REFLECT_R = right_color_sensor.reflection()

    wait(2000)
    ev3.screen.clear()
    ev3.screen.print('Right Black color')
    ev3.screen.print('Press DOWN button')
    ev3.speaker.say('right Black color')
    while Button.DOWN not in ev3.buttons.pressed():
        wait(10)
    ev3.screen.clear()
    ev3.screen.print(right_color_sensor.reflection())
    BLACK_REFLECT_R = right_color_sensor.reflection()


    global HALF_VLAUE_R
    HALF_VLAUE_R = (BLACK_REFLECT_R + WHITE_REFLECT_R )/2
    print(HALF_VLAUE_R)


#Following the line for the distance. at the speed, if didn't give according to the default value
# l_r_sensor means left or right sensor
# l_r means left part of the line or the right part of the line to following
def lineFollow(distance, l_r_sensor='r', l_r='r', speed=50):
    robot.stop()
    robot.reset()
    robot.settings(straight_speed=30, straight_acceleration=30, turn_rate=88, turn_acceleration=88)
    derivative = 0
    integral = 0
    last_error = 0
    speed_factor = 2
    print('I am herein linefollowing')
    # print(left_color_sensor.reflection())
    kp = 0.6  # The formar is 0.4
    ki = 0.0007 #0.0007 # the Formar is 0.0015
    kd = 0.03 #0.03   # The formar is 0.4
    if l_r == 'l':
        a = -1
    if l_r == 'r':
        a = 1
    if l_r_sensor =='r':
        while robot.distance()<distance:
            proportional = right_color_sensor.reflection() - 45
            integral += proportional
            steering = a* ((kp* proportional) + (ki* integral) + (kd * derivative))
            drive_speed = speed-(speed_factor*(abs(proportional-last_error)))
            robot.drive(drive_speed, steering)            
            last_error = proportional
            derivative = last_error-proportional
        robot.stop()
    else:
        while robot.distance()<distance:
            proportional = left_color_sensor.reflection() - 45
            integral += proportional
            steering = a* ((kp* proportional) + (ki* integral) + (kd * derivative))
            drive_speed = speed-(speed_factor*(abs(proportional-last_error)))
            robot.drive(drive_speed, steering)
            last_error = proportional
            derivative = last_error-proportional
            #When the Right Color Sensor Detect the White We should make robot to stop and broke jump out the loop
            # color_sensor = Ev3devSensor(Port.S3)
            # print(color_sensor.read('RGB-RAW'))
            
            # I just test the code for recolbirate the sensor
            # in here I just test the color of RGB value. to test the light value
            # r, g, b = color_sensor.read('RGB-RAW')
            # print(r)
            # print(g)
            # print(b)
            # if r>150 and g>150 and b>100:
            #     robot.stop()
            #     print('I will jump to the lineFollow')
            #     break                
            # if right_color_sensor.color()==Color.WHITE:
            #     robot.stop()
            #     print('I will jump to the lineFollow')
            #     break

        robot.stop()


def lineFollowCC(distance, l_r_sensor='r', l_r='r', speed=50):
    print('in the lineFollowCC')
    print(HALF_VLAUE_R)
    print(HALF_VLAUE_L)
    robot.stop()
    robot.reset()
    robot.settings(straight_speed=30, straight_acceleration=30, turn_rate=88, turn_acceleration=88)
    derivative = 0
    integral = 0
    last_error = 0
    speed_factor = 2
    print('I am herein linefollowing')
    # print(left_color_sensor.reflection())
    kp = 0.6  # The formar is 0.4
    ki = 0.0007 #0.0007 # the Formar is 0.0015
    kd = 0.03 #0.03   # The formar is 0.4
    if l_r == 'l':
        a = -1
    if l_r == 'r':
        a = 1
    if l_r_sensor =='r':
        while robot.distance()<distance:
            proportional = right_color_sensor.reflection() - HALF_VLAUE_R
            integral += proportional
            steering = a* ((kp* proportional) + (ki* integral) + (kd * derivative))
            drive_speed = speed-(speed_factor*(abs(proportional-last_error)))
            robot.drive(drive_speed, steering)            
            last_error = proportional
            derivative = last_error-proportional
        robot.stop()
    else:
        while robot.distance()<distance:
            proportional = left_color_sensor.reflection() - HALF_VLAUE_L
            integral += proportional
            steering = a* ((kp* proportional) + (ki* integral) + (kd * derivative))
            drive_speed = speed-(speed_factor*(abs(proportional-last_error)))
            robot.drive(drive_speed, steering)
            last_error = proportional
            derivative = last_error-proportional
            # #When the Right Color Sensor Detect the White We should make robot to stop and broke jump out the loop
            # # color_sensor = Ev3devSensor(Port.S3)
            # # print(color_sensor.read('RGB-RAW'))
            # r, g, b = color_sensor.read('RGB-RAW')
            # print(r)
            # print(g)
            # print(b)
            # if r>150 and g>150 and b>100:
            #     robot.stop()
            #     print('I will jump to the lineFollow')
            #     break                
            # if right_color_sensor.color()==Color.WHITE:
            #     robot.stop()
            #     print('I will jump to the lineFollow')
            #     break

        robot.stop()


def lineFollow_Stop_on_Cross(distance, l_r_sensor='r', l_r='r', speed=50):
    robot.stop()
    robot.reset()
    robot.settings(straight_speed=30, straight_acceleration=30, turn_rate=88, turn_acceleration=88)
    derivative = 0
    integral = 0
    last_error = 0
    speed_factor = 2
    print('I am herein linefollowing')
    # print(left_color_sensor.reflection())
    kp = 0.6  # The formar is 0.4
    ki = 0.0007 #0.0007 # the Formar is 0.0015
    kd = 0.03 #0.03   # The formar is 0.4
    if l_r == 'l':
        a = -1
    if l_r == 'r':
        a = 1
    if l_r_sensor =='r':
        while robot.distance()<distance:
            proportional = right_color_sensor.reflection() - 45
            integral += proportional
            steering = a* ((kp* proportional) + (ki* integral) + (kd * derivative))
            drive_speed = speed-(speed_factor*(abs(proportional-last_error)))
            robot.drive(drive_speed, steering)            
            last_error = proportional
            derivative = last_error-proportional
            color_sensor = Ev3devSensor(Port.S1)
            r, g, b = color_sensor.read('RGB-RAW')
            if r>180 and g>180 and b>120:
                robot.stop()
                print('I will jump to the lineFollow')
                break   
        robot.stop()
    else:
        while robot.distance()<distance:
            proportional = left_color_sensor.reflection() - 45
            integral += proportional
            steering = a* ((kp* proportional) + (ki* integral) + (kd * derivative))
            drive_speed = speed-(speed_factor*(abs(proportional-last_error)))
            robot.drive(drive_speed, steering)
            last_error = proportional
            derivative = last_error-proportional
            #When the Right Color Sensor Detect the White We should make robot to stop and broke jump out the loop
            # color_sensor = Ev3devSensor(Port.S3)
            # print(color_sensor.read('RGB-RAW'))
            color_sensor2 = Ev3devSensor(Port.S3)
            r, g, b = color_sensor2.read('RGB-RAW')
            print(r)
            print(g)
            print(b)
            if r>180 and g>180 and b>120:
                robot.stop()
                print('I will jump to the lineFollow')
                break                
            # if right_color_sensor.color()==Color.WHITE:
            #     robot.stop()
            #     print('I will jump to the lineFollow')
            #     break

        robot.stop()



def lineSquare(returnSeconds=3, startSpeed=120, motorstartSpeed=100, forwardSpeed=50, backwardSpeed=50):
    print('inside the lineSquare')
    blackTarget = 17
    whiteTarget = 80
    target = 40
    courseAdjustment = True
    while courseAdjustment:
        robot.drive(startSpeed, 0)
        if left_color_sensor.reflection()<blackTarget:
            robot.stop()
            while right_color_sensor.reflection()>blackTarget:
                right_motor.run(motorstartSpeed)
            right_motor.stop()
            courseAdjustment = False
        else:
            if right_color_sensor.reflection()<blackTarget:
                robot.stop()
                while left_color_sensor.reflection()>blackTarget:
                    left_motor.run(startSpeed)
                left_motor.stop()
                courseAdjustment = False
            else:
                continue

    fineAdjustment = True
    rightAlign = False
    leftAlign = False

    while fineAdjustment:
        if left_color_sensor.reflection()<(target-5):
            left_motor.run(forwardSpeed)
        elif left_color_sensor.reflection()>(target+5):
            left_motor.run(backwardSpeed)
        else:
            left_motor.stop()
        
        if right_color_sensor.reflection()<(target-5):
            right_motor.run(forwardSpeed)
        elif right_color_sensor.reflection()>(target+5):
            right_motor.run(backwardSpeed)
        else:
            right_motor.stop()
        
        if right_color_sensor.reflection()<(target+3) and right_color_sensor.reflection()>(target-3):
            rightAlign = True
        if left_color_sensor.reflection()<(target+3) and left_color_sensor.reflection()>(target-3):
            leftAlign = True

        if rightAlign and leftAlign:
            print('Both rightAlign and leftAlign is True')
            left_motor.stop()
            right_motor.stop()
            fineAdjustment = False



#Make the robot to following the Gyro degree. According to the PID Control, control the robot to following the degree.
#make the robot move distance accoring the angle'degree.
# go forward make the speed positive. go backward make the speed nagative.
#Very imort the angle reprent the Navigate degree, like the earth Noth Degree, South Degree


#Use The control class to advance the distance
# Control the robot to go staight and make the robot angle is 0, then following the turn(0)
# So that is mean replace the PID control, Because I find when PID robot always shaker
def Go_Straight_line(dist=0, speed=76):
    robot.stop()
    robot.settings(straight_speed=speed, straight_acceleration=100000, turn_rate=99999, turn_acceleration=99999)
    robot.heading_control.limits(speed=349, acceleration=100000, actuation=100)
    robot.heading_control.pid(kp=300, ki=600, kd=2, integral_range=0, integral_rate=0, feed_forward=1)
    # robot.distance_control.pid(kp=200, ki=600, kd=2, integral_range=0, integral_rate=0, feed_forward=1)
    robot.heading_control.target_tolerances(position=0)
    robot.straight(dist)
    robot.stop()
    robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=120, turn_acceleration=35)
    robot.heading_control.limits(speed=650, acceleration=35, actuation=100)
    # print(robot.heading_control.pid())    



def Turn_on_position(degree=0, t_rate=35):
    robot.stop()
    robot.settings(straight_speed=666, straight_acceleration=666, turn_rate=666, turn_acceleration=666)
    robot.distance_control.target_tolerances(position=0)
    robot.turn(degree)
    # robot.straight(1)
    robot.stop()
    robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=120, turn_acceleration=35)
    robot.heading_control.limits(speed=650, acceleration=35, actuation=100)

def gyroDrivePID(angle, distance, speed=70):
    # robot.stop()
    print('we are here')
    # robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
    # Every time, We will make the distance to zero. Then we can keep robot move 'distance',according some degree.
    robot.reset()
    robot.stop()
    # robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
    robot.settings(straight_speed=speed, straight_acceleration=35, turn_rate=120, turn_acceleration=35)
    # But if we put reset, The degree also set to Zero??
    # robot.settings(straight_ac/celeration=1)
    # robot.settings(straight_speed=120, straight_acceleration=5)


    # I want control the distance and turn with the control class
    # robot.settings(straight_speed=10, straight_acceleration=10, turn_rate=182, turn_acceleration=792)

    # robot.distance_control.limits(speed=650, acceleration=35, actuation=100)
    # robot.heading_control.limits(speed=650, acceleration=35, actuation=100)
    # robot.heading_control.target_tolerances(position=0)
    # robot.distance_control.target_tolerances(position=0)
    # if(speed>71):
    kp=6.6 #5.399999999999999 #18
    ki=0#0.0001506896893501282#0.0018
    kd=0#48377.56339826046#0.001188
    # else:
        # kp =7.95  #7.2#at first is 7, 9, 11.18 7.5
        # ki =0.0065# at first is 0.003 0.005 0.0096
        # kd =0.00429# at first is 0.4 0.6 0.2
    
    # print('Kp={0}, Ki={1}, Kd={2}'.format(kp, ki,kd))
    lastError = 0
    integral = 0
    derivative = 0
    #when robot go forwar speed positive. When go backward, speed is negative.
    while abs(robot.distance()) < distance:
        error = gyro_sensor.angle()-angle
        integral += error
        steering = (kp*error + ki*integral + + kd*derivative)*1
        robot.drive(speed, steering)
        # reset the degree
        # cali_gyro_0()
        # print('reset the degree')
        # gyro_sensor.reset_angle(angle) # I want test Keep The Degree
        derivative = error - lastError
        # lastError = error 
    
    robot.stop()
    robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=120, turn_acceleration=35)
    print('PID_Finised,Gyro_sensor.angle={0}, Robot_distance={1}'.format(gyro_sensor.angle(), robot.distance()))
    left_motor.hold()
    right_motor.hold()
    wait(200)


def gyroDrivePID_0926(angle, distance, speed=70):
    # robot.stop()
    print('we are here')
    # robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
    # Every time, We will make the distance to zero. Then we can keep robot move 'distance',according some degree.
    robot.reset()
    robot.stop()
    robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
    # robot.settings(straight_speed=speed, straight_acceleration=35, turn_rate=120, turn_acceleration=35)
    # But if we put reset, The degree also set to Zero??
    # robot.settings(straight_ac/celeration=1)
    # robot.settings(straight_speed=120, straight_acceleration=5)


    # I want control the distance and turn with the control class
    # robot.settings(straight_speed=10, straight_acceleration=10, turn_rate=182, turn_acceleration=792)

    robot.distance_control.limits(speed=650, acceleration=35, actuation=100)
    robot.heading_control.limits(speed=650, acceleration=35, actuation=100)
    robot.heading_control.target_tolerances(position=0)
    robot.distance_control.target_tolerances(position=0)
    # if(speed>71):
    kp=18 #5.399999999999999 #18
    ki=0#0.0001506896893501282#0.0018
    kd=0#48377.56339826046#0.001188
    # else:
        # kp =7.95  #7.2#at first is 7, 9, 11.18 7.5
        # ki =0.0065# at first is 0.003 0.005 0.0096
        # kd =0.00429# at first is 0.4 0.6 0.2
    
    # print('Kp={0}, Ki={1}, Kd={2}'.format(kp, ki,kd))
    lastError = 0
    integral = 0
    derivative = 0
    #when robot go forwar speed positive. When go backward, speed is negative.
    while abs(robot.distance()) < distance:
        error = (gyro_sensor.angle()-angle)*1
        integral += error
        steering = (kp*error + ki*integral + + kd*derivative)*-1
        robot.drive(speed, steering)
        # reset the degree
        # cali_gyro_0()
        # print('reset the degree')
        # gyro_sensor.reset_angle(angle) # I want test Keep The Degree
        derivative = error - lastError
        # lastError = error 
    
    robot.stop()
    robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=120, turn_acceleration=35)
    print('PID_Finised,Gyro_sensor.angle={0}, Robot_distance={1}'.format(gyro_sensor.angle(), robot.distance()))
    left_motor.hold()
    right_motor.hold()
    wait(200)

# The postive number +  means trun right.  
# The nagative number - means turn left.
# When two wheel move together, on forward, another go backward. use turnType=2
# When only one wheel to move. use turnType=1 turn right, move  left wheel, the right wheel stuck.
# When only one wheel to move, use turnType=1 turn left, move right wheel. the left wheel stuck.(when turn left, I fonnd the robot will move forward a little few distance)
def turn_0929(angle, turnType=1, turnSpeed=520):
    robot.stop()
    # init_distance = robot.distance()
    # print('At first Distance={0}'.format(robot.distance()))
    robot.settings(straight_speed=0, straight_acceleration=0, turn_rate=turnSpeed, turn_acceleration=200)
    if turnType == 1:
        if gyro_sensor.angle()<angle-3:
            while gyro_sensor.angle()<angle:
                left_motor.run(turnSpeed)
            left_motor.stop()
        else:
            while gyro_sensor.angle()>angle+3:
                right_motor.run(turnSpeed)
            right_motor.stop()
        # print('505: D={0}, angle+3={1}'.format(gyro_sensor.angle(), angle+3))
    elif turnType == 2:
        if gyro_sensor.angle()<angle:
            # print('in 536')
            while gyro_sensor.angle()<angle:
                left_motor.run(turnSpeed/2)
                right_motor.run(turnSpeed/-2)  
            # print('540: Degree={0}  :'.format(gyro_sensor.angle()))
            right_motor.hold()
            left_motor.hold()
        else:
            # print('in 544')
            while gyro_sensor.angle()>angle:
                # print('546: D={0}:  '.format(gyro_sensor.angle()))
                right_motor.run(turnSpeed/2)
                left_motor.run(turnSpeed/-2)
            # print('549: Degree={0}  :'.format(gyro_sensor.angle()))
            right_motor.hold()
            left_motor.hold()
    
    print('Turn_Finished,Gyro_sensor.angle={0}, Robot_distance={1}'.format(gyro_sensor.angle(), robot.distance()))
    wait(200)
    
    # last_distance = robot.distance()
    # print('At Last Distance={0}'.format(robot.distance()))
    # error = last_distance-init_distance
    # # robot.straight(-1 * error)
    # print(error)

def turn(angle, turnType=1, turnSpeed=520):
    robot.stop()
    # init_distance = robot.distance()
    # print('At first Distance={0}'.format(robot.distance()))
    robot.settings(straight_speed=0, straight_acceleration=0, turn_rate=turnSpeed, turn_acceleration=200)
    if turnType == 1:
        if gyro_sensor.angle()<angle-3:
            while gyro_sensor.angle()<angle:
                right_motor.run(turnSpeed)
            left_motor.stop()
        else:
            while gyro_sensor.angle()>angle+3:
                left_motor.run(turnSpeed)
            right_motor.stop()
        # print('505: D={0}, angle+3={1}'.format(gyro_sensor.angle(), angle+3))
    elif turnType == 2:
        if gyro_sensor.angle()<angle:
            # print('in 536')
            while gyro_sensor.angle()<angle:
                left_motor.run(turnSpeed/2)
                right_motor.run(turnSpeed/-2)  
            # print('540: Degree={0}  :'.format(gyro_sensor.angle()))
            right_motor.hold()
            left_motor.hold()
        else:
            # print('in 544')
            while gyro_sensor.angle()>angle:
                # print('546: D={0}:  '.format(gyro_sensor.angle()))
                right_motor.run(turnSpeed/2)
                left_motor.run(turnSpeed/-2)
            # print('549: Degree={0}  :'.format(gyro_sensor.angle()))
            right_motor.hold()
            left_motor.hold()
    
    print('Turn_Finished,Gyro_sensor.angle={0}, Robot_distance={1}'.format(gyro_sensor.angle(), robot.distance()))
    wait(200)
    
    # last_distance = robot.distance()
    # print('At Last Distance={0}'.format(robot.distance()))
    # error = last_distance-init_distance
    # # robot.straight(-1 * error)
    # print(error)

def turn_angle_1001(angle, speed=150):
    # angle = -90 # degrees
    # speed = 150 # mm/s
    robot.stop()
    robot.settings(straight_speed=0, straight_acceleration=0, turn_rate=speed, turn_acceleration=200)
    gyro_sensor.reset_angle(0)
    if angle < 0:
        while gyro_sensor.angle() > angle:
            right_motor.run(speed=(-1 * speed))
            left_motor.run(speed=speed)
            wait(10)
    elif angle > 0:  
        while gyro_sensor.angle() < angle:
            right_motor.run(speed=speed)
            left_motor.run(speed=(-1 * speed))
            wait(10)  
    else:
        print("Error: no angle chosen")

    left_motor.hold()
    right_motor.hold()
    wait(100)
    robot.stop()
    robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)

def turn_angle_0929(angle, speed=150):
    # angle = -90 # degrees
    # speed = 150 # mm/s
    robot.stop()
    robot.settings(straight_speed=0, straight_acceleration=0, turn_rate=speed, turn_acceleration=200)
    # gyro_sensor.reset_angle(0)
    if angle < 0:
        while gyro_sensor.angle() > angle:
            left_motor.run(speed=(-1 * speed))
            right_motor.run(speed=speed)
            wait(10)
    elif angle > 0:  
        while gyro_sensor.angle() < angle:
            left_motor.run(speed=speed)
            right_motor.run(speed=(-1 * speed))
            wait(10)  
    else:
        print("Error: no angle chosen")

    left_motor.hold()
    right_motor.hold()
    wait(1000)
    robot.stop()
    robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)

def fulsh_gyro():
    my_sensor = Ev3devSensor(Port.S4)
    for i in range(5): # At first 6 times loop

        # wait(200)
        wait(2)
        # print(my_sensor.read('GYRO-FAS'))
        # print(my_sensor.read('GYRO-RATE'))
        print(my_sensor.read('GYRO-G&A'))
        # my_sensor.read()
    # print(my_sensor.read('GYRO-CAL'))
    # wait(1000)
    print(my_sensor.read('GYRO-ANG'))
    # wait(1000)
    print('772')
    gyro_sensor = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
    for i in range(5):
        print(gyro_sensor.angle())
        gyro_sensor.reset_angle(0)  


def compass(angle, distance, speed=70):
    initial_angle = angle
    # print('777')
    old_degree = gyro_sensor.angle()
    # fulsh_gyro()
    # for i in range(5):
    #     print(gyro_sensor.angle())
    #     gyro_sensor.reset_angle(0) 

    robot.reset()

    robot.stop()
    robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
    # robot.settings(straight_speed=10, straight_acceleration=10, turn_rate=182, turn_acceleration=792)
    # robot.distance_control.limits(speed=650, acceleration=35, actuation=100)
    # robot.heading_control.limits(speed=650, acceleration=35, actuation=100)
    # robot.heading_control.target_tolerances(position=0)
    # robot.distance_control.target_tolerances(position=0)

    print('iniial_angle = {0}'.format(initial_angle))
    print('Old_degree = {0}'.format(old_degree))
    print('The new angle={0}'.format(gyro_sensor.angle()))
    ### The following is the PID drive Gyro
    # Kp=10.8; Ki=0.07534795236181951; Kd=387.0045447283584; 
    Ts= speed
    Kp=11; Ki=0; Kd=0;
    # Kp=5.399999999999999; Ki=0.0001506896893501282; Kd=48377.56339826046;
    # Kp=5.888; Ki=0.006342179493713379; Kd=595.8733908029614; 
    Td = distance # target distance
    # Ts = 50 # target speed of robot in mm/s
    # Kp = 3 #  the Constant 'K' for the 'p' proportional controller

    integral = 0 # initialize
    # Ki = 0.025 #  the Constant 'K' for the 'i' integral term

    derivative = 0 # initialize
    lastError = 0 # initialize
    # Kd = 3 #  the Constant 'K' for the 'd' derivative term
    # print(gyro_sensor.angle())
    while (abs(robot.distance()) < Td):
        error = gyro_sensor.angle() - angle# proportional 
        
        if (error == 0):
            integral = 0
        else:
            integral = integral + error    
        
        derivative = error - lastError  
        
        correction = (Kp*(error) + Ki*(integral) ++ Kd*derivative) * -1
        
        robot.drive(Ts, correction)

        lastError = error
    
    robot.stop()
    robot.settings(straight_speed=150, straight_acceleration=35, turn_rate=120, turn_acceleration=35)
    # gyro_sensor.reset_angle(initial_angle) #go back to the orighianl degree
    # print('833')
    # print(gyro_sensor.angle())

#there will two different turn Type, 1=The first is one wheel to fixed. and another wheel to turn specifical "angle"degree
# the second turnType==2 means two wheel move together, one move forward another move backward.
def turn_old(angle, turnType=1, turnSpeed=180):
    robot.stop()
    if turnType == 1:
        if gyro_sensor.angle()<angle-3:
            while gyro_sensor.angle()<angle:
                left_motor.run(turnSpeed)
            left_motor.stop()
        else:
            while gyro_sensor.angle()>angle+3:
                right_motor.run(turnSpeed)
            right_motor.stop()
    elif turnType == 2:
        if gyro_sensor.angle()<angle:
            while gyro_sensor.angle()<angle-3:
                left_motor.run(turnSpeed/2)
                right_motor.run(turnSpeed/-2)
            right_motor.stop()
            left_motor.stop()
        else:
            while gyro_sensor.angle()>angle+3:
                right_motor.run(turnSpeed/2)
                left_motor.run(turnSpeed/-2)
            right_motor.stop()
            left_motor.stop()



#There is a special color sensor on the robot to Detected the color.
#When detetcor the color. the robot will stop to move.
# ? How to transfer the colorSensor, Whether left or right is OK
def colorChecker(color):
    colornotDetected = True
    while colornotDetected:
        print('robot.turn(3)')
        # right_motor.run(200)
        # left_motor.run(200)
        robot.turn(3)
        # if colorDetector.color() == color:
        if left_color_sensor.color() == color:
            colornotDetected = False
            print('change the colornotdetect')
    # right_motor.stop()
    # left_motor.stop()
    # robot.stop()


#Wait until center button to be pressed.
def button():
    while True:
        pressed = Button.CENTER in ev3.buttons.pressed()
        robot.stop()
        if pressed:
            break


def Show_Screen():
    # ev3.screen.set_font(big_font)
    while True:
        # ev3.screen.print(gyro_sensor.speed())
        # We can't use speed and angle at the same time
        # When calibrate the sensor,you can not use gyro-angle,speed. at the same time
        # calibreate the Gyro. you should make the robot stop completed.
        ev3.screen.print(gyro_sensor.angle())
        ev3.screen.print(robot.distance())
        ev3.screen.print(robot.angle())
        ev3.screen.print(robot.state())
        # ev3.screen.print(lift_motor.angle())
        # ev3.screen.print(fork_motor.angle())


        # When I use this. The motor alwasys sharker continues
        # ev3.screen.print('fork_m:{0}'.format(fork_motor.angle()))
        # ev3.screen.print('lift_m:{0}'.format(lift_motor.angle()))

        # ev3.screen.print(left_color_sensor.reflection())
        # ev3.screen.print(left_color_sensor.rgb())

        # ev3.screen.print(right_color_sensor.reflection())
        # ev3.screen.print(right_color_sensor.rgb())

        # ev3.screen.print(back_color_sensor .reflection())
        # ev3.screen.print(back_color_sensor .rgb())


        # ev3.screen.print(color_sensor.read('RGB-RAW'))
        # ev3.screen.print(sensor.read('GYRO-ANG'))
        # ev3.screen.print(30, 30, robot.angle())
        # ev3.screen.print(WHITE_REFLECT_L)
        # ev3.screen.print(BLACK_REFLECT_L)
        # ev3.screen.print(HALF_VLAUE_L)
        # ev3.screen.print(WHITE_REFLECT_R)
        # ev3.screen.print(BLACK_REFLECT_R)
        # ev3.screen.print(HALF_VLAUE_R)
        # ev3.screen.print(40, 40, robot.distance())
        # ev3.screen.print(40, 40, robot.distance())
        # r, g, b = color_sensor.read('RGB-RAW')
        # ev3.screen.print(r)
        # ev3.screen.print(g)
        # ev3.screen.print(b)
        wait(10)
        ev3.screen.clear()


def Lift_up():
    lift_motor.run_angle(speed=-250, rotation_angle=900, then=Stop.HOLD, wait=False)

def Lift_down():
    lift_motor.run_angle(speed=250, rotation_angle=900, then=Stop.HOLD, wait=False)


