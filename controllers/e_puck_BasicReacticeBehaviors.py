"""
    e_puck_BasicReacticeBehaviors controller.
    Author: Dominik Żurek - Poland

    This controller was developed as part of my coursework for the "Introduction to Robotics with Webots" - Basic Robotics Behaviors and Odometry
    Specialization on Coursera from University of Colorado Boulder.
    LINK: https://www.coursera.org/specializations/introduction-robotics-webots

    What this code does:
        The robot drives forward to the first obstacle (O1), detects it, and turns 180 degrees. 
        Then, it drives forward to the second obstacle (O2), turns right, and drives along 
        its edge until it passes the corner, then stops completely.
    
    Steps: 
        0: Drive forward until O1 obstacle is detected
        1: Turn 180 from O1 obstacle
        2: Drive forward until O2 obstacle is detected
        3: Turn right from O2 obstacle
        4: Drive forward until losing track of O2 obstacle
"""

from controller import Robot

# CONSTANTS
SEPARATOR_LINE = "-" * 55
MAX_VELOCITY = 6.28
SLOWDOWN_VELOCITY = 0.5
TURN_AROUND_VELOCITY = MAX_VELOCITY * 0.5
TIME_STEP_TO_ROTATE = 47
TIME_STEP_TO_TURN_RIGHT = 24

# Sensor Thresholds
FRONT_SLOWDOWN_THRESHOLD = 70
FRONT_STOP_THRESHOLD = 100
REAR_ALIGN_THRESHOLD = 82.2
LEFT_WALL_ALIGN_THRESHOLD = 115
LEFT_WALL_LOST_THRESHOLD = 70

# Initialize Webots E-Puck:
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Initialize motors:
motor_left, motor_right = robot.getDevice('left wheel motor'), robot.getDevice('right wheel motor')
motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))
print(f"{SEPARATOR_LINE}\nMotors are ready to start.")

# Initialize sensors:
distance_sensors = []
for i in range(8):
    distance_sensors.append(robot.getDevice('ps' + str(i)))
    distance_sensors[-1].enable(timestep)
print(f"All sensors are enabled.\n{SEPARATOR_LINE}")

# Start task:
current_step = 0
turn_step = 0
print("Robot driving forward until O1 is detected...")

while robot.step(timestep) != -1:

    # 0: Drive forward until O1 obstacle is detected
    if current_step == 0:
        # Read distance from front sensors
        front_right_sensor = distance_sensors[0].getValue()
        front_left_sensor = distance_sensors[7].getValue()
        
        # Sequence
        if front_left_sensor < FRONT_SLOWDOWN_THRESHOLD or front_right_sensor < FRONT_SLOWDOWN_THRESHOLD:
            motor_left.setVelocity(MAX_VELOCITY)
            motor_right.setVelocity(MAX_VELOCITY)

        elif front_left_sensor < FRONT_STOP_THRESHOLD or front_right_sensor < FRONT_STOP_THRESHOLD:
            motor_left.setVelocity(SLOWDOWN_VELOCITY)
            motor_right.setVelocity(SLOWDOWN_VELOCITY)

        else:
            motor_left.setVelocity(0)
            motor_right.setVelocity(0)
            print("Robot is five cm away from O1 obstacle.\nTurning around....")
            current_step = 1
            

    # 1: Turn 180 from O1 obstacle      
    elif current_step == 1:

        # Read distance from rear sensors
        rear_right_sensor = distance_sensors[3].getValue()
        rear_left_sensor = distance_sensors[4].getValue()

        # Sequence
        if turn_step < TIME_STEP_TO_ROTATE:
            motor_left.setVelocity(-TURN_AROUND_VELOCITY)
            motor_right.setVelocity(TURN_AROUND_VELOCITY)
            turn_step += 1

        else:
            motor_left.setVelocity(-TURN_AROUND_VELOCITY * 0.04)
            motor_right.setVelocity(TURN_AROUND_VELOCITY * 0.04)

            if rear_left_sensor > REAR_ALIGN_THRESHOLD and rear_right_sensor > REAR_ALIGN_THRESHOLD:
                print("Turning finished.\nDrive forward until O2 obstacle is detected...")
                turn_step = 0
                current_step = 2
        
    
    # 2: Drive forward until O2 obstacle is detected
    elif current_step == 2:
        # Read distance from front sensors
        front_right_sensor = distance_sensors[0].getValue()
        front_left_sensor = distance_sensors[7].getValue()
        
        # Sequence
        if front_left_sensor < FRONT_SLOWDOWN_THRESHOLD or front_right_sensor < FRONT_SLOWDOWN_THRESHOLD:
            motor_left.setVelocity(MAX_VELOCITY)
            motor_right.setVelocity(MAX_VELOCITY)

        elif front_left_sensor < FRONT_STOP_THRESHOLD or front_right_sensor < FRONT_STOP_THRESHOLD:
            motor_left.setVelocity(SLOWDOWN_VELOCITY)
            motor_right.setVelocity(SLOWDOWN_VELOCITY)

        else:
            current_step = 3
            motor_left.setVelocity(0)
            motor_right.setVelocity(0)
            print("Robot is five cm away from O2 obstacle.\nTurning right...")

    # 3: Turn right from O2 obstacle        
    elif current_step == 3:
        # Read data from left sensor
        left_sensor = distance_sensors[5].getValue()

        # Sequence
        if turn_step < TIME_STEP_TO_TURN_RIGHT:
            motor_left.setVelocity(TURN_AROUND_VELOCITY)
            motor_right.setVelocity(-TURN_AROUND_VELOCITY)
            turn_step += 1

        else:
            motor_left.setVelocity(TURN_AROUND_VELOCITY *0.04)
            motor_right.setVelocity(-TURN_AROUND_VELOCITY * 0.04)

            if left_sensor >= LEFT_WALL_ALIGN_THRESHOLD:
                print("Turning finished.\nRobot drive forward along the edge of O2 obstacle...")
                turn_step = 0
                current_step = 4
        
    # 4: Drive forward until losing track of O2 obstacle
    elif current_step == 4:
        # Read data from left sensor
        left_sensor = distance_sensors[5].getValue()
        
        # Sequence
        if left_sensor > LEFT_WALL_LOST_THRESHOLD:
            motor_left.setVelocity(MAX_VELOCITY)
            motor_right.setVelocity(MAX_VELOCITY)

        else:
            motor_left.setVelocity(0)
            motor_right.setVelocity(0)
            turn_step = 0
            print(f"Robot at the edge of O2 obstacle.\n{SEPARATOR_LINE}\nRobot finished the task!\n{SEPARATOR_LINE}")
            break

    # Finish program if current_step <> valid steps     
    else:
        print("Invalid step!")
        break

    pass