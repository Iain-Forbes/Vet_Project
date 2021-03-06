from db.run_sql import run_sql
from models.owner import Owner
from models.appointment import Appointment
from models.animal import Animal

def save(new_owner):
    sql = "INSERT INTO owners (name, address) VALUES (%s, %s) RETURNING id"
    values = [new_owner.name, new_owner.address]
    results = run_sql(sql, values)
    id = results[0]['id']
    new_owner.id = id

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for result in results:
        owner = Owner(
            result["name"], 
            result["address"],
            result["id"])
        owners.append(owner)
    return owners

def select(id):
    sql ="SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
   
    if result is not None:
     owner = Owner(
        result["name"], 
        result["address"], 
        result["id"])
    return owner 

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    vaules = [id]
    run_sql(sql, vaules)

def update(owner):
    sql = "UPDATE owners SET (name, address) = (%s, %s) WHERE id = %s"
    values = [
        owner.name, 
        owner.address, 
        owner.id]
    run_sql(sql, values)

