from MLBackendInterface import Backend_Interface
from abc import ABC, abstractmethod

class TTS_Interface(Backend_Interface, ABC):
    @abstractmethod
    def synthesize(self, text:str) -> dict:
        """Synthesize speech from text

        Args:
            text (str): text to be synthesized

        Returns:
            dict: audio data, should contain the audio data and the sample rate
        """
        pass