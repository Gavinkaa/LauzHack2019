INSERT INTO Genomes (seq)
SELECT :seq WHERE NOT EXISTS (SELECT 1 FROM Genomes where seq=:seq);