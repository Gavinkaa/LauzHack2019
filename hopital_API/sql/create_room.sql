INSERT INTO Rooms (hospitalID, n)
SELECT id, :room FROM Hospitals
WHERE n=:hospital AND NOT EXISTS(SELECT 1 FROM Rooms where n=:room);