class Pub:

    def __init__(self, name, cash, drinks_list):
        self.name = name
        self.cash = cash
        self.drinks_list = drinks_list
    
    def increase_cash(self, amount):
        self.cash += amount

    def drink_stock(self):
        return len(self.drinks_list)

    def add_drink(self, new_drink):
        self.drinks_list.append(new_drink)

    def remove_drink(self, drink_removed):
        for drink in self.drinks_list:
            if drink.name == drink_removed.name:
                self.drinks_list.remove(drink)

    def return_drink_price(self, drink_name):
        for drink in self.drinks_list:
            if drink.name == drink_name:
                return drink.price