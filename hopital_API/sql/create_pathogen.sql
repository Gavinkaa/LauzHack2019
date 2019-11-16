INSERT INTO Pathogens
SELECT :pathogen WHERE NOT EXISTS (SELECT 1 FROM Pathogens where seq=:pathogen);