from Interfaces.MLBackendInterface import Backend_Interface
from abc import ABC, abstractmethod

class LM_Interface(Backend_Interface, ABC):
    """ Abstract class for language models (NLP Component) """
    @abstractmethod
    def generate_text(self, prompt:str) -> str:
        """Generates text based on the prompt

        Args:
            prompt (str): User's prompt

        Returns:
            str: Generated text by model
        """
        pass