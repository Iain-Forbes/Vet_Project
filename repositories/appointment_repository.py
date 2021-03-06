from db.run_sql import run_sql
from models.appointment import Appointment
from models.owner import *
from models.animal import *
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository

def save(new_appointment):
    sql = "INSERT INTO appointments (start_time, end_time, appointment_date, animal_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [new_appointment.start_time, 
    new_appointment.end_time, new_appointment.appointment_date, new_appointment.animal.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    new_appointment.id = id

def select_all():
    appointments = []
    
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    
    for result in results:
        animal = animal_repository.select(result["animal_id"])
        
        appointment = Appointment(
            result["start_time"], 
            result["end_time"],
            result["appointment_date"], 
            animal, 
            result["id"])
        appointments.append(appointment)
    return appointments

def select(id):
    sql = "SELECT * FROM appointments WHERE id = %s"
    vaules = [id]
    result = run_sql(sql, vaules)[0]
    animal = animal_repository.select(result["animal_id"])
        
    if result is not None:
        appointment = Appointment(
        result["start_time"], 
        result["end_time"],
        result["appointment_date"], 
        animal, 
        result["id"]) 
    return appointment

def delete_all():
    sql = "DELETE * FROM appoinments"

def delete(id):
    sql = "DELETE FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(appointment):
    sql = "UPDATE appointments SET (start_time,end_time, appointment_date) = (%s, %s, %s) WHERE id = %s"
    vaules = [
        appointment.start_time, 
        appointment.end_time,
        appointment.appointment_date,
        appointment.id] 
    run_sql(sql, vaules)

# def show_appointments(date):
#     todays_appointments = []
#     sql = """SELECT start_time, end_time FROM appointments WHERE appointment_date = '%s'"""


