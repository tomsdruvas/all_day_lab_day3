import unittest
from src.pub import Pub


class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
    
    def test_pub_has_name(self):
        expected = "The Prancing Pony"
        result = self.pub.name
        self.assertEqual(expected, result)

    