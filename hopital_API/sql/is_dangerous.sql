SELECT 1 WHERE EXISTS (
    SELECT 1 FROM Genomes
    INNER JOIN GenomesMatchSpecies ON Genomes.id=GenomesMatchSpecies.genomeID
    INNER JOIN Species ON Species.id=GenomesMatchSpecies.speciesID
    WHERE Genomes.seq=:gen AND Species.dangerous AND Species.depth >=:depth
);
