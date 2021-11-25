import unittest
from unittest import result
from src.drink import Drink


class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Stella", 5, True, 4)
        self.drink2 = Drink("Gin and Tonic", 6, True, 4)
        self.drink3 = Drink("Tea", 4, False, 0)
        self.drink4 = Drink("Double Vodka", 10, True, 10)

    
