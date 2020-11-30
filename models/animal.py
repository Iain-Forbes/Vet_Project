class Animal:
    def __init__(self,
    name, date_of_birth, animal_type, treatment_notes, owner, id=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.animal_type = animal_type
        self.treatment_notes = treatment_notes
        self.owner = owner
        self.id = id

