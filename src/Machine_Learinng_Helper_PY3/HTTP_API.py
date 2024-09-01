from flask import Flask, request, jsonify, send_file
from scipy.io.wavfile import write
import io

IP_TITLE = "ip"
PORT_TITLE = "port"
MESSAGE_TITLE = "message"
ERROR_TITLE = "error"

# Global variables
app = Flask(__name__)
language_model = None
language_model_path = "/Volumes/Untitled/Gemma 2/gemma-2-2b-it"

import TTS.TTS
@app.route('/getAudio', methods=['POST'])
def get_audio():
    data = request.get_json()
    if data and MESSAGE_TITLE in data:
        text = data[MESSAGE_TITLE]
        audio = TTS.TTS.getAudoChunks(text)
        
        sampling_rate = 16000  # Example sampling rate
        wav_io = io.BytesIO()
        write(wav_io, sampling_rate, audio)
        wav_io.seek(0)  # Rewind the buffer to the beginning
        
        # Serve the WAV file over HTTP
        return send_file(wav_io, mimetype='audio/wav')
    else:
        return jsonify({'error': 'Invalid input, expected JSON with "audio" key'}), 400
    
import Language_Model.LM
@app.route('/generateText', methods=['POST'])
def generate_text():
    data = request.get_json()
    if data and MESSAGE_TITLE in data:
        text = str(data[MESSAGE_TITLE])
        print("Generating text for input:", text)
        global language_model
        global language_model_path
        
        if not language_model:
            language_model = Language_Model.LM.Gemma2LMBackEnd(language_model_path)
        generated_text = language_model.generate_text(text)
        return jsonify({MESSAGE_TITLE: generated_text})
    else:
        return jsonify({'error': 'Invalid input, expected JSON with "audio" key'}), 400
app.run(debug=True, port=5000)