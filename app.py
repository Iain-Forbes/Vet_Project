from flask import Flask, render_template, Blueprint

# from controllers.owner_controller import owner_blueprint
# from controllers.appointment_controller import vet_blueprint
from controllers.animal_controller import animals_blueprint

app = Flask(__name__)

# app.register_blueprint(vet_blueprint)
# app.register_blueprint(owner_blueprint)
app.register_blueprint(animals_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run
