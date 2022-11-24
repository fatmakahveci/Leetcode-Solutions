SELECT customer_id, COUNT(visit_id) as count_no_trans 
FROM Visits
WHERE NOT EXISTS (SELECT visit_id FROM Transactions
	              WHERE Transactions.visit_id = Visits.visit_id)
GROUP BY customer_id;
