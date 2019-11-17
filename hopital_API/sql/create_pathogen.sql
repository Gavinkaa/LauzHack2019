INSERT INTO Pathogens (seq)
SELECT :pathogen WHERE NOT EXISTS (SELECT 1 FROM Pathogens where seq=:pathogen);