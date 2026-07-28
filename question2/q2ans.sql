-- Question 2(a)
-- Count the number of Acacia plant species

SELECT COUNT(DISTINCT species) AS acacia_species_count
FROM taxonomy
WHERE species LIKE 'Acacia%';


-- Question 2(b)
-- Wheat species with the longest DNA sequence

SELECT
    t.species,
    MAX(r.length) AS longest_dna_sequence
FROM taxonomy t
JOIN rfamseq r
ON t.ncbi_id = r.ncbi_id
WHERE t.species LIKE '%wheat%'
   OR t.species LIKE 'Triticum%'
GROUP BY t.species
ORDER BY longest_dna_sequence DESC
LIMIT 1;


-- Question 2(c)
-- 9th page (15 results per page)

SELECT
    f.rfam_acc AS family_accession_id,
    f.description AS family_name,
    MAX(r.length) AS max_dna_sequence_length
FROM rfamseq r
JOIN full_region fr
    ON r.rfamseq_acc = fr.rfamseq_acc
JOIN family f
    ON fr.rfam_acc = f.rfam_acc
WHERE r.length > 1000000
GROUP BY f.rfam_acc, f.description
ORDER BY max_dna_sequence_length DESC
LIMIT 120,15;