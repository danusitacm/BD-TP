# Kevda Database
Kevda Database es una base de datos diseñada registra las com-
pras y venta de juegos e íıtems entre usuario, así como para almacenar y administrar reseñas de juegos e usuarios como vendedores. Este proyecto utiliza Python con las librerías Faker y el motor de base de datos PostgreSQL. Además, se utiliza pgAdmin, DBeaver, explain.dalibo.com y Power Architect SQL como herramientas para administrar, consultar, analizar el rendimiento y modelar la base de datos.
## Instalación
### Base de Datos
Clona el repositorio de Kevda Database:
```sh
git clone https://github.com/tu-usuario/kevda-database.git
```
Ejecuta el script challenge7_Cristaldo_March.sql en tu herramienta de administración de bases de datos para crear las tablas necesarias. Puedes utilizar el siguiente comando en la línea de comandos:
```sh
psql -U [usuario] -d [nombre_de_la_base_de_datos] -f challenge7_Cristaldo_March.sql
```
O simplemente abra el archivo en el pgAdmin.

### Script de Datos
Este proyecto incluye un script de carga de datos aleatorio, para ejecutar el script, introduzca el siguiente comando.
```sh
python script/main.py
```
##  Características
* Gestión de usuarios: Registra nuevos usuarios.
* Compra y venta de juegos: Registra transacciones de compra y venta de juegos.
* Gestión de juegos: Agrega nuevos juegos a la base de datos, actualiza información, precios, etc.
* Reseñas de juegos: Permite a los usuarios dejar reseñas y calificaciones para los juegos.
* Compra y venta de items: Registra transacciones de compra y venta de coleccionables entre jugadores.
* Gestion de eventos: Agrega nuevos eventos a la base de datos, actualiza información, fechas, etc.

## Triggers
Kevda Database incluye los siguientes triggers:

1. Trigger Antisolapamiento de eventos: Este trigger controla que un evento no puede comenzar si existe otro evento entre las fechas especificadas.
2. Trigger user no compra a si mismo: controla que un usuario
no puede comprar un item a si mismo.
3. Trigger user no review si no compro: controla que un usuario
no puede dejar un review si no tiene el juego.
4. Trigger calculo precio compra: calcula el precio de un juego si
esta en descuento.

## Reportes
Kevda Database proporciona los siguientes reportes:

1. Funcion getGamesFromEvent: Trae los juegos mas vendidos de un evento
2. Funcíon getActiveUserFromCommunity: Trae los usuarios mas
activos de una comunidad, definimos la cantidad minima de reviews
de un usuario para que sea considerado activo.
3. Funcion getuserhistory: Trae nombre, juegos que compro, fecha,
evento que compro, si compro para regalo, a quien le regalo y su
review si dejo.

## Créditos
- Faker: Librería utilizada para generar datos de ejemplo.
- PostgreSQL: Motor de base de datos utilizado en el proyecto.
- pgAdmin: Herramienta de administración de PostgreSQL.
- DBeaver: Herramienta de administración y consulta de bases de datos.
- explain.dalibo.com: Herramienta de análisis de rendimiento de consultas.
- Power Architect SQL: Herramienta de modelado de bases de datos.

