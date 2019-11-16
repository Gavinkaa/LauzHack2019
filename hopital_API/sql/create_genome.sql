INSERT INTO Genomes (n)
SELECT :seq WHERE NOT EXISTS (SELECT 1 FROM Genome where seq=:seq);