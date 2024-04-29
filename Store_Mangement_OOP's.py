'''
    The below code represents the class and objets utilization in the code

'''
import csv

class Item:
    pay_rate = 0.8
    all = []
    def __init__(self , name:str , price , quantity=0) -> None:

        assert price >= 0, f"Price {price} not greater than 0"
        assert quantity >= 0 ,f"Quantity {quantity} not greater than 0"

        self.name = name
        self.price = price
        self.quantity =  quantity

        
        
    # Actions to execute
        Item.all.append(self)

    def calucalte_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('Item.csv' , 'r') as f:
            reader = csv.DictReader(f)
            for i in reader:
                Item(
                    name=i.get('name'),
                    price=int(i.get('price')),
                    quantity=int(i.get('quantity'))
                )
            
    def __repr__(self) -> str:
        return f"Item({self.name} , {self.price} , {self.quantity})" 
    
Item.instantiate_from_csv()
print(Item.all)