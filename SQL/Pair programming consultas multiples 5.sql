-- Este es el pair programming multiples 5

USE northwind ;
-- Ejercicio 1
/*Extraed los pedidos con el máximo "OrderDate" para cada empleado.
Nuestro jefe quiere saber la fecha de los pedidos más recientes que ha gestionado cada empleado. Para eso nos pide que lo hagamos con una query correlacionada.*/

SELECT order_date, employee_id, order_id, required_date, customer_id
FROM orders AS o1
WHERE order_date = (SELECT MAX(order_date)
			FROM orders AS o2
                        WHERE o1.order_id = o2.order_id) ;


/*2.
Extraed el precio unitario (UnitPrice) de cada producto vendido.
Supongamos que ahora nuestro jefe quiere un informe de los productos más vendidos y su precio unitario. De nuevo lo tendréis que hacer con queries correlacionadas.*/
SELECT p.product_id, p.product_name, p.quantity_per_unit, p.unit_price AS precio_unitario, p.units_on_order, SUM(o.quantity) AS cantidades_vendidas
FROM products AS p
LEFT JOIN orderdetails AS o
ON p.product_id = o.product_id
GROUP BY p.product_id, p.product_name, p.quantity_per_unit
ORDER BY cantidades_vendidas DESC
LIMIT 10;
-- Los 10 productos más vendidos

                            
-- Hemos puesto más info de los productos vendidos por sugerencia de l@s profes (pista: profe con nombre de cantante( y en realidad cantante)). Sabemos que nos piden menos cosas.



/*3.
Ciudades que empiezan con "A" o "B"
Por un extraño motivo, nuestro jefe quiere que le devolvamos una tabla con aquelas compañias que están afincadas en ciudades que empiezan por "A" o "B". Necesita que le devolvamos la ciudad, el nombre de la compañia y el nombre de contacto.
4.
Número de pedidos que han hecho en las ciudades que empiezan con L
En este caso, nuestro objetivo es devolver los mismos campos que en la query anterior el número de total de pedidos que han hecho todas las ciudades que empiezan por "L".
5.
Todos los clientes cuyo "ContactTitle" no incluya "Sales".
Nuestro objetivo es extraer los clientes que no tienen el contacto "Sales" en su "ContactTitle". Extraer el nombre de contacto, su posisión (ContactTitle) y el nombre de la compañia.
6.
Todos los clientes que no tengan una "A" en segunda posición en su nombre.
Devolved unicamente el nombre de contacto.*/









