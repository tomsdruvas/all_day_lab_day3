from src.pub import Pub
from src.drink import Drink
import pdb

class Customer:
    def __init__(self, name, wallet, age, drunkness):
        self.name = name
        self.wallet = wallet
        self.finished_drinks = []
        self.age = age
        self.drunkness = drunkness
        self.drink1 = Drink("Stella", 5, True, 4)
        self.drink2 = Drink("Gin and Tonic", 6, True, 4)
        self.drink3 = Drink("Tea", 4, False, 0)
        self.drink4 = Drink("Double Vodka", 10, True, 10)
        self.drinks_list = [self.drink1, self.drink2, self.drink3, self.drink4]

    def reduce_wallet(self, amount, customer):
        customer.wallet -= amount

    def add_finished_drink(self, drink, customer):
        customer.finished_drinks.append(drink)

    def check_alcohol_status(self, drink_name):
        for drink in self.drinks_list:
            if drink.name == drink_name:
                if drink.alcohol_status:
                    return True
                else:
                    return False

    def get_alcohal_level(self, drink_name):
        for drink in self.drinks_list:
            if drink.name == drink_name:
                return drink.alcohol_level
                    
    
    def buy_soft_drink(self, name_of_drink, pub, customer):
        if self.check_alcohol_status(name_of_drink) == False:
            for drink in pub.drinks_list:
                if drink.name == name_of_drink:
                    # pdb.set_trace()
                    self.reduce_wallet(drink.price, customer)
                    pub.increase_cash(drink.price)
                    self.add_finished_drink(drink, customer)
                    pub.remove_drink(drink)

    def buy_drink(self, name_of_drink, pub, customer):

        if pub.check_age(customer):
            alcohol_level = self.get_alcohal_level(name_of_drink)
            drunkness = customer.drunkness
            total = alcohol_level + drunkness

            if total < 10:
                for drink in pub.drinks_list:
                    if drink.name == name_of_drink:
                        # pdb.set_trace()
                        self.reduce_wallet(drink.price, customer)
                        pub.increase_cash(drink.price)
                        self.add_finished_drink(drink, customer)
                        pub.remove_drink(drink)
                    
        elif pub.check_age(customer) == False and self.check_alcohol_status(name_of_drink) == False:
            # pdb.set_trace()
            for drink in pub.drinks_list:
                if drink.name == name_of_drink:
                    # pdb.set_trace()
                    self.reduce_wallet(drink.price, customer)
                    pub.increase_cash(drink.price)
                    self.add_finished_drink(drink, customer)
                    pub.remove_drink(drink)
        

