from Interfaces.SpeechRecognitionInterface import SpeechRecognition_Interface

import torch
import os
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

class SpeechRecognitionBackend(SpeechRecognition_Interface):
    device = "mps"
    model_path = "/Users/lipeihong/Downloads/whisper-small.en"
    sampling_rate = 16000
    torch_dtype = torch.float16
    pipe = None
    processor = None

    def __init__(self):
        pass
    
    def init(self, model_folder_path:str):
        if not os.path.exists(model_folder_path):
            raise Exception("Model folder does not exist")
        
        print("[+] initializing SpeechRecognitionBackend")
        self.model_path = model_folder_path
        # choose processing backend
        if torch.cuda.is_available():
            self.device = "cuda"
        elif torch.backends.mps.is_available():
            self.device = "mps"
        else:
            self.device = "cpu"
        print("    -> Using device: ", self.device)
        
        # Load the model
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            self.model_path, torch_dtype=self.torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        model.to(self.device)

        self.processor = AutoProcessor.from_pretrained(self.model_path)

        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            torch_dtype=self.torch_dtype,
            device=self.device,
        )
        print("    -> SpeechRecognitionBackend loaded")
        
    def get_info(self):
        return {
            "device": self.device,
            "model_path": self.model_path,
            "sampling_rate": self.sampling_rate,
            "torch_dtype": self.torch_dtype,
        }
        
    def recognize(self, audio_data:dict) -> str:
        # print("**** Debug ****: ", audio_data)
        # print("**** Debug **** [Condition 1] Should be: False", "array" not in audio_data)
        # print("**** Debug **** [Condition 2] Should be: False", "sampling_rate" not in audio_data)

        if "array" not in audio_data or "sampling_rate" not in audio_data:
            raise Exception("audio_data should contain the audio data and the sample rate")
        return self.pipe(audio_data)
        
        