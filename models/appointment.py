class Appointment:
    def __init__(self,  appointment_time, appointment_date, owner, animal, id=None):
        self.appointment_time = appointment_time
        self.appointment_date = appointment_date
        self.owner = owner
        self.animal = animal
        self.id = id
