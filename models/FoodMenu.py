from models.abstractitems import abstractitems
from models.foodItem import foodItem  # Assuming this exists

class FoodMenu(abstractitems):
    def __init__(self, name):
        super().__init__(name, rating=0)
        self.__foodItems = []

    @property
    def foodItems(self):
        return self.__foodItems

    @foodItems.setter
    def foodItems(self, items):
        for item in items:
            if not isinstance(item, foodItem):
                print("The item is not a foodItem.")
                return
        self.__foodItems = items

    def displayitem(self, start):
        print(f"{start} => {self.name}")
