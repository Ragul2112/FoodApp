from models.abstractitems import abstractitems
from models.FoodMenu import FoodMenu

class Restaurant(abstractitems):
    def __init__(self, name,rating ,location ,offer):
        super().__init__(name,rating)
        self.location = location
        self.offer = offer
        self.__FoodMenus=[]

    @property
    def FoodMenus(self):
        return self.__FoodMenus

    @FoodMenus.setter
    def FoodMenus(self, items):
        for item in items:
            if not (isinstance(item, FoodMenu)):
                print("The item is not a FoodMenu.")
                return
        self.__FoodMenus = items
    def displayitem(self,start):
        print(f"{start} => {self.name},{self.rating}")
