SELECT 
    Product.ProductID,
    Product.ProductName,
    Supplier.SupplierName,
    Supplier.Country 
FROM Products Product
	INNER JOIN Suppliers Supplier
    	ON Product.SupplierID = Supplier.SupplierID
WHERE Product.ProductID >= 20
ORDER BY Product.ProductID DESC;