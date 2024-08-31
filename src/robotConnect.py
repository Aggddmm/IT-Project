# Code written in Python 2.7
# should cd to the directory where the SDK is located when running this code

# Change Me:
SDK_ABS_PATH = "/Users/lipeihong/Downloads/pynaoqi-python2.7-2.8.6.23-mac64-20191127_144231"

import sys
sys.path.append(SDK_ABS_PATH + "/lib/python2.7/site-packages")

from naoqi import ALProxy

class Robot:
    ip = ""
    port = 0
    
    # default constructor
    def __init__ (self, ip_addr, port_remote):
        self.ip = ip_addr
        self.port = port_remote
    
    def connect(self, module):
        try:
            proxy = ALProxy(module, self.ip, self.port)
            print "[*] Connected to ", module
            return proxy
        except Exception as e:
            print "[!] Error: ", e
            exit(1)
        
    def say(self, text):
        proxy = self.connect("ALTextToSpeech")
        proxy.say(text)
        
    def getAllBodyPosture(self):
        proxy = self.connect("ALRobotPosture")
        return proxy.getPostureFamilyList()
    
    def setBodyPosture(self, posture):
        postureProxy = self.connect("ALRobotPosture")
        motionProxy = self.connect("ALMotion")
        self.StiffnessOn(motionProxy)
        postureProxy.goToPosture(posture, 5)
        
    def StiffnessOn(self, proxy):
        # We use the "Body" name to signify the collection of all joints
        pNames = "Body"
        pStiffnessLists = 1.0
        pTimeLists = 1.0
        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
            
            
    
# test codes (main function)
def main():
    ip_addr = "127.0.0.1"
    port_remote = 9559
    robotInstance = Robot(ip_addr, port_remote)
    # robotInstance.say("Hello, World!")
    # all_postures = robotInstance.getAllBodyPosture()
    
    # # choose a random index
    # import random
    # rand_num = random.randint(0, len(all_postures) - 1)
    # print "[*] Random Posture: ", all_postures[rand_num]
    # robotInstance.setBodyPosture(all_postures[rand_num])
    robotInstance.setBodyPosture("StandInit")


if __name__ == "__main__":
    main()