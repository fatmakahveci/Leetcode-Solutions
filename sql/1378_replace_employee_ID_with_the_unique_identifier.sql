SELECT emp_uni.unique_id, emp.name
FROM Employees AS emp LEFT JOIN EmployeeUNI AS emp_uni ON emp.id = emp_uni.id;
