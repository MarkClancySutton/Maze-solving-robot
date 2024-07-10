#!/usr/bin/env python3
#Assigment 2 for Mobile Robotics
#Team Members:  Mark Clancy Sutton
#               George Ciobanu
#               Dairary Mabika

# Import the necessary libraries for each of the robots sensors to work
import time
import math
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.button import Button
from ev3dev2.display import *


# Initialize motors and sensors
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)    # Define the drive motors
sonar = UltrasonicSensor(INPUT_2)             # Define the ultrasonic sensor

# Initialize distance variable
distance = sonar.distance_centimeters

#Initialize color variable
color_sensor_in1 = ColorSensor(INPUT_3)

#yellow = start
def yellow():
    x = 1

a =0
# Main loop
while True :

    print(color_sensor_in1.color)

    if color_sensor_in1.color == 4:
        a==1
        
    while a==1:
        yellow()
        # Move forward while the distance is greater than 25cm
        while distance > 20:
         tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(10), 0.5)   # Set motor speed and duration
         distance = sonar.distance_centimeters     # Update distance variable

        # If distance is less than 25cm, take action
        if distance < 20:
            distance = sonar.distance_centimeters     

            # If distance is still less than 25cm, turn right and update distance variable
            if distance < 20:
                tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(25), 1.4)   # Turn right
                distance = sonar.distance_centimeters     

                # If distance is still less than 25cm, turn left, move forward, and update distance variable
                if distance < 20:
                    tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(-25), 1.4)   # Turn left
                    tank_drive.on_for_seconds(SpeedPercent(25), SpeedPercent(25), 0.5)   # Move forward
                    distance = sonar.distance_centimeters     

                    # If distance is still less than 25cm, turn left and update distance variable
                    if distance < 20:
                        tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(-25), 1.4)   # Turn left
                        distance = sonar.distance_centimeters     

        # Stop the motors
        if color_sensor_in1.color == 5:
            print('done')
            tank_drive.on_for_seconds(SpeedPercent(25), SpeedPercent(25), 1)
            tank_drive.on_for_seconds(SpeedPercent(25), SpeedPercent(-25), 10)