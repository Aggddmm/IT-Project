
# IT Project Report Skeleton

### Design Graph Link
    https://unimelbcloud-my.sharepoint.com/:u:/g/personal/peihongl_student_unimelb_edu_au/Ee1CcKK7F25OvqqulfCpuGEBpLTNOVXbd5Po1QQnEMrUHg

### IDK what else to put here... (maybe shared word document?)

### 1. **System Architecture Overview**

The System Architecture Overview provides a high-level view of the entire system, explaining how each component fits together and interacts within the "Wise Sage Robot" project.

#### **Components to Include:**

1. **Architecture Diagram**:
   - **Hardware Layer**: 
     - NAO H25 V6 robot, highlighting key hardware components such as cameras, microphones, tactile sensors, and actuators (motors).
   - **Software Control Layer**:
     - Operating system and middleware that manage robot hardware.
     - Control software modules responsible for motion control, sensor data processing, and communications.
   - **Communication Interfaces**:
     - Details on how the robot connects to external systems, such as Wi-Fi, Ethernet, or Bluetooth.
     - Data flow between the robot and any cloud-based services or external databases.
   - **User Interaction Layer**:
     - Components for voice recognition, image processing, and user input handling.
     - Interface through which users interact with the robot, including the special glasses.
   - **Data Processing and Storage Layer**:
     - Local storage on the robot for temporary data caching.
     - Remote storage (e.g., cloud or external database) for persistent data, such as user interaction history and the wisdom database.

2. **Component Relationships**:
   - Describe how each component within the architecture interacts.
   - Define the flow of information between hardware components (e.g., how sensor data is transmitted to the processing units).
   - Explain the interaction between software layers (e.g., how the speech recognition module communicates with the dialogue generation module).

3. **Data Flow Diagram**:
   - **User Input to Response Flow**: Diagram showing how user input (voice, objects) is processed from the moment it is detected by the robot's sensors until a response is generated and delivered (e.g., audio output or gesture).
   - **NAO to Cloud Flow**: Outline how data that needs to be processed or stored in the cloud is transmitted, processed, and retrieved.

4. **Subsystem Overview**:
   - Brief descriptions of major subsystems (e.g., movement control, audio processing, visual recognition) and their roles within the architecture.
   - Explanation of how these subsystems integrate to create the overall system behavior.

### 2. **Component Design Document**

The Component Design Document offers a detailed breakdown of each system component, including its functionality, design, and implementation.

#### **Components to Include:**

1. **Hardware Components**:
   - **NAO H25 V6 Robot**:
     - **Cameras**: Specifications and roles of the front and rear cameras; how they are used for object recognition and user interaction.
     - **Microphones**: Directional microphones for capturing voice input, including noise reduction techniques.
     - **Tactile Sensors**: Placement and purpose of tactile sensors, such as detecting user touches on the head or arms.
     - **Actuators**: Details of the actuators that control the robot’s movement, including joint motors for head, arms, and other relevant parts.

2. **Software Components**:
   - **Motion Control Module**:
     - **Action Planning**: Algorithms and pre-defined sequences for generating and executing movements (e.g., nodding, hand gestures).
     - **Motor Control**: API details for controlling robot’s joints and executing planned movements.
   - **Speech Recognition Module**:
     - **Keyword Detection**: Techniques for recognizing specific keywords in user speech that trigger responses.
     - **Natural Language Processing (NLP)**: Integration of NLP tools to parse and understand user queries.
   - **Image Processing Module**:
     - **Special Glasses Recognition**: Algorithms for detecting and identifying the special glasses worn by users.
     - **Object Recognition**: Processes for identifying objects presented by users and linking them to relevant knowledge in the database.
   - **Dialogue Generation Module**:
     - **Dialogue Framework**: Structure for managing conversational state and context to maintain coherence in interactions.
     - **Text-to-Speech (TTS)**: Description of the TTS engine used for converting generated text into speech output.
   - **User Interaction Module**:
     - **Interaction Trigger**: How interactions are initiated when a user wearing the special glasses enters the robot’s field of view.
     - **Feedback Mechanisms**: Methods for providing visual or auditory feedback to users during interaction.

