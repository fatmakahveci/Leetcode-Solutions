SELECT Users.name AS name, SUM(Transactions.amount) AS balance
FROM Users LEFT JOIN Transactions 
ON Users.account=Transactions.account
GROUP BY name HAVING balance>10000;
