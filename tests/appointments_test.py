import unittest
from models.appointment import *

class AppointmentTest(unittest.TestCase):
    def setUp(self):
        self.appointment1 = Appointment("23:00", "22/06/82")

    def test_appointment_has_appointment_time(self):
        self.assertEquals(self.appointment1.appointment_time, "23:00")

    def test_appointment_has_appointment_time(self):
        self.assertEquals(self.appointment1.appointment_date, "22/06/82")