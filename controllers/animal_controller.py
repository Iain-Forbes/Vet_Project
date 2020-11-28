from flask import Flask, render_template, Blueprint, redirect, request 
from models.animal import Animal
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.appointment_repository as appointment_repository

animals_blueprint = Blueprint('animal', __name__)

# INDEX
# GET '/animals'
@animals_blueprint.route("/animals", methods=['GET'])
def animal():  
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals=animals)

# NEW
# GET '/animals/new'
@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    return render_template("animals/new.html")


# CREATE
@animals_blueprint.route("/animals", methods=["POST"])
def create_animal():
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    animal_type = request.form["animal_type"]
    treatment_notes = request.form["treatment_notes"]
    new_animal = Animal(name, date_of_birth, animal_type, treatment_notes)
    animal_repository.save(new_animal)
    return redirect("/animals")

# SHOW
@animals_blueprint.route("/animals/<id>")
def show_zombie(id):
    animal = animal_repository.select(id)
    return render_template("animals/show.html", animal=animal)



# EDIT
@animals_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    animal = animal_repository.select(id)
    return render_template('animals/edit.html', animal=animal)


# UPDATE
@animals_blueprint.route("/animals/<id>", methods=["POST"])
def update_animal(id):
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    animal_type = request.form["animal_type"]
    treatment_notes = request.form["treatment_notes"]
    new_animal = Animal(name, date_of_birth, animal_type, treatment_notes, id)
    animal_repository.update(animal)
    return redirect("/animals")


# DELETE
@animals_blueprint.route("/animals/<id>/delete", methods=["POST"])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect("/animals")

