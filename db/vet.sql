DROP TABLE IF EXISTS owners CASCADE;
DROP TABLE IF EXISTS animals CASCADE;
DROP TABLE IF EXISTS appointments CASCADE;


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

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    appointment_time VARCHAR, 
    appointment_date VARCHAR,
    owner_id SERIAL REFERENCES owners(id),
    animal_id SERIAL REFERENCES animals(id)
    
);




