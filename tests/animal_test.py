import unittest
from models.animal import *

class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.ali = Animal("ali", "22/06/87", "dog", "cunning plan")

    def test_Ali_has_name(self):
        self.assertEquals(self.ali.name, "ali")
