from db.run_sql import run_sql
from models.owner import *


def save(new_owner):
    sql = "INSERT INTO owners (name, contact_details) VALUES (%s, %s) RETURNING id"
    values = [new_owner.name, new_owner.contact_details]
    results = run_sql(sql, values)
    id = results[0]['id']
    new_owner.id = id

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for result in results:
        owner = Owner(result["name"], result ["contact_details"],result["id"])
        owners.append(owner)
    return owners

def select(id):
    sql ="SELECT * FROM owners where id = %s"
    vaules = [id]
    result = run_sql(sql, values[0])
    owner = Owner(result["name"], result, ["contact_details"],result["id"])
    return owner 

def delete_all():
    sql = "DELETE FROM humans"
    run_sql(sql)