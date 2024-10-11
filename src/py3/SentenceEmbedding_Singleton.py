from transformers import AutoTokenizer, AutoModel
import torch

class SentenceEmbedding:
    tokenizer = None
    model = None
    compute_backend = None
    _instance = None
    
    def get_compute_backend(self):
        if torch.cuda.is_available():
            return "cuda"
        elif torch.backends.mps.is_available():
            return "mps"
        else:
            return "cpu"
    
    def __init__(self) -> None:
        self.compute_backend = self.get_compute_backend()
        self.tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
        self.model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2').to(self.compute_backend)
        
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SentenceEmbedding, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def get_sentence_embedding(self, text:str):
        input_ids = self.tokenizer(text, return_tensors='pt')['input_ids'].to("cuda")
        with torch.no_grad():
            model_output = self.model(input_ids)
        # return model_output.last_hidden_state[:,0,:].squeeze()
        return model_output.last_hidden_state[:,0,:].squeeze().cpu().numpy()
    

    