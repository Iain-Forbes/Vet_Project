from db.run_sql import run_sql
from models.animal import Animal
import repositories.owner_repository as owner_repository
from models.owner import *


def save(new_animal):
    sql = "INSERT INTO animals (name, date_of_birth, animal_type, treatment_notes, owner_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [
        new_animal.name, 
        new_animal.date_of_birth, new_animal.animal_type, new_animal.treatment_notes, new_animal.owner.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    new_animal.id = id
    

def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for result in results:
        owner = owner_repository.select(result["owner_id"])
        animal =  Animal(
            result["name"], 
            result ["date_of_birth"], 
            result ["animal_type"], 
            result ["treatment_notes"], 
            owner,
            result["id"])
        animals.append(animal)
    return animals

def select(id):
    sql ="SELECT * FROM animals where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
   

    if result is not None:
        owner = owner_repository.select(result["owner_id"])
        animal =  Animal(
        result["name"], 
        result ["date_of_birth"], 
        result ["animal_type"], 
        result ["treatment_notes"], 
        owner,
        result["id"]) 
    return animal 

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(animal):
    sql = "UPDATE animals SET (name, date_of _birth, animal_type, treatment plan, owner_id) (%s, %s, %s, %s, %s, %s) WHERE id = %s" 
    values = [
        animal.name, 
        animal.date_of_birth, 
        animal.animal_type, 
        animal.treatment_notes, 
        animal.owner.id,
        animal.id]
    run_sql(sql, values)

def display_animals_owned(id):
    owned_animals = []
    sql = """SELECT *
            FROM animals
            WHERE owner_id = %s"""
    vaules = [id]
    results = run_sql(sql, vaules)
    owner = owner_repository.select(id)
    for result in results:
        animals =  Animal(
        result ["name"],
        result ["date_of_birth"], 
        result ["animal_type"], 
        result ["treatment_notes"], 
        owner,
        result ["id"])
        owned_animals.append(animals)
    return owned_animals
        


