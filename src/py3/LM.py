from Interfaces.LMInterface import LM_Interface
from LM_ChatState import ChatState

import os
import torch
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM

class LMBackend(LM_Interface):
    device:str = None
    model = None
    model_path:str = None
    tokenizer = None
    config = None
    chat_state = None
    
    def __init__(self):
        pass
    
    def init(self, model_folder_path:str):
        if not os.path.exists(model_folder_path):
            raise Exception("Model folder does not exist")
        
        print("[+] initializing LMBackend")
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
        self.model = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=self.model_path, 
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            use_safetensors=True
        )
        self.model.to(torch.device(self.device))
        self.config = AutoConfig.from_pretrained(self.model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        
        self.chat_state = ChatState(system="answer questions briefly with chat tone")
        print("    -> LMBackend loaded")
    
    def get_info(self):
        return {
            "device": self.device,
            "model_path": self.model_path,
        }
    
    def generate_text(self, prompt:str) -> str:
        full_prompt = self.chat_state.get_prompt(prompt)
        
        input_ids = self.tokenizer(full_prompt, return_tensors="pt").to(torch.device(self.device))
        outputs = self.model.generate(
            **input_ids,
            max_new_tokens=150,  
            eos_token_id=self.tokenizer.eos_token_id,  
            pad_token_id=self.tokenizer.eos_token_id 
        )
        
        response_text = self.tokenizer.decode(outputs[0], skip_special_tokens=False)
        
        answer_list = response_text.split("<start_of_turn>model")
        answer = answer_list[len(answer_list)-1].split("<end_of_turn><eos>")[0].replace("\n", "")
        
        self.chat_state.add_to_history_as_model(answer)
        print("    -> Generated response: ", answer)
        return answer

