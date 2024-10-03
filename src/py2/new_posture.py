from naoqi import ALProxy

class Robot:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    def connect(self, module):
        try:
            proxy = ALProxy(module, self.ip, self.port)
            print("[*] Connected to", module)
            return proxy
        except Exception as e:
            print("[!] Error:", e)
            return None
    
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

# Example usage
def main():
    # Use localhost and port 9559 for virtual robot
    robot_ip = "127.0.0.1"  # Virtual robot's IP address
    robot_port = 9559  # Default port for virtual robot
    
    robot = Robot(robot_ip, robot_port)
    
    # Replace with your behavior name as seen in Choregraphe
    behavior_name = "new/Go to position Nod"
    
    # Start the behavior
    robot.start_behavior(behavior_name)
    
    # Optionally, you can stop the behavior after some time
    # import time
    # time.sleep(5)
    # robot.stop_behavior(behavior_name)

if __name__ == "__main__":
    main()
