INSERT INTO GenomeRoom
SELECT Genomes.id, Rooms.id
FROM Genomes INNER JOIN Rooms
ON Genomes.seq=:genome AND Rooms.n=:room
WHERE NOT EXISTS
(SELECT 1 FROM GenomeRoom WHERE
genomeID=Genomes.id AND roomID=Rooms.id
);