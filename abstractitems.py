
from abc import ABC, abstractmethod

class abstractitems(ABC):
    def __init__(self,name,rating):
        self.name = name
        self.rating = rating
    @abstractmethod
    def displayitem(self,start):pass

