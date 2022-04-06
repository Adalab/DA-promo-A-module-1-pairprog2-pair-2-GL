USE northwind ;

-- Ejercicio 1
/*Extraed información de los productos "Beverages".
En este caso nuestro jefe nos pode que le devolvamos toda la 
información necesaria para identificar un tipo de producto. En concreto, 
tienen especial interés por los productos con categoría "Beverages". 
Devuelve su el ID del producto, el nombre del producto y su ID de 
categoría.*/

SELECT products.product_id, products.product_name, categories.category_id, categories.category_name, categories.description
FROM products
INNER JOIN categories
ON products.category_id = categories.category_id
WHERE category_name = 'Beverages';
-- stá hecho pero tenemos dudas de que sea tan simple. Info redundante. 


/*Extraed la lista de países donde viven los clientes, pero no hay ningún 
proveedor ubicado en ese país.
Suponemos que si se trata de ofrecer un mejor tiempo de entrega a los 
clientes, entonces podría dirigirse a estos países para buscar 
proveedores adicionales.
Extraer los clientes que compraron mas de 20 articulos "Grandma's 
Boysenberry Spread"
Extraed una lista de pedidos y sus clientes que pidieron más de 20 
artículos del producto "Grandma's Boysenberry Spread" �ProductID 6� en 
un solo pedido.
Extraed los 10 productos mas caros
Nos siguen pidiendo más queries correlacionadas. En este caso 
queremos saber cuáles son los 10 productos más caros.
Qué producto es más popular.
Extraed cuál es el producto que más ha sido comprado y la cantidad que 
se compró*/