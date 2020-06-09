-- https://leetcode.com/problems/duplicate-emails/
-- Write your MySQL query statement below
SELECT Email from Person GROUP BY Email HAVING COUNT(*)>1