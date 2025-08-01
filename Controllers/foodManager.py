

from models.foodItem import foodItem
from models.FoodMenu import FoodMenu
from models.Restaurant import Restaurant
class foodManager:
    def __init__(self):
        self.Restaurant = self.__PrepareRestaurant()
    def PrepareFoodItems(self):
        item1 = foodItem("vegbiriyani",4,130,"**")
        item2 = foodItem("parota",7,120,"@@")
        item3 = foodItem("chickenrice",9,110,"%%")
        item4 = foodItem("noodle", 7, 110, "$$")
        return [item1, item2, item3,item4]
    def __PrepareFoodMenu(self):
        foodItems = self.PrepareFoodItems()
        menu1 = FoodMenu("veg")
        menu1.foodItems = [foodItems[0],foodItems[1]]
        menu2 = FoodMenu("non-veg")
        menu2.foodItems = [foodItems[2]]
        menu3 = FoodMenu("chinese")
        menu3.foodItems = [foodItems[3]]

        return [menu1, menu2, menu3]

    def __PrepareRestaurant(self):
        menus =self.__PrepareFoodMenu()
        res1 = Restaurant("arcot",2.4,"chennai",10)
        res1.FoodMenu = [menus[0]]
        res2 = Restaurant("santhosi",6,"mumbai",9)
        res2.FoodMenu = [menus[1], menus[2]]
        return [res1,res2]

    def findrestaurant(self, name):
        for res in self.Restaurant:
            if res.name.lower() == name:
                return res
        return None







