from abc import ABC, abstractmethod

class BaseExtraction(ABC):
    def __init__(self, coffee):
        self.coffee = coffee
    
    @abstractmethod
    def extract(self):
        pass
    
    @abstractmethod
    def calculate_cost(self):
        pass