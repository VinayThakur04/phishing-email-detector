from abc import ABC, abstractmethod

class BaseRule(ABC):
    @abstractmethod
    def check(self, email: dict) -> bool:
        pass
