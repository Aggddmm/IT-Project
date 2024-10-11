from Interfaces.QuestionClassifierInterface import QuestionClassifier_Interface
from SentenceEmbedding_Singleton import SentenceEmbedding

import torch

import joblib
import numpy as np

class Answer_Classifier(QuestionClassifier_Interface):
    _model_name = '/answer_classifier_knn.joblib'
    _vectorizer = None
    
    
    def __init__(self):
        pass
    
    def init(self, model_folder_path:str):
        
        # Load the model
        self._model = joblib.load(model_folder_path + self._model_name)

    def get_info(self):
        return {
            'model': self._model,
        }
    
    def classify(self, question:str) -> str:
        processed_vector = self._preprocess_text(question)
        prediction = self._model.predict(processed_vector.reshape(1, -1))
        return prediction[0]
    
    # private methods for question preprocessing
    def _preprocess_text(self, text):
        """ Preprocess question into flavorable format for the model """
        instance = SentenceEmbedding()
        return instance.get_sentence_embedding(text=text)