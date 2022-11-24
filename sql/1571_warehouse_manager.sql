SELECT Warehouse.name AS warehouse_name, SUM(Warehouse.units*Products.Width*Products.Length*Products.Height) AS volume
FROM Warehouse, Products
WHERE Warehouse.product_id = Products.product_id
GROUP BY Warehouse.name;
