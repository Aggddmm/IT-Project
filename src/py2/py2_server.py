from flask import Flask, jsonify, request
from robot_connect import Robot
import requests
import time

# Constants
IP_TITLE = "ip"
PORT_TITLE = "port"
MESSAGE_TITLE = "message"
ERROR_TITLE = "error"
DURATION_TITLE = "time"
GET = "GET"
POST = "POST"
ERROR = -1

# Global vatiables 
robotIP = ""
robotPort = 0
remoteRobot = None
isDebug = False
serverPort = 5000
python3ServerIP = "127.0.0.1"
python3ServerPort = 63121

# Initialize the Flask application
app = Flask(__name__)

def runServer(debug=False, port=5000):
    global isDebug
    global serverPort
    isDebug = debug
    serverPort = port
    app.run(debug=debug, port=port)
    
def connect_server(ip, port, method, api_entry='/checkConnection', data=None):
    if method == GET:
        try:
            respond = requests.get("http://" + ip + ":" + str(port) + api_entry)
        except requests.exceptions.RequestException as e:
            print "[-] Error: ", e
            return ERROR
    if method == POST:
        try:
            respond = requests.post("http://" + ip + ":" + str(port) + api_entry, json=data)
        except requests.exceptions.RequestException as e:
            print "[-] Error: ", e
            return ERROR
    if respond.status_code != 200:
        print "[-] Error: ", respond.status_code
        return ERROR
    return respond

@app.route('/checkConnection', methods=['GET'])
def check_connection():
    return jsonify({MESSAGE_TITLE: "Connection Alive"})

# API Call to Robot Say
@app.route('/robotSay', methods=['POST'])
def robot_say():
    data = request.get_json()

    if data and MESSAGE_TITLE in data:
        # Extract the message
        message = str(data[MESSAGE_TITLE])
        
        global isDebug
        if isDebug:
            print "[+] Message Get From Remote: ", message
        
        if remoteRobot is None:
            return jsonify({ERROR_TITLE: "Please call /setRobotIPPort API First."}), 400
        remoteRobot.say(message)
        return jsonify({MESSAGE_TITLE: message})
    
    else:
        return jsonify({ERROR_TITLE: "Invalid input, expected JSON with 'message' key"}), 400
    
# API Call to Set Remote Robot IP and Port
@app.route('/setRobotIPPort', methods=['POST'])
def set_robot_ip_port():
    # Get the JSON data from the request
    data = request.get_json()

    # Decode JSON
    if data and IP_TITLE in data and PORT_TITLE in data:
        ip = str(data[IP_TITLE])
        port = int(data[PORT_TITLE])
        # Print out
        
        global isDebug
        if isDebug:
            print "[+] IP: ", ip, "Type: ", type(ip)
            print "[+] Port: ", port, "Type: ", type(port)
        # Set the global variables
        global robotIP
        global robotPort
        robotIP = ip
        robotPort = port

        global remoteRobot
        remoteRobot = Robot(robotIP, robotPort)
        return jsonify({MESSAGE_TITLE: "Robot IP and Port Set"})
    else:
        return jsonify({ERROR_TITLE: "Invalid input, expected JSON with 'ip' and 'port' keys"}), 400

@app.route('/py3LMWrapper', methods=['POST'])
def lm_wrapper():
    data = request.get_json()
    if data and MESSAGE_TITLE in data:
        text = str(data[MESSAGE_TITLE])
        
        respond = connect_server(python3ServerIP, python3ServerPort, POST, '/generateText', {MESSAGE_TITLE: text})
        
        if respond == ERROR or ERROR_TITLE in respond.json():
            return jsonify({ERROR_TITLE: "Error!"}), 400
        
        return jsonify({MESSAGE_TITLE: respond.json()[MESSAGE_TITLE]})
    else:
        return jsonify({ERROR_TITLE: "Invalid input, expected JSON with 'message' key"}), 400
        # call

@app.route('/getAllAvailBehavior', methods=['GET'])
def get_all_avail_posture():
    if remoteRobot is None:
        return jsonify({ERROR_TITLE: "Please call /setRobotIPPort API First."}), 400
    return jsonify({MESSAGE_TITLE: remoteRobot.get_all_behaviors()})

@app.route('/startBehavior', methods=['POST'])
def start_behavior():
    data = request.get_json()
    if data and MESSAGE_TITLE in data and DURATION_TITLE in data:
        # Extract the message
        behavior_name = str(data[MESSAGE_TITLE])
        if remoteRobot is None:
            return jsonify({ERROR_TITLE: "Please call /setRobotIPPort API First."}), 400
        # Start the behavior
        remoteRobot.start_behavior(behavior_name)
        return jsonify({MESSAGE_TITLE: "Behavior Started"})
    else:
        return jsonify({ERROR_TITLE: "Invalid input, expected JSON with 'message' key"}), 400

@app.route('/stopBehavior', methods=['POST'])
def stop_behavior():
    data = request.get_json()
    if data and MESSAGE_TITLE in data:
        # Extract the message
        behavior_name = str(data[MESSAGE_TITLE])
        if remoteRobot is None:
            return jsonify({ERROR_TITLE: "Please call /setRobotIPPort API First."}), 400
        # Stop the behavior
        remoteRobot.stop_behavior(behavior_name)
        return jsonify({MESSAGE_TITLE: "Behavior Stopped"})
    else:
        return jsonify({ERROR_TITLE: "Invalid input, expected JSON with 'message' key"}), 400
    
# Run the app when the script is executed
if __name__ == '__main__':
    # Enable debug mode and set the port
    runServer(debug=True, port=26386)
    