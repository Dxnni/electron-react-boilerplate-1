#!/usr/bin/python2.7
import sys
import time

if sys.version_info[0] > 2:
    raise Exception("Python 2 is required.")


from naoqi import ALProxy
robotIP = "10.0.1.19"
if argv[1]
    robotIP = argv[1]

vid = ALProxy("ALVideoRecorder", robotIP, 9559)

#startRecording(folderPath, fileName)
vid.startRecording("/home/nao/recordings/cameras","testVidFeed")

#5 second delay before next command
time.sleep(5.0)

#stopRecording(): [num of recorded frames, absolute file path of vid]
output = vid.stopRecording()

print(output)