3. **Integration Components**:
   - **Data Handling**:
     - **Data Flow**:
       - **Sensors to Processing Units**: The robot uses a camera and microphone to detect and recognize faces, objects, and spoken words. The sensor data is captured in real time and sent to the CPU for analysis. The camera captures visual input like faces, objects, while the microphone captures audio input such as spoken words or phrases.
       - **Processing Units to Output Modules**: After the data is processed by the CPU—identifying objects or recognizing speech—the robot generates appropriate responses. These responses are then sent to output modules such as the speech synthesis module (to speak advice or proverbs) and the motor control module (to initiate subtle hand movements or nodding).
     - **Data Buffering**:
       - **Real-Time Processing**: Sensor data, such as live camera feed and audio input, is temporarily buffered to ensure real-time processing. For instance, frames from the camera are buffered momentarily to allow facial or object recognition algorithms to operate. Similarly, audio data is buffered in small chunks to enable continuous speech recognition.
       - **Handling Delays**: To manage any processing delays, a circular buffer is used to ensure that the most recent data is always available while older, irrelevant data is discarded. This allows the system to respond quickly and accurately to user interactions without significant lag.
   - **Middleware**:
     - **API Definitions**:
       - **Camera API**: Provides interfaces for initializing the camera, capturing frames, and retrieving real-time video feeds. It also includes functions for adjusting camera settings based on different lighting conditions.
       - **Audio Input API**: Offers functions for capturing audio from the robot's microphone, processing the audio for noise reduction, and passing the data to the speech recognition module.
       - **Facial and Object Recognition API**: Contains methods for detecting and identifying faces and objects within the camera feed. It can return metadata such as object type, position, and confidence level.
       - **Speech Synthesis API**: Facilitates converting text to speech, with options to adjust tone, pitch, and speed to achieve a calm and deliberate speaking style.
       - **Motor Control API**: Provides methods to control the robot's hand movements, nodding actions, and other gestures to portray thoughtful stances and emphasize the robot's advice.
       - **Data Communication API**: Middleware API that handles data exchange between different components (e.g., sensor data to processing unit, processing results to output modules). It ensures reliable and efficient communication, using message queuing or a publish-subscribe model.
4. **User Interaction Design**:
   - **Interaction Flow**:
     - **User Approach**: When a user approaches the robot, the proximity sensor triggers the system to initiate interaction mode. The camera begins facial recognition, and the microphone activates to capture any spoken input.
       - **Recognition and Greeting**: Upon recognizing a user (either by face or voice), the robot gently nods and greets the user with a calm welcome message, inviting them to seek wisdom or ask for advice.
     - **Interaction Engagement**:
       - **User Input**: The user may speak a question or present an object to the camera. The audio input is processed by the speech recognition module, while the visual input is processed by the object recognition module.
       - **Processing and Response**: Based on the recognized input (face, object, or spoken words), the robot's CPU selects an appropriate response from its database of wisdom or proverbs. For example, if a book is recognized, the robot might say, "Knowledge is the path to wisdom, and every book is a step along that journey."
       - **Output Delivery**: The selected response is delivered through the speech synthesis module, and accompanying gestures are performed by the robot's hands or head to emphasize the message.
     - **End of Interaction**: After providing a response, the robot waits for further input. If no further input is detected for a set period, the robot gently nods and returns to an idle state, waiting for the next user.
   - **Error Handling**:
     - **Unclear or Unrecognized Input**:
       - **Fallback Strategies**: If the robot fails to recognize the user’s input (either audio or visual), it responds with a polite prompt, such as “I’m sorry, I didn’t quite catch that. Could you please repeat?” This encourages the user to try again without frustration.
       - **Repeat Prompt Limitation**: To avoid infinite loops, the robot is programmed to limit the number of unrecognized attempts. After three failed attempts, it says, "I may not understand everything, but I’m here to help however I can," and returns to an idle state.
     - **System Errors**:
       - **Hardware Malfunctions**: If any hardware component (camera, microphone, motor) fails, the middleware API generates an error message, and the robot speaks, "I am experiencing a temporary issue. Please bear with me." The system logs the error for further diagnostics.
       - **Data Processing Errors**: In case of data processing failures (e.g., speech recognition errors due to noise), the robot asks the user to repeat or try again in a quieter environment.


### 3. **Data Architecture Document**

### Database ER Diagram


+----------------------------------------+
|               Robot                    |
|----------------------------------------|
| Robot_ID PK     | int                  |
| Name            | varchar(255)         |
| Hardware_Specs  | text                 |
| Software_Version| varchar(50)          |
+----------------------------------------+

  |
  |
  has
  |
  v

+----------------------------------------+
|           Audio-sensors                |
|----------------------------------------|
| Sensor_ID PK   | int                   |
| Robot_ID FK    | int                   |
| Type           | varchar(50)           |
| Location       | varchar(100)          |
| Status         | varchar(50)           |
+----------------------------------------+

  |
  |
  captures
  |
  v

+----------------------------------------+
|           Sensor_Data                  |
|----------------------------------------|
| Data_ID PK      | int                  |
| Sensor_ID FK    | int                  |
| Timestamp       | datetime             |
| Data_Type       | varchar(50)          |
| Data_Value      | text                 |
+----------------------------------------+

  |
  |
  processed by
  |
  v

+----------------------------------------+
|           Processing_Unit              |
|----------------------------------------|
| Unit_ID PK       | int                 |
| Sensor_Data_ID FK| int                 |
| Type             | varchar(50)         |
| Status           | varchar(50)         |
+----------------------------------------+

  |
  |
  sends data to
  |
  v

+----------------------------------------+
|           Output_Modules               |
|----------------------------------------|
| Module_ID PK      | int                |
| Processing_Unit_ID FK | int            |
| Type              | varchar(50)        |
| Status            | varchar(50)        |
+----------------------------------------+

  |
  |
  generates
  |
  v

+----------------------------------------+
|           Robot_Responses              |
|----------------------------------------|
| Response_ID PK    | int                |
| Output_Module_ID FK | int              |
| Response_Type     | varchar(50)        |
| Content           | text               |
| Timestamp         | datetime           |
+----------------------------------------+


+----------------------------------------+
|           Robot_Actions                |
|----------------------------------------|
| Action_ID PK      | int                |
| Robot_ID FK       | int                |
| Type              | varchar(50)        |
| Location          | varchar(100)       |
| Status            | varchar(50)        |
+----------------------------------------+

+----------------------------------------+
|               Users                    |
|----------------------------------------|
| User_ID PK        | int                |
| Name              | varchar(100)       |
| Profile_Data      | text               |
| Interaction_History | text             |
+----------------------------------------+

  |
  |
  uses
  |
  v

+----------------------------------------+
|             Audio_output               |
|----------------------------------------|
| Audio_ID PK      | int                 |
| User_ID FK       | int                 |
| Type             | varchar(50)         |
| Status           | varchar(50)         |
+----------------------------------------+


+----------------------------------------+
|           Wisdom_Database              |
|----------------------------------------|
| Quote_ID PK       | int                |
| Remote_Server_ID FK | int              |
| Content           | text               |
| Mood              | varchar(50)        |
| Associated_Action | varchar(100)       |
+----------------------------------------+


The Data Architecture Document focuses on how data is structured, stored, and processed within the system, ensuring that the robot can efficiently manage user interactions and knowledge.

Ideally, our robot should be able to understand what people say to it and generate intelligent responses using our AI system. That’s the perfect scenario we're aiming for. But if the voice recognition isn't quite up to par, we’ve got a backup plan. We’ve set up a database filled with hundreds of famous quotes. If needed, the robot can pick an appropriate quote from this database to respond with.

Each quote in this database comes with two extra attributes: a mood and an action. So, when the robot, NOVA6, decides what it’s going to say, it will also perform an action that reflects the mood of the quote. This way, even if the robot can’t fully grasp or process a conversation, it will still be able to interact in a meaningful and expressive way.


### 4. **API Design Document**

APIs in this system are primarily used for data exchange between Robots and process backend, and setting states for the robot.

<div style="text-align: center;">
<img src="Images/Architecture_Overview.png" style="align-self: center;"></br>Architecture Overview</img>
</div>

#### **Components to Include:**

1. **Hardware APIs**:
   - **Robot Control API**:
     - **Motor Control**: API endpoints for controlling robot movements, including specifications for motion commands like “nod,” “wave,” or “point.”
     - **Sensor Data Access**: APIs for accessing real-time data from the robot’s sensors (e.g., camera feed, microphone input, tactile sensor states).
   - **Communication API**:
     - **Network Communication**: Endpoints for establishing and maintaining connections between the robot and remote servers or databases.

2. **Software APIs**:
   - **Speech Recognition API**:
     - **Voice Input Handling**: API for passing raw audio data to the speech recognition module and receiving transcribed text.
     - **Keyword Detection**: Endpoints for identifying and reacting to specific keywords within the audio data.
   - **Image Processing API**:
     - **Glasses Recognition**: API for detecting the special glasses and identifying the wearer.
     - **Object Recognition**: API for processing images and identifying objects presented by the user.
   - **Dialogue Generation API**:
     - **Text Response Generation**: API for generating textual responses based on user input and context.
     - **TTS Output**: API for converting text into speech and playing it through the robot’s speakers.

3. **External Integration APIs**:
   - **Knowledge Database API**:
     - **Data Retrieval**: Endpoints for querying the wisdom database and retrieving appropriate advice or sayings based on user input.
     - **Data Ingestion**: API for updating or expanding the wisdom database with new entries.
   - **User Data Management API**:
     - **User Profile Access**: API for retrieving and updating user profiles, including interaction history and preferences.

4. **Error Handling and Logging**:
   - **API Error Codes**: Standardized error codes for handling and diagnosing API failures or unexpected behavior.
   - **Logging API**: API for logging API requests and responses, useful for debugging and performance monitoring.

5. **Security and Authentication**:
   - **API Authentication**: Methods for authenticating API requests, ensuring that only authorized components can interact with the system.
   - **Data Protection**: Strategies for protecting data accessed or

 transmitted through APIs, including encryption and secure tokens.

### 5. **Deployment Architecture Document**

The Deployment Architecture Document outlines the strategies for deploying the system, ensuring it runs efficiently and can be maintained over time.

#### **Components to Include:**

1. **Hardware Deployment**:
   - **NAO Robot Setup**:
     - **Initial Configuration**: Step-by-step guide for setting up the NAO H25 V6 robot, including calibration of sensors and actuators.
     - **Network Configuration**: Instructions for connecting the robot to the local network, including Wi-Fi setup and IP address assignment.
     - **Power Management**: Recommendations for managing the robot’s power supply, including battery maintenance and charging cycles.

2. **Software Deployment**:
   - **Local Software Installation**:
     - **Operating System**: Details on the robot’s operating system setup, including required libraries and dependencies.
     - **Application Software**: Procedures for deploying and configuring the control software, including installation of motion control, speech recognition, and image processing modules.
   - **Remote Server Configuration**:
     - **Cloud Services Setup**: Instructions for setting up cloud services (e.g., AWS, Azure) for data processing, storage, or additional computational tasks.
     - **Database Deployment**: Steps for deploying and configuring the remote database that stores user data and the knowledge database.

3. **CI/CD Pipeline**:
   - **Version Control**:
     - **Repository Setup**: Guidelines for setting up and managing the project’s codebase in a version control system (e.g., Git).
     - **Branching Strategy**: Recommended practices for branching, merging, and version tagging in the development process.
   - **Automated Testing**:
     - **Test Suites**: Descriptions of automated test suites for unit testing, integration testing, and system testing.
     - **Continuous Integration**: Setup of CI tools (e.g., Jenkins, GitHub Actions) to automatically run tests and deploy updates to the robot or remote servers.
   - **Deployment Automation**:
     - **Deployment Scripts**: Scripts for automating the deployment process, reducing manual intervention and ensuring consistency across environments.
     - **Rollback Procedures**: Steps for reverting to previous versions in case of deployment failures or critical issues.

4. **Monitoring and Maintenance**:
   - **System Monitoring**:
     - **Real-Time Monitoring**: Tools and techniques for monitoring the robot’s health, including CPU usage, memory usage, and network connectivity.
     - **Performance Metrics**: Key performance indicators (KPIs) to monitor, such as response time, accuracy of recognition modules, and uptime.
   - **Logging and Analytics**:
     - **Log Management**: Strategies for collecting, storing, and analyzing logs generated by the robot and associated services.
     - **Anomaly Detection**: Methods for detecting and responding to anomalies in the system, such as unexpected behavior or performance degradation.
   - **Software Updates**:
     - **OTA (Over-the-Air) Updates**: Process for deploying software updates remotely, ensuring the robot’s software stays up to date with minimal disruption.
     - **Patch Management**: Procedures for applying patches to fix bugs, security vulnerabilities, or performance issues.

5. **Security and Compliance**:
   - **Security Configurations**:
     - **Firewall Setup**: Guidelines for configuring firewalls and other security measures to protect the robot and associated servers from unauthorized access.
     - **Data Encryption**: Implementation of encryption for data storage and transmission to safeguard sensitive information.
   - **Compliance Standards**:
     - **Data Protection Regulations**: Ensuring compliance with data protection regulations (e.g., GDPR) relevant to user data and interaction logs.
     - **Audit and Reporting**: Setting up processes for regular audits and generating compliance reports to demonstrate adherence to relevant standards.
