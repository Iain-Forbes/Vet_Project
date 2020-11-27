from db.run_sql import run_sql
from models.owner import Animal



def save(new_owner):
    sql = "INSERT INTO owners (name, contact_details) VALUES (%s, %s) RETURNING id"
    values = [new_owner.name, new_owner.contact_details]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id