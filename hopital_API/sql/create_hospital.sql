INSERT INTO Hospitals (n)
SELECT :hospital WHERE NOT EXISTS (SELECT 1 FROM Hospitals where n=:hospital);