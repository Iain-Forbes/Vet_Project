from db.run_sql import run_sql
from models.appointment import Appointment
from models.owner import *
from models.animal import *
import repositories.owner_repository as owner_repository
import repositories.animal_repository as amnimal_repository

def save(new_appointment):
    sql = "INSERT INTO appointments (appointment_time, appointment_date, owner.id, animaL_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [new_appointment.appointment_time, new_appointment.appointment_date, new_appointment.owner.id, new_appointment.animal.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    new_appointment.id = id

def select_all():
    appointments = []
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    for result in results:
        owner = owner_repository.select(result["owner.id"])
        animal = amnimal_repository.select(result["animal.id"])
        appointment = Appointment(result["appointment_time"], result["appintment_date"], owner, animal, result["id"])
        appointments.append(appointment)
    return appointments

    def select(id):
        sql = "SELECT * FROM appointments WHERE id = %s"
        vaules = [id]
        results = run_sql(sql, vaules)
        owner = owner_repository.select(result["owner.id"])
        animal = amnimal_repository.select(result["animal.id"])
        appointment = Appointment(result["appointment_time"], result["appintment_date"], owner, animal, result["id"])
        return appointment

def delete_all():
    sql = "DELETE * FROM appoinments"

def delete(id):
    sql = "DELETE FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(appointment):
    sql = "UPDATE appointments SET (appointment_time, appointment_date, animal.id, owner_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    vaules = [appointment.appointment_time, appointment.appointment_date, appointment.owner._id, appointment.animal_id, appointment.id]
    run_sql(sql, vaules)