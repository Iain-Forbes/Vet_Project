import unittest
from models.vet import *

class VetTest(unittest.TestCase):
    def setUp(self):
        self.vet1 = Vet("23:00", "22/06/82")

    def test_vet_has_appointment_time(self):
        self.assertEquals(self.vet1.appointment_time, "23:00")

    def test_vet_has_appointment_time(self):
        self.assertEquals(self.vet1.appointment_date, "22/06/82")