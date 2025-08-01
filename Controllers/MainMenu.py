from controllers.foodManager import foodManager
from models.Cart import cart
from models.foodItem import foodItem


class MainMenu:
    __options = {
        1: "showrestaurants",
        2: "showfooditems",
        3: "searchRestaurants",
        4: "searchfooditems",
        5: "exit"
    }
    def __init__(self):
        self.__foodManager= foodManager()
    def showrestaurants(self):
        for i, res in enumerate(self.__foodManager.Restaurant,1):
            res.displayitem(i)
        try:
            choice = int(input("Please choose a restaurant number: "))
            if 1 <= choice <= len(self.__foodManager.Restaurant):
                res = self.__foodManager.Restaurant[choice - 1]
                self.showfoodmenu(res.FoodMenu)
            else:
                print("Invalid restaurant selection.")
        except Exception as e:
            print("Error in showrestaurants:", e)

    def showfooditems(self):
        fooditems = self.__foodManager.PrepareFoodItems()
        for i,item in enumerate(fooditems,1):
            item.displayitem(i)
        try:
            choices = list(map(int, input("Please choose your food items (comma-separated): ").split(',')))
            c = cart(fooditems, choices)
            c.processorder()
        except Exception as e:
            print("Error in showfooditems:", e)

    def searchRestaurants(self):
        print("\nAvailable Restaurants:")
        for res in self.__foodManager.Restaurant:
            print(f"- {res.name}")
        resname = input("Please enter restaurant name: ").strip().lower()
        res = self.__foodManager.findrestaurant(resname)
        if res is not None:
            print(f"Restaurant found: {res.name} (Rating: {res.rating})")
            self.showfoodmenu(res.FoodMenu)
        else:
            print(f"Restaurant '{resname}' not found.")

    def searchfooditems(self):
        # Show all available food items first
        print("\nAvailable Food Items:")
        all_items = self.__foodManager.PrepareFoodItems()
        for i, item in enumerate(all_items, 1):
            item.displayitem(i)

        # Ask user for input to search
        query = input("\nEnter food item name to search: ").strip().lower()

        # Filter matching food items
        matched_items = [item for item in all_items if query in item.name.lower()]

        # If found, display and process order
        if matched_items:
            print("\nSearch Results:")
            for i, item in enumerate(matched_items, 1):
                item.displayitem(i)
            try:
                choices = list(map(int, input("Please choose your food items (comma-separated): ").split(',')))
                c = cart(matched_items, choices)
                c.processorder()
            except Exception as e:
                print("Error in searchfooditems:", e)
        else:
            print("No food items found with that name.")

    def showfoodmenu(self, menu_list):
        print("\n\nList of menu available:")
        for i, m in enumerate(menu_list, 1):
            print(f"{i} => {m.name}")
        try:
            choice = int(input("Please choose menu: "))
            selected_menu = menu_list[choice - 1]  # ✅ This is a single FoodMenu object

            fooditems = selected_menu.foodItems  # ✅ No indexing, just get the list of food items

            for i, item in enumerate(fooditems, 1):
                item.displayitem(i)

            choices = list(map(int, input("Please choose your food items (comma-separated): ").split(',')))
            c = cart(fooditems, choices)
            c.processorder()

        except Exception as e:
            print("Error in showfoodmenu:", e)

    def exit(self):
        print("Thank you! Logging out...")
        quit()

    def start(self):
        while True:
            for option in MainMenu.__options:
                print(f">>{option}.{MainMenu.__options[option]}")
            print()
            try:
                choice = int(input("please select the choice"))
                value=MainMenu.__options[choice]
                getattr(self,value)()
            except Exception as e:
                print("Error:", e)





