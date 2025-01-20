# seek-prueba libros

* Book API - Django REST Framework & MongoDB

* Descripción:
Esta API permite realizar acciones CRUD con la informacion de libros utilizando Django Rest Framework (DRF) y MongoDB y cuenta con una funcionalidad para calcular el precio promedio de los libros publicados en un año específico, paginación y pruebas unitarias.

* Características
- CRUD: Crear, leer, actualizar y eliminar libros
- MongoDB: Base de datos NoSQL para almacenamiento de libros
- Serialización: Uso de pymongo y rest_framework.serializers
- Paginación: Implementada con PageNumberPagination
- Pruebas unitarias: Incluye tests para validar la API.

Tecnologías Utilizadas
Python 3.x
Django 4.x
Django Rest Framework (DRF)
MongoDB
Pymongo
Postman (para pruebas)

Instalación y Configuración
1- Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/jokar29/seek-prueba.git
2- Crear un entorno virtual y activarlo
python -m venv venv
venv\Scripts\activate
3- Instalar dependencias
pip install -r requirements.txt 
4️- Configurar MongoDB
Asegúrate de que MongoDB esté corriendo localmente en mongodb://localhost:27017/.
Si necesitas modificar la conexión, edita views.py:

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["book_db"]
collection = db["books"]
5- Ejecutar el servidor
python manage.py runserver
Ahora puedes acceder a la API en http://127.0.0.1:8000/api/books/.

Endpoints de la API
Método	URL	Descripción
GET	/api/books/	Listar todos los libros (paginados).
POST /api/books/	Agregar un nuevo libro.
GET	/api/books/{id}/	Obtener detalles de un libro específico.
PUT	/api/books/{id}/	Actualizar un libro.
DELETE /api/books/{id}/	Eliminar un libro.
GET	/api/books/average-price/?year=2023	Obtener precio promedio de libros en un año.

* Pruebas Unitarias
Las pruebas se encuentran en books/tests.py. 
Para ejecutarlas: python manage.py test books

* Ejemplo de Uso
Agregar un libro (POST /api/books/) en Postman:
POST http://127.0.0.1:8000/api/books/ \
{
    "title": "Django for Beginners",
    "author": "William S. Vincent",
    "published_date": "2023-05-10",
    "genre": "Programming",
    "price": 39.99
}
* Ingresar libros de prueba:
cd books
ejecutar: python .seed.py

* Autor
Desarrollado por Johann José Carvajal F. - 2025.