from MLBackendInterface import Backend_Interface

from abc import ABC, abstractmethod

class QuestionClassifier_Interface(Backend_Interface):
    """ abstract class for all question classifiers """
    
    @abstractmethod
    def classify(self, question:str) -> str:
        """classify the question and return the category
        
        Args:
            question (str): the question to be classified
        
        Returns:
            str: the category of the question
        """
        pass