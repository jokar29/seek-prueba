from rest_framework.test import APITestCase
from rest_framework import status
from pymongo import MongoClient

# Conexion a MongoDB para pruebas
client = MongoClient("mongodb://localhost:27017/")
db = client["test_book_db"]  # Base de datos de pruebas
collection = db["books"]

class BookAPITestCase(APITestCase):
    """Pruebas unitarias para la API de libros"""

    def setUp(self):
        # Limpiar la colección antes de cada prueba
        collection.delete_many({})

        # Insertar libros de prueba
        collection.insert_many([
            {"title": "Book 1", "author": "Author 1", "published_date": "2023-01-10", "genre": "Fiction", "price": 25.99},
            {"title": "Book 2", "author": "Author 2", "published_date": "2022-07-15", "genre": "Sci-Fi", "price": 19.99}
        ])

    def test_get_books_list(self):
        """Obtener la lista de libros de prueba"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertGreater(len(response.data["results"]), 0)  # Verifica que hay al menos 1 libro

    def test_create_book(self):
        """Crear un nuevo libro de prueba"""
        new_book = {
            "title": "Book 3",
            "author": "Author 3",
            "published_date": "2024-02-20",
            "genre": "Mystery",
            "price": 29.99
        }
        response = self.client.post("/api/books/", new_book, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Book added successfully")

    def tearDown(self):
        """Eliminar la base de datos despues de cada prueba"""
        collection.delete_many({})