from flask import Flask, render_template, Blueprint, redirect, request 
from models.owner import Owner
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.appointment_repository as appointment_repository


owners_blueprint = Blueprint('owner', __name__)

# INDEX
# GET '/owners
@owners_blueprint.route("/owners", methods=['GET'])
def owner():  
    owners = owner_repository.select_all()
    return render_template("owners/index.html", all_owners=owners)

# NEW
# GET '/owners/new'
@owners_blueprint.route("/owners/new", methods=['GET'])
def new_owner():
    return render_template("owners/new.html")

@owners_blueprint.route("/owners/<id>")
def show_owner(id):
    owner = owner_repository.select(id)
    return render_template("owners/show.html", owner=owner)

@owners_blueprint.route("/owners", methods=["POST"])
def create_owners():
    name = request.form["name"]
    address = request.form["address"]
    new_owner = Owner(name, address)
    owner_repository.save(new_owner)
    return redirect("/owners")

@owners_blueprint.route("/owners/<id>")
def show_owners(id):
    owner = owner_repository.select(id)
    owned_animals = animal_repository.display_animals_owned(id)
    return render_template("owners/show.html", owner=owner, owned_animals=owned_animals)



@owners_blueprint.route("/owners/<id>/edit")
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template("owners/edit.html", owner=owner)


@owners_blueprint.route("/owners/<id>", methods=["POST"])
def update_owner(id):
    name = request.form["name"]
    address = request.form["address"]
    new_owner = Owner(name, address, id)
    owner_repository.update(owner)
    return redirect("/owners")


@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete_owners(id):
    owner_repository.delete(id)
    return redirect("/owners")