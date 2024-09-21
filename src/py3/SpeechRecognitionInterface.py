from MLBackendInterface import Backend_Interface
from abc import ABC, abstractmethod

class SpeechRecognition_Interface(Backend_Interface, ABC):
    @abstractmethod
    def recognize(self, audio_data:dict) -> str:
        """Recognize speech from audio data

        Args:
            audio_data (dict): audio data to be recognized, should contain the audio data and the sample rate

        Returns:
            str: recognized text
        """
        pass