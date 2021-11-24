class Customer:
    def __init__(self, name, wallet, finished_drinks):
        self.name = name
        self.wallet = wallet
        self.finished_drinks = finished_drinks

    def reduce_wallet(self, amount):
        self.wallet -= amount 

    def add_finished_drink(self, amount):
        self.finished_drinks += amount