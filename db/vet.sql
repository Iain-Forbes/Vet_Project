DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners; (
    id SERIAL PRIMARY KEY
    name VARCHAR(225),
    contact_details VARCHAR(225),
)

CREATE TABLE animals; (
    id SERIAL PRIMARY KEY
    name VARCHAR(225),
    date_of_birth VARCHAR(225),
    animal_type VARCHAR(225)
    treatment_notes TEXT
    owner_id SERIAL REFERENCES owner(id),
    vet_id SERIAL REFERENCES vet(id),
    
)

CREATE TABLE vets; (
    id SERIAL PRIMARY KEY
    name VARCHAR(225),
    contact_details VARCHAR(225),
)

