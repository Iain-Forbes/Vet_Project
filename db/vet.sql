DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS animals;



CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    address VARCHAR
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    date_of_birth DATE NOT NULL DEFAULT CURRENT_DATE,
    animal_type VARCHAR,
    treatment_notes VARCHAR
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    appointment_time VARCHAR, appointment_date VARCHAR,
    animal_id SERIAL REFERENCES animals(id),
    owner_id SERIAL REFERENCES owners(id)
);




