-- Pair Programming consultas multiples 4 
USE northwind ;

-- Ejercicio 1
/*Extraed información de los productos "Beverages". En este caso nuestro jefe nos pode que le devolvamos toda la 
información necesaria para identificar un tipo de producto. En concreto, tienen especial interés por los productos con categoría "Beverages". 
Devuelve su el ID del producto, el nombre del producto y su ID de categoría.*/

SELECT products.product_id, products.product_name, categories.category_id, categories.category_name, categories.description
FROM products
INNER JOIN categories
ON products.category_id = categories.category_id
WHERE category_name = 'Beverages';
-- stá hecho pero tenemos dudas de que sea tan simple. Info redundante. 

-- Ejercicio 2
/*Extraed la lista de países donde viven los clientes, pero no hay ningún proveedor ubicado en ese país.Suponemos que si se 
trata de ofrecer un mejor tiempo de entrega a los clientes, 
entonces podría dirigirse a estos países para buscar proveedores adicionales.*/
SELECT customer_id, country
FROM customers
WHERE country NOT IN (	SELECT country
			FROM suppliers) ;
                    
-- Ejercicio 3
/*Extraer los clientes que compraron mas de 20 articulos "Grandma's Boysenberry Spread"Extraed una lista de pedidos y sus clientes que pidieron más de 20 
artículos del producto "Grandma's Boysenberry Spread" (ProductID 6) en un solo pedido.*/

                                        
SELECT customer_id
FROM customers
WHERE customer_id = (SELECT order_id
		    FROM orders
		    WHERE order_id = (SELECT order_id, product_id, quantity
				      FROM orderdetails
                                      WHERE order_id = 6));		
										

-- Ejercicio 4. SUBCONSULTA EN WHERE. DEMASIADO SIMPLE?
/*Extraed los 10 productos mas caros. Nos siguen pidiendo más queries correlacionadas. En este caso 
queremos saber cuáles son los 10 productos más caros. .

SELECT unit_price, product_id
FROM orderdetails
GROUP BY product_id
ORDER BY unit_price DESC
LIMIT 10; 



-- Ejercicio 5. BONUS!!
/* Qué producto es más popular. Extraed cuál es el producto que más ha sido comprado y la cantidad que 
se compró*/
