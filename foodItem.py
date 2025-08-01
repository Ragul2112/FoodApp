from models.abstractitems import abstractitems
class foodItem(abstractitems):
    def __init__(self,name,rating,price,description):
        super().__init__(name,rating)
        self.price = price
        self.description = description
    def displayitem(self,start):
        print(f"{start} => {self.name},{self.price},{self.rating}")
