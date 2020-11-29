import pdb
from models.animal import *
from models.owner import *
from models.appointment import *

import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.appointment_repository as appointment_repository


owner_repository.delete_all()
animal_repository.delete_all()
appointment_repository.delete_all() 

owner1 = Owner("Jimmy", "Cloverfeild")
owner_repository.save(owner1)
owner2 = Owner("Steve", "Black Mesa")
owner_repository.save(owner2)
# owner_repository.select_all()

animal1 = Animal("Joe", "2020-10-10","Goose", "Broken Goosing: Adminsiter 50cc's of goose.")
animal_repository.save(animal1)
# animal_repository.select_all()

appointment1 = Appointment("17:40", "2201-23-23", owner1, animal1)

appointment_repository.save(appointment1)
appointment_repository.select_all()



pdb.set_trace()
