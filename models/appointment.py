class Appointment:
    def __init__(self,  start_time, end_time, appointment_date, animal, id=None):
        self.start_time = start_time
        self.end_time = end_time
        self.appointment_date = appointment_date
        self.animal = animal
        self.id = id
