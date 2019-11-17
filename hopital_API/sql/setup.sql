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

CREATE TABLE Pathogens (
    id INTEGER PRIMARY KEY,
    seq TEXT UNIQUE NOT NULL
);

CREATE TABLE GenomesMatchPathogens (
    genomeID INTEGER NOT NULL,
    pathogenID INTEGER NOT NULL,
    PRIMARY KEY (genomeID, pathogenID),
    FOREIGN KEY (genomeID) REFERENCES genomes(genomeID),
    FOREIGN KEY (pathogenID) REFERENCES pathogen(pathogenID)
);

CREATE TABLE GenomeRoom (
    genomeID INTEGER NOT NULL,
    roomID INTEGER NOT NULL,
    PRIMARY KEY (genomeID, roomID),
    FOREIGN KEY (genomeID) REFERENCES genomes(genomeID),
    FOREIGN KEY (roomID) REFERENCES rooms(roomID)
);


