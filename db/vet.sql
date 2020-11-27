DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;


CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    contact_details VARCHAR
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    date_of_birth DATE,
    animal_type VARCHAR,
    treatment_notes VARCHAR
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    appointment_time VARCHAR, appointment_date VARCHAR,
    animal_id SERIAL REFERENCES animals(id),
    owner_id SERIAL REFERENCES owners(id)
);




