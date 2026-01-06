# Write your MySQL query statement below

-- SELECT * FROM patients WHERE conditions REGEXP '\\bDIAB1'

select * from patients
where conditions like '% DIAB1%' or conditions like 'DIAB1%'
order by patient_id