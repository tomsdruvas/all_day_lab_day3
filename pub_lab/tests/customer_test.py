import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from tests.pub_test import TestPub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.drink1 = Drink("Stella", 5, True, 4)
        self.drink2 = Drink("Gin and Tonic", 6, True, 4)
        self.drink3 = Drink("Tea", 4, False, 0)
        self.drink4 = Drink("Double Vodka", 10, True, 10)
        self.drinks_list = [self.drink1, self.drink2, self.drink3]
        self.customer = Customer("Joe", 500, 30, 5)
        self.customer2 = Customer("Helen", 30, 16, 0)
        self.customer3 = Customer("Charlie", 50, 15, 0)
        self.customer4 = Customer("Tom", 50, 20, 9)
        self.pub = Pub("The Prancing Pony", 100.00, self.drinks_list)


    def test_check_finished_drinks(self):
        expected = 0
        result = len(self.customer.finished_drinks)
        self.assertEqual(expected, result)

    def test_reduce_wallet(self):
        expected = 495
        self.customer.reduce_wallet(5, self.customer)
        self.assertEqual(expected, self.customer.wallet)
    

    def test_add_finished_drinks(self):
        expected = 1
        self.customer.add_finished_drink(self.drink1, self.customer2)
        self.assertEqual(expected, len(self.customer2.finished_drinks))

    def test_check_alcohol_status(self):
        expected = True
        result = self.customer.check_alcohol_status("Stella")
        self.assertEqual(expected, result)
    
    def test_check_alcohol_level(self):
        expected = 4
        result = self.customer.get_alcohal_level("Stella")
        self.assertEqual(expected, result)

    def test_buy_soft_drink(self):
        self.customer.buy_soft_drink("Tea", self.pub, self.customer3)
        # reduce cash of customer
        self.assertEqual(46, self.customer3.wallet)
        # increase cash in till
        self.assertEqual(104, self.pub.cash)
        # increase customers finished drinks
        self.assertEqual(1, len(self.customer3.finished_drinks))
        # remove from pub drinks list
        self.assertEqual(2, self.pub.drink_stock())

    def test_buy_drink(self):
        self.customer.buy_drink("Stella", self.pub, self.customer)
        # reduce cash of customer
        self.assertEqual(495, self.customer.wallet)
        # increase cash in till
        self.assertEqual(105, self.pub.cash)
        # increase customers finished drinks
        self.assertEqual(1, len(self.customer.finished_drinks))
        # remove from pub drinks list
        self.assertEqual(2, self.pub.drink_stock())

    def test_buy_drink_underage_alcohol(self):
        self.customer.buy_drink("Stella", self.pub, self.customer2)
        # reduce cash of customer
        self.assertEqual(30, self.customer2.wallet)
        # increase cash in till
        self.assertEqual(100, self.pub.cash)
        # increase customers finished drinks
        self.assertEqual(0, len(self.customer2.finished_drinks))
        # remove from pub drinks list
        self.assertEqual(3, self.pub.drink_stock())

    def test_buy_drink_underage_not_alcohol(self):
        self.customer.buy_drink("Tea", self.pub, self.customer3)
        # reduce cash of customer
        self.assertEqual(46, self.customer3.wallet)
        # increase cash in till
        self.assertEqual(104, self.pub.cash)
        # increase customers finished drinks
        self.assertEqual(1, len(self.customer3.finished_drinks))
        # remove from pub drinks list
        self.assertEqual(2, self.pub.drink_stock())