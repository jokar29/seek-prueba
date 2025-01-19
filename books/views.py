from pymongo import MongoClient
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from datetime import datetime

# Conexión a MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")  # Conexio a MongoDB
    db = client["book_db"]  # Nombre de la base de datos
    collection = db["book"]  # Nombre de la colección
except Exception as ex:
    print("error de conexion: {}".format(ex))

class BookList(APIView):
    def get(self, request):
        books = list(collection.find({}))  # Obtener todos los libros
        books = list(collection.find({}, {"_id": 0}))  # Excluir _id si no quieres mostrarlo
        serializer = BookSerializer(books, many=True)  # Serializa la lista de libros
        return Response(serializer.data)
    
    def post(self, request):
        # Agregar libros a la colección 'books'
        new_book = request.data  # Datos de la insercion en Json
        collection.insert_one(new_book)  # Inserta un nuevo documento en la colección
        return Response({"message": "Book added successfully"}, status=201)
