INSERT INTO GenomesMatchSpecies
SELECT Genomes.id, Species.id
FROM Genomes INNER JOIN Species
ON Genomes.seq=:gen AND Species.n=:species
WHERE NOT EXISTS
(SELECT 1 FROM GenomesMatchSpecies WHERE
genomeID=Genomes.id AND speciesID=Species.id
);