import pdb
from models.animal import *
from models.owner import *
from models.vet import *

import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository


owner_repository.delete_all()
animal_repository.delete_all()

owner1 = Owner("Jimmy", "Cloverfeild")
owner_repository.save(owner1)
owner2 = Owner("Steve", "Black Mesa")
owner_repository.save(owner2)
owner_repository.select_all()

animal1 = Animal("Joe", "2020-10-10","Goose", "Broken Goosing: Adminsiter 50cc's of goose.")
animal_repository.save(animal1)

pdb.set_trace()
