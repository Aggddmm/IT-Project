import sys
sys.path.append("/opt/anaconda3/envs/MPS-Torch/bin")

from transformers import pipeline
from datasets import load_dataset
import numpy as np
import torch

# always return sound with bit rate 16k
def getAudoChunks(text):

    synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
    # You can replace this embedding with your own as well.

    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})

    
    return speech['audio']