from abc import ABC, abstractmethod

class Agent(ABC):
    @abstractmethod
    def review(self, input_data: str) -> str:
        pass