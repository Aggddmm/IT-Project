from abc import ABC, abstractmethod

class Backend_Interface(ABC):
    """ abstract class for all machine learning backends """
    
    @ abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def init(self, model_folder_path:str):
        """initialize and load the model

        Args:
            model_folder_path (str): directory path where the model is stored, or the model name from huggingface
        """
        pass
    
    @abstractmethod
    def get_info(self):
        """get information about the model

        Returns:
            dict: a dictionary containing information about the model, like parameters, etc.
        """
        pass
    