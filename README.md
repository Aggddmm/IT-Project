# AI Model Deployment Project

## Overview
This project highlights a third-year university initiative, developed collaboratively with four group members. We designed and deployed a backend system integrating multiple AI models and the SoftBank NAOqi API. The system aims to answer users' questions using retrieval-augmented generation while providing body feedback through the NAO robot for a more engaging and intuitive interaction experience.

![Project Image](blob:https://brickcarrier.atlassian.net/2b84c6a3-a4b3-41b2-83c6-57992f1a5bb0)

## Features
- Deployment of transformer models for various AI tasks.
- Backend system optimized for Debian-based operating systems (e.g., Ubuntu).
- Integration of custom Python APIs and the `pynaoqi` library.

## Goals
1. Answer users' questions based on information retrieved from a database.
2. Utilize SoftBank's NAOqi API and NAO robot (body posture) to deliver a more intuitive and engaging chatting experience.

## Contributions
- Developed the majority of interfaces and core code (excluding robot posture functionality).
- Integrated multiple systems, including TTS, LLMs, and databases.
- Designed the system architecture, including class structures and interfaces.

## Key Technologies
- **Programming Language**: Python (versions 2.7 and 3.12)
- **Operating System**: Debian-based Linux (e.g., Ubuntu)
- **AI Models**:
  - [Google Gemma 2](https://huggingface.co/google/gemma-2-2b-it): Used for answer generation and general question answering.
  - [OpenAI Whisper](https://huggingface.co/openai/whisper-small.en): Deployed for speech-to-text processing and natural language understanding.
  - [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2): Transformed sentences into vector representations for database queries.
- **Database**: SQLite3 for storing question-answer information.
- **Tools**: `pynaoqi` API, virtual environments, Anaconda, and the Hugging Face library.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd project-directory
   ```
3. Install dependencies:
   - For Python 2.7:
     ```bash
     pip install -r /src/py2/requirements.txt
     ```
   - For Python 3.12:
     ```bash
     pip install -r /src/py3/requirements.txt
     ```
4. Update the AI model paths in `Conversation_Handler_Proto.ipynb` as needed.
5. Run the project using Jupyter Notebook.

## Acknowledgments
This project was a collaborative effort among university peers and was made possible through guidance from our Computer Science faculty.
