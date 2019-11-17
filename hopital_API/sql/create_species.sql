INSERT INTO Species (n, dangerous, depth)
SELECT :species, :dangerous, :depth WHERE NOT EXISTS (SELECT 1 FROM Species where n=:species);
