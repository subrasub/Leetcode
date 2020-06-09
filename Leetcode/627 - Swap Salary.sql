# Write your MySQL query statement below
UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' then 'f'
        ELSE 'm'
    END;
    