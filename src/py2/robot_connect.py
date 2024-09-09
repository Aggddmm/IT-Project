# Code written in Python 2.7
# should cd to the directory where the SDK is located when running this code

# Change Me:
SDK_ABS_PATH = "/Users/lipeihong/Desktop/IT Project/py2/SDK"

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

# test codes (main function)
import time
def main():
    # Set the IP address and port number to the physical robot
    ip_addr = "192.168.1.106"
    port_remote = 9559
    robotInstance = Robot(ip_addr, port_remote)
    # API calls.
    
    # TODO: speed of speech adjustment (too fast) **Tested**
    robotInstance.say("do you like me if im nothing but a robot? even if i have no feelings? even if i have no soul? even if i have no heart?")
    print(robotInstance.get_language_avail())
    
    # # TODO: apply customized posture to the robot **Tested** "Some posture 100% works (StandInit, LyingBack), some doesn't"
    # print str(robotInstance.getAllBodyPosture())
    # robotInstance.setBodyPosture("LyingBack")
    
    # speech_recon_proxy = robotInstance.get_speech_recognition_proxy()
    # speech_recon_proxy.setLanguage("English")
    # vocabulary = ["yes", "no", "please", "thank you", "hello", "goodbye"]
    # speech_recon_proxy.setVocabulary(vocabulary, False)
    # speech_recon_proxy.subscribe("Test_ASR")
    # print 'Speech recognition engine started'
    # time.sleep(5)
    # speech_recon_proxy.unsubscribe("Test_ASR")
    
    # # get word recognized
    # recognized_word = speech_recon_proxy.getLastWordRecognized()
    # print 'Recognized word: ', recognized_word


if __name__ == "__main__":
    main()