from db.run_sql import run_sql
from models.animal import Animal


def save(new_animal):
    sql = "INSERT INTO animals (name, date_of_birth, animal_type, treatment_notes) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [new_animal.name, new_animal.date_of_birth, new_animal.animal_type, new_animal.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    new_animal.id = id

def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for result in results:
        animal =  Animal(result["name"], result ["date_of_birth"], result ["animal_type"], result ["treatment_notes"], result["id"])
        animals.append(animal)
    return animals

def select(id):
    sql ="SELECT * FROM animals where id = %s"
    vaules = [id]
    result = run_sql(sql, values[0])
    owner = animal =  Animal(result["name"], result ["date_of _birth"], result ["animal_type"], result ["treatment_notes"], result["id"])
    return animal 

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    vaules = [id]
    run_sql(sql, vaules)

def update(animal):
    sql = "UDPATE animals SET name  = %s SET date_of _birth = %s SET animal_type = %s SET  treatment plan = %s WHERE id %s"
    vaules = [animal.name, animal.date_of_birth, animal.animal_type, animal.treatment_notes]
    run_sql(sql, values)


