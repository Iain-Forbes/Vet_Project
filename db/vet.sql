DROP TABLE IF EXISTS appointments CASCADE;
DROP TABLE IF EXISTS animals CASCADE;
DROP TABLE IF EXISTS owners CASCADE;



CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    address VARCHAR
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    date_of_birth VARCHAR,
    animal_type VARCHAR,
    treatment_notes VARCHAR,
    owner_id SERIAL REFERENCES owners(id)
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    appointment_time VARCHAR, 
    appointment_date VARCHAR,
    owner_id SERIAL REFERENCES owners(id),
    animal_id SERIAL REFERENCES animals(id)
    
);




