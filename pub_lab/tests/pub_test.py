import unittest
from unittest import result
from src.pub import Pub
from src.drink import Drink


class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink("Stella", 5, True)
        self.drink2 = Drink("Gin and Tonic", 6, True)
        self.drink3 = Drink("Tea", 4, False)
        drinks_list = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("The Prancing Pony", 100.00, drinks_list)

    
    def test_pub_has_name(self):
        expected = "The Prancing Pony"
        result = self.pub.name
        self.assertEqual(expected, result)
    
    def test_pub_has_cash(self):
        expected = 100
        result = self.pub.cash
        self.assertEqual(expected, result)
    
    def test_increase_cash(self):
        expected = 150
        self.pub.increase_cash(50)
        self.assertEqual(expected, self.pub.cash)
    
    def test_drinks_stock(self):
        self.assertEqual(3, self.pub.drink_stock())
        




    