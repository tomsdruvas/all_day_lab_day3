import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from tests.pub_test import TestPub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Stella", 5, True)
        self.drink2 = Drink("Gin and Tonic", 6, True)
        self.drink3 = Drink("Tea", 4, False)
        self.drinks_list = [self.drink1, self.drink2, self.drink3]
        self.customer = Customer("Joe", 500)
        self.pub = Pub("The Prancing Pony", 100.00, self.drinks_list)


    def test_check_finished_drinks(self):
        expected = 0
        result = len(self.customer.finished_drinks)
        self.assertEqual(expected, result)

    def test_reduce_wallet(self):
        expected = 495
        self.customer.reduce_wallet(5)
        self.assertEqual(expected, self.customer.wallet)

    def test_add_finished_drinks(self):
        expected = 1
        self.customer.add_finished_drink(self.drink1)
        self.assertEqual(expected, len(self.customer.finished_drinks))

    def test_buy_drink(self):
        self.customer.buy_drink("Stella", self.pub)
        # reduce cash of customer
        self.assertEqual(495, self.customer.wallet)
        # increase cash in till
        self.assertEqual(105, self.pub.cash)
        # increase customers finished drinks
        self.assertEqual(1, len(self.customer.finished_drinks))
        # remove from pub drinks list
        self.assertEqual(2, self.pub.drink_stock())