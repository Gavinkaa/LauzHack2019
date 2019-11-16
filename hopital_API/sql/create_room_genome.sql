SELECT Rooms.id, Genomes.id
FROM Rooms INNER JOIN Genomes
ON Rooms.n=:room AND Genomes.seq=:genome;
