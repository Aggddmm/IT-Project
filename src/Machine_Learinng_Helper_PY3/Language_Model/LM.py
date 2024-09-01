
from transformers import AutoTokenizer, AutoConfig
from transformers import AutoModelForCausalLM
from safetensors.torch import load_file
import torch
import os

MODEL_PATH = ""

class Gemma2LMBackEnd:
    process_device = None
    model_folder = ""
    model = None
    tokenizer = None
    
    def __init__(self, model_folder) -> None:
        # Check if the model folder exists
        if not os.path.exists(model_folder):
            raise Exception("Model folder does not exist")
        # check what device is avaliable to run torch
        if torch.cuda.is_available():
            message += "CUDA"
            self.process_device  = torch.device("cuda")
        elif torch.backends.mps.is_available():
            self.process_device  = torch.device("mps")
        else:
            self.process_device = torch.device("cpu")
            
        print("Using device: ", self.process_device)
            
        self.model_folder = model_folder
        
        # Load the model
        self.model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=self.model_folder, 
            torch_dtype=torch.bfloat16
        )
        self.model.to(self.process_device)
        
        # Load the tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_folder)
        
    def getInfo(self):
        return {
            "device": self.process_device
        }
        
    def generate_text(self, text:str):
        input_ids = self.tokenizer(text, return_tensors="pt").to(self.process_device)
        outputs = self.model.generate(**input_ids)
        return self.tokenizer.decode(outputs[0])
        
if __name__ == "__main__":
    model_folder = "/Volumes/Untitled/Gemma 2/gemma-2-2b-it"
    LMProcessor = Gemma2LMBackEnd(model_folder)
    print(LMProcessor.getInfo())
    print(LMProcessor.generate_text("Hello, World!"))


