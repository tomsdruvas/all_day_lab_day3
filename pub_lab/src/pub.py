class Pub():

    def __init__(self, name, cash, drinks_list):
        self.name = name
        self.cash = cash
        self.drinks_list = drinks_list
    
    def increase_cash(self, amount):
        self.cash += amount

    def drink_stock(self):
        return len(self.drinks_list)