#!/usr/bin/python2.7
import sys

if sys.version_info[0] > 2:
    raise Exception("Python 2 is required.")


from naoqi import ALProxy

memory = ALProxy("ALMemory", "10.0.1.133", 9559)
sonar = ALProxy("ALSonar", "10.0.1.133", 9559)

#starts ultrasonic sensor
sonar.subscribe("myApplication")

#gets ultrasonic sensor data. max detection distance is 0.5 meters
left = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
right = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")

#stops ultrasonic sensor
sonar.unsubscribe("myApplication")

print(left)
print(right)