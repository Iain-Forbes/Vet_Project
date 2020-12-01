from flask import Flask, render_template, Blueprint

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.appointment_repository as appointment_repository

from controllers.owner_controller import owners_blueprint
from controllers.appointment_controller import appointments_blueprint
from controllers.animal_controller import animals_blueprint

app = Flask(__name__)

app.register_blueprint(appointments_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(animals_blueprint)

@app.route('/')
def home():
    owners = owner_repository.select_all()
    animals = animal_repository.select_all()
    appointments = appointment_repository.select_all()
    return render_template('index.html', owners=owners, animals=animals, appointments=appointments)

if __name__ == '__main__':
    app.run
