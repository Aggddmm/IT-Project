# Code written in Python 2.7
# should cd to the directory where the SDK is located when running this code

# Change Me:
SDK_ABS_PATH = ""

import sys
sys.path.append(SDK_ABS_PATH)

from naoqi import ALProxy

class Robot:
    ip = ""
    port = 0
    proxy = None
    
    # default constructor
    def __init__ (self, ip_addr, port_remote):
        self.ip = ip_addr
        self.port = port_remote
    
    def connect(self):
        try:
            tts = ALProxy("ALTextToSpeech", self.ip, self.port)
            self.proxy = tts
            print("[+] Connected to the remote robot.")
        except Exception as e:
            print("[!] Error: ", e)
            return None
        
    def say(self, text):
        if self.proxy != None:
            self.proxy.say(text)
        else:
            print("[!] Error: Not connected to the remote robot.")
            
            
    
# test codes (main function)
def main():
    ip_addr = "127.0.0.1"
    port_remote = 9559
    sender = Robot(ip_addr, port_remote)
    tts = sender.connect()
    if tts != None:
        tts.say("Hello, world!")
    else:
        print("Failed to connect to the robot.")

if __name__ == "__main__":
    main()