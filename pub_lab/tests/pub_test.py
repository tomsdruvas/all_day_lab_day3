import unittest
from unittest import result
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink1 = Drink("Stella", 5, True)
        self.drink2 = Drink("Gin and Tonic", 6, True)
        self.drink3 = Drink("Tea", 4, False)
        drinks_list = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("The Prancing Pony", 100.00, drinks_list)
        self.customer = Customer("Joe", 500, 30)
        self.customer2 = Customer("Beth", 30, 15)

    
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
    
    def test_add_drinks(self):
        self.new_drink = Drink("Red Wine", 9, True)
        self.pub.add_drink(self.new_drink)
        self.assertEqual(4, self.pub.drink_stock())

    def test_remove_drink(self):
        self.pub.remove_drink(self.drink1)
        self.assertEqual(2, self.pub.drink_stock())

    def test_return_drink_price(self):
        expected = 5
        result = self.pub.return_drink_price(self.drink1.name)
        self.assertEqual(expected, result)

    def test_check_customer_age_over_18(self):
        expected = True
        result = self.pub.check_age(self.customer)
        self.assertEqual(expected, result)

    def test_check_customer_age_under_18(self):
        expected = False
        result = self.pub.check_age(self.customer2)
        self.assertEqual(expected, result)



    