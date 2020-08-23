# Prueba Técnica Desarrollador Junior
This repo contains the challenge of **TSAKANA** for the job offer Python Developer Junior.

Esta prueba consiste en 2 apartados, Conocimientos en Python para desarrollo web y prueba de lógica.


## Requirements
> Python version 3.x


## Reto Python para desarrollo Web

La distribuidora **Sancho Limitada**, se especializa en la venta de ropa (retail) para caballero. Lo ha contratado como desarrollador para realizar un aplicativo web responsive, sobre MySQL, el cual permitirá registrar clientes (*cédula, nombre, dirección, teléfono y foto*), productos (*código del producto, categoría, nombre, precio, cantidad en bodega, estado -activo, inactivo-*) y facturas (*código de la factura, cliente que realiza la compra, productos, cantidad de productos, fecha de compra, valor total y método de pago*). Se debe poder: 

- Registrar y Editar Productos 
- Registrar y Editar Clientes 
- Registrar y Editar Facturas 
- Listar Productos 
- Listar Clientes 
- Listar Facturas 
- Desactivar productos (*dejando de aparecer en el listado*)
- Eliminar Clientes
- Listar clientes ordenados por cantidad de compras realizadas (factura = compra)

Se le solicita que junto a este desarrollo facilite un servicio API para consultar facturas por código, el cuál recibe un código de factura y retorna el valor total, ya que los clientes de la empresa deben conectar su sistema contable a este servicio.


## Prueba de Lógica 

Uno de los algoritmos más básicos en criptografía es el **cifrado César**, que fue utilizado por *Julio César* para comunicarse con sus generales, y que consiste en dado un texto, por cada una de las letras del texto, añadirle un desplazamiento para conseguir una nueva letra diferente de la original. Ejemplo: 

Si asignamos el número 1 a la primera letra del abecedario, A; 2 a la siguiente, B, etc., 

imagina que tenemos el siguiente mensaje: 
`ABC`
`123` 

Si aplicamos un desplazamiento de 3, buscaremos cuál es la letra en el abecedario que se corresponde: 

`DEF` 
`456`

`ABC` se ha convertido en `DEF` porque hemos sumado un desplazamiento de 3. También podríamos aplicar otros tipos de desplazamiento como los negativos.
Por ejemplo, para el desplazamiento -1 y el mensaje original `ABC` tendríamos un mensaje cifrado de: `ZAB`. 

Escribe una función que, dado un mensaje cifrado y un desplazamiento, calcule y devuelva el mensaje original. 

**Nota.** Usar como alfabeto de entrada, el alfabeto español en mayúsculas.


## AUTHOR
**Jackson Moreno**


## LICENCE
**MIT**

