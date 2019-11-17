CREATE TABLE Hospitals (
    id INTEGER PRIMARY KEY,
    n TEXT UNIQUE NOT NULL
);

CREATE TABLE Rooms (
    id INTEGER PRIMARY KEY,
    hospitalID INTEGER NOT NULL,
    n TEXT UNIQUE NOT NULL,
    FOREIGN KEY (hospitalID) REFERENCES hospitals(hospitalID)
);

CREATE TABLE Genomes (
    id INTEGER PRIMARY KEY,
    seq TEXT UNIQUE NOT NULL
);

CREATE TABLE Species (
    id INTEGER PRIMARY KEY,
    n TEXT UNIQUE NOT NULL,
    dangerous INTEGER NOT NULL,
    depth INTEGER NOT NULL
);

CREATE TABLE GenomesMatchSpecies (
    genomeID INTEGER NOT NULL,
    speciesID INTEGER NOT NULL,
    PRIMARY KEY (genomeID, speciesID),
    FOREIGN KEY (genomeID) REFERENCES Genomes(genomeID),
    FOREIGN KEY (speciesID) REFERENCES Species(pathogenID)
);

CREATE TABLE GenomeRoom (
    genomeID INTEGER NOT NULL,
    roomID INTEGER NOT NULL,
    PRIMARY KEY (genomeID, roomID),
    FOREIGN KEY (genomeID) REFERENCES genomes(genomeID),
    FOREIGN KEY (roomID) REFERENCES rooms(roomID)
);


