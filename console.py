import pdb
from models.animal import *
from models.owner import *
from models.vet import *

import repositories.owner_repository as owner_repository


owner_repository.delete_all()


owner1 = Owner("Jimmy", "Cloverfeild")
owner_repository.save(owner1)
owner2 = Owner("Steve", "Black Mesa")
owner_repository.save(owner2)

owner_repository.select_all()

pdb.set_trace()
