import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Joe", 500, 0)

    def test_check_finished_drinks(self):
        expected = 0
        result = self.customer.finished_drinks
        self.assertEqual(expected, result)

    def test_reduce_wallet(self):
        expected = 495
        self.customer.reduce_wallet(5)
        self.assertEqual(expected, self.customer.wallet)

    def test_add_finished_drinks(self):
        expected = 1
        self.customer.add_finished_drink(1)
        self.assertEqual(expected, self.customer.finished_drinks)
