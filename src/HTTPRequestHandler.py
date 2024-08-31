from flask import Flask, jsonify, request
from robotConnect import Robot

# Constants
IP_TITLE = "ip"
PORT_TITLE = "port"
MESSAGE_TITLE = "message"
ERROR_TITLE = "error"

# Global vatiables 
robotIP = ""
robotPort = 0
remoteRobot = None
isDebug = False
serverPort = 5000

# Initialize the Flask application
app = Flask(__name__)

def runServer(debug=False, port=5000):
    global isDebug
    global serverPort
    isDebug = debug
    serverPort = port
    
    app.run(debug=debug, port=port)

@app.route('/checkConnection', methods=['GET'])
def api():
    # Return a JSON response
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

# Run the app when the script is executed
if __name__ == '__main__':
    # Enable debug mode and set the port
    runServer(debug=True, port=5000)