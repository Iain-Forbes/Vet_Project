import unittest
from models.owner import *

class OwnerTest(unittest.TestCase):
    def setUp(self):
        self.owner1 = Owner("Dr House", "132 fake drive")

    def test_owner_has_name(self):
        self.assertEquals(self.owner1.name, "Dr House")

    def test_owner_has_address(self):
        self.assertEquals(self.owner1.address, "132 fake drive" )
