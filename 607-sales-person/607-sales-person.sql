/* Write your T-SQL query statement below */
SELECT name
	FROM SalesPerson 
	WHERE sales_id NOT IN (
							SELECT s.sales_id
							FROM Orders o
							JOIN Company c ON c.com_id = o.com_id
							JOIN SalesPerson s ON o.sales_id = s.sales_id
							WHERE c.name = 'RED')
