import unittest
from unittest import result
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Joe", 500, 0)

    def test_check_finished_drinks(self):
        expected = 0
        result = self.customer.finished_drinks
        self.assertEqual(expected, result)

    
