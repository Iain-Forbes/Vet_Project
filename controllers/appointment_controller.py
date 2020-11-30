from flask import Flask, render_template, Blueprint, redirect, request 
from models.appointment import Appointment
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.appointment_repository as appointment_repository

appointments_blueprint = Blueprint('appointment', __name__)

# INDEX
# GET '/appointments
@appointments_blueprint.route("/appointments", methods=['GET'])
def owner():  
    appointments = appointment_repository.select_all()
    owners = owner_repository.select_all()
    animals = animal_repository.select_all()
    return render_template("appointments/index.html", all_appointments=appointments, owners=owners, animals=animals)

# NEW
# GET '/appointments/new'
@appointments_blueprint.route("/appointments/new", methods=['GET'])
def new_appointment():
    owners = owner_repository.select_all()
    animals = animal_repository.select_all()
    return render_template("appointments/new.html", owners=owners, animals=animals)
    return render_template("appointments/new.html")

#Show Appointments
@appointments_blueprint.route("/appointments/<id>")
def show_appointments(id):
    owner_appointment = appointment_repository.all_appointments(id)
    appointment = appointment_repository.select(id)
    return render_template("appointments/show.html", appointment=appointment, owner_appointment=owner_appointment)

#Make Appointments
@appointments_blueprint.route("/appointments", methods=["POST"])
def create_appointment():
    appointment_time = request.form["appointment_time"]
    appointment_date = request.form["appointment_date"]
    owner  = owner_repository.select(request.form["owner_id"])
    animal = animal_repository.select(request.form["animal_id"])
    new_appointment = Appointment(
        appointment_time, 
        appointment_date, 
        owner, 
        animal)
    appointment_repository.save(new_appointment)
    return redirect("/appointments")


#Edit Appointments
@appointments_blueprint.route("/appointments/<id>/edit")
def edit_appointment(id):
    owners = owner_repository.select_all()
    animals = animal_repository.select_all()
    appointment = appointment_repository.select(id)
    return render_template("appointments/edit.html", appointment=appointment, owners=owners, animals=animals)

#Update Appointments
@appointments_blueprint.route("/appointments/<id>", methods=["POST"])
def update_appointment(id):
    appointment_time = request.form  ["appointment_time"]
    appointment_date = request.form["appointment_date"]
    animal = animal_repository.select(request.form["animal_id"])
    owner  = owner_repository.select(request.form["owner_id"])
    appointment = Appointment(
        appointment_time, 
        appointment_date, 
        owner, 
        animal
        )
    appointment_repository.update(appointment )
    return redirect("/appointments")


#Delete Appointments
@appointments_blueprint.route("/appointments/<id>/delete", methods=["POST"])
def delete_appointment(id):
    appointment_repository.delete(id)
    return redirect("/appointments")
