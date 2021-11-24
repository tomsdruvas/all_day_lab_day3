class Pub():

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drinks_list = []
    
    def increase_cash(self, amount):
        self.cash += amount
