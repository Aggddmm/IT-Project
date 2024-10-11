# Code written in Python 2.7
# should cd to the directory where the SDK is located when running this code

# Change Me:
SDK_ABS_PATH = "/home/aggddmm/Downloads/SDK"

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
    
    # Speech Recognition
    def get_speech_recognition_proxy(self):
        return self.connect("ALSpeechRecognition")
    
    def get_language_avail(self):
        proxy = self.connect("ALSpeechRecognition")
        return str(proxy.getAvailableLanguages())
    
    # Behavior Management, code by MUMU47
    def start_behavior(self, behavior_name):
        behavior_manager = self.connect("ALBehaviorManager")
        if behavior_manager:
            if behavior_manager.isBehaviorInstalled(behavior_name):
                if not behavior_manager.isBehaviorRunning(behavior_name):
                    print("[*] Starting behavior:", behavior_name)
                    behavior_manager.startBehavior(behavior_name)
                else:
                    print("[!] Behavior is already running:", behavior_name)
            else:
                print("[!] Behavior not installed:", behavior_name)
    
    def stop_behavior(self, behavior_name):
        behavior_manager = self.connect("ALBehaviorManager")
        if behavior_manager:
            if behavior_manager.isBehaviorRunning(behavior_name):
                print("[*] Stopping behavior:", behavior_name)
                behavior_manager.stopBehavior(behavior_name)
            else:
                print("[!] Behavior is not running:", behavior_name)
                
    def get_all_behaviors(self):
        behavior_manager = self.connect("ALBehaviorManager")
        if behavior_manager:
            return behavior_manager.getInstalledBehaviors()
        else:
            return None


# test codes (main function)
import time
def main():
    # Set the IP address and port number to the physical robot
    ip_addr = "127.0.0.1"
    port_remote = 9559
    robotInstance = Robot(ip_addr, port_remote)
    # API calls.
    
    # TODO: speed of speech adjustment (too fast) **Tested**
    robotInstance.say("do you like me if im nothing but a robot? even if i have no feelings? even if i have no soul? even if i have no heart?")
    
    print(type(robotInstance.get_all_behaviors()))


if __name__ == "__main__":
    main()
    
# behavior manager test code by MUMU47
# # Replace with your behavior name as seen in Choregraphe
# behavior_name = "new/Go to position Nod"

# # Start the behavior
# robot.start_behavior(behavior_name)

# # Optionally, you can stop the behavior after some time
# # import time
# # time.sleep(5)
# # robot.stop_behavior(behavior_name)
