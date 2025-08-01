from models.abstractitems import abstractitems
from models.FoodMenu import FoodMenu
import time

class cart:
    def __init__(self,items,choices):
        self.foodItem = items
        self.choices = choices
        self.fooditems = self.addtocart(items)
    def addtocart(self,items):
        fooddic={}
        for choice in self.choices:
            if choice > len(items):
                raise KeyError
            if choice in fooddic:
                fooddic[choice]+=1
            else:
                fooddic[choice]=1
        return fooddic

    def processorder(self):
        total = 0
        summary_lines = []  # ✅ define this before appending
        print("\nYour Order Summary:")

        for item_index in self.fooditems:
            quantity = self.fooditems[item_index]
            item = self.foodItem[item_index - 1]
            price = item.price * quantity
            total += price
            line = f"{item.name} x {quantity} = ₹{price}"
            print(line)
            summary_lines.append(line)

        total_line = f"\nTotal Amount: ₹{total}"
        print(total_line)
        summary_lines.append(total_line)

        # ✅ Save to file
        with open("receipt.txt", "w",encoding="utf-8") as file:
            file.write("\n".join(summary_lines))

        self.processpayment(total)

    def processpayment(self, amount):
        print(f"Processing payment of ₹{amount}", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="")
        print("\nPayment successful! Thank you for your order.")







