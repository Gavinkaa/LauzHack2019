INSERT INTO GenomesMatchPathogens
SELECT Genomes.id, Pathogens.id
FROM Genomes INNER JOIN Pathogens
ON Genomes.seq=:genome AND Pathogens.seq=:pathogen
WHERE NOT EXISTS
(SELECT 1 FROM GenomesMatchPathogens WHERE
genomeID=Genomes.id AND pathogenID=Pathogen.id
);