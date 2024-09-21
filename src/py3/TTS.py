from TTSInterface import TTS_Interface

import torch
from transformers import FastSpeech2ConformerTokenizer, FastSpeech2ConformerModel, FastSpeech2ConformerHifiGan

class TTSBackend(TTS_Interface):
    
    device:str = None
    tokenizer = None
    model = None
    hifigan = None
    samplerate = 22050
    
    def __init__(self):
        pass
    
    def init(self, model_folder_path:str="espnet/fastspeech2_conformer"):
        print("[+] initializing TTS System")
        # choose processing backend
        if torch.cuda.is_available():
            self.device = "cuda"
        elif torch.backends.mps.is_available():
            self.device = "mps"
        else:
            self.device = "cpu"
        print("    -> Using device: ", self.device)
        self.tokenizer = FastSpeech2ConformerTokenizer.from_pretrained(model_folder_path)
        self.model = FastSpeech2ConformerModel.from_pretrained(model_folder_path)
        self.model.to(self.device)
        self.hifigan = FastSpeech2ConformerHifiGan.from_pretrained("espnet/fastspeech2_conformer_hifigan")
        
        print("    -> TTS System loaded")
    
    def get_info(self):
        return {
            "device": self.device,
            "model": "FastSpeech2Conformer",
            "tokenizer": "FastSpeech2ConformerTokenizer",
            "hifigan": "FastSpeech2ConformerHifiGan",
            "sample_rate": self.samplerate
        }
        
    def synthesize(self, text: str) -> dict:
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        input_ids = inputs["input_ids"]

        output_dict = self.model(input_ids, return_dict=True)
        spectrogram = output_dict["spectrogram"]
        waveform = self.hifigan(spectrogram.to("cpu"))

        return {"array": waveform.squeeze().detach().numpy(), "sampling_rate": self.samplerate}