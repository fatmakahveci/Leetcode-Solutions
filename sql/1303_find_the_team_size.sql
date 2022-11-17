SELECT employee_id, team_size
FROM Employee,
     (SELECT team_id, COUNT(*) AS team_size FROM Employee GROUP BY team_id) AS Team
WHERE Employee.team_id = Team.team_id;
