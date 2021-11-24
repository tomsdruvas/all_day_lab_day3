from src.pub import Pub
from src.drink import Drink
import pdb

class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.finished_drinks = []
        self.age = age
        self.drink1 = Drink("Stella", 5, True)
        self.drink2 = Drink("Gin and Tonic", 6, True)
        self.drink3 = Drink("Tea", 4, False)
        self.drinks_list = [self.drink1, self.drink2, self.drink3]

    def reduce_wallet(self, amount):
        self.wallet -= amount 

    def add_finished_drink(self, drink):
        self.finished_drinks.append(drink)

    def buy_drink(self, name_of_drink, pub):
        
        for drink in pub.drinks_list:
            if drink.name == name_of_drink:
                # pdb.set_trace()
                self.reduce_wallet(drink.price)
                pub.increase_cash(drink.price)
                self.add_finished_drink(drink)
                pub.remove_drink(drink)
        

