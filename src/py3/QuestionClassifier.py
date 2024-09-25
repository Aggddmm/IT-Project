from QuestionClassifierInterface import QuestionClassifier_Interface

import spacy
import joblib

class QuestionClassifier(QuestionClassifier_Interface):
    _nlp = None
    _model = None
    _vectorizer = None
    _model_name = '/question_classifier_knn.pkl'
    _vectorizer_name = 'vectorizer.joblib'
    _spacy_model_name = 'en_core_web_sm'
    
    def __init__(self):
        pass
    
    def init(self, model_folder_path:str):
        
        # Load the model
        self._model = joblib.load(model_folder_path + self._model_name)
        # Load the vectorizer
        self._vectorizer = joblib.load(model_folder_path + self._vectorizer_name)
        # Load the nlp model
        self._nlp = spacy.load(self._spacy_model_name)
    
    def get_info(self):
        return {
            'model': self._model,
            'vectorizer': self._vectorizer,
            'nlp': self._nlp,
            'model_name': self._model_name,
            'vectorizer_name': self._vectorizer_name,
            'spacy_model_name': self._spacy_model_name
        }
    
    def classify(self, question:str) -> str:
        processed_text = self._preprocess_text(question)
        vectorized_text = self._vectorizer.transform([processed_text])
        prediction = self._model.predict(vectorized_text)
        return prediction[0]
    
    # private methods for question preprocessing
    def _preprocess_text(self, text):
        """ Preprocess question into flavorable format for the model """
        # Normalize text
        processed_text:str = text.lower()
        processed_text = processed_text.replace('?', '')
        # lemmatization
        doc = self._nlp(processed_text)
        processed_text = ' '.join([token.lemma_ for token in doc])
        
        return processed_text