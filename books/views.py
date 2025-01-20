from pymongo import MongoClient
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from datetime import datetime
from bson import ObjectId
from rest_framework.pagination import PageNumberPagination

# Conexión a MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")  # Conexio a MongoDB
    db = client["book_db"]  # Nombre de la base de datos
    collection = db["book"]  # Nombre de la colección
except Exception as ex:
    print("error de conexion: {}".format(ex))

class BookList(APIView, PageNumberPagination):
    page_size = 5  
    def get(self, request):
        books = list(collection.find({}))  # Obtener todos los libros
        paginated_books = self.paginate_queryset(books, request, view=self)
        serializer = BookSerializer(paginated_books, many=True)  # Serializa la lista de libros
        
        return self.get_paginated_response(serializer.data)
    
    def post(self, request):
        # Agregar libros a la colección 'books'
        new_book = request.data  # Datos de la insercion en Json
        collection.insert_one(new_book)  # Inserta un nuevo documento en la colección
        return Response({"message": "Book added successfully"}, status=201)


class BookDetail(APIView):
    """Operaciones CRUD en un libro específico"""

    def get(self, request, book_id):
        """Obtener un libro por su ID."""
        book = collection.find_one({"_id": ObjectId(book_id)})
        if book:
            book["_id"] = str(book["_id"])
            return Response(book, status=200)
        return Response({"error": "Book not found"}, status=404)

    def put(self, request, book_id):
        """Actualizar completamente un libro por su ID"""
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            result = collection.update_one(
                {"_id": ObjectId(book_id)}, {"$set": request.data}
            )
            if result.modified_count > 0:
                return Response({"message": "Book updated successfully"}, status=200)
            return Response({"message": "No changes made"}, status=200)

        return Response(serializer.errors, status=400)

    def patch(self, request, book_id):
        """Actualizar parcialmente un libro por su ID"""
        data = request.data
        result = collection.update_one(
            {"_id": ObjectId(book_id)}, {"$set": data}
        )
        if result.modified_count > 0:
            return Response({"message": "Book partially updated"}, status=200)
        return Response({"message": "No changes made"}, status=200)

    def delete(self, request, book_id):
        """Eliminar un libro por su ID"""
        result = collection.delete_one({"_id": ObjectId(book_id)})
        if result.deleted_count > 0:
            return Response({"message": "Book deleted successfully"}, status=200)
        return Response({"error": "Book not found"}, status=404)
    

class AveragePriceByYear(APIView):
    """Obtener el precio promedio x año específico"""

    def get(self, request, year):
        """Calcula el precio promedio de los libros publicados en el año dado"""
        try:
            year = int(year)  # Convertir en estero el año
            pipeline = [
                {
                    "$match": {
                        "published_date": {
                            "$gte": f"{year}-01-01",
                            "$lt": f"{year+1}-01-01"
                        }
                    }
                },
                {
                    "$group": {
                        "_id": None,  # No se requiere agrupar por ningún campo en específico
                        "average_price": {"$avg": "$price"}
                    }
                },
                {
                    "$project": {
                        "_id": 0,  # se oculta el campo _id
                        "year": year,
                        "average_price": {"$round": ["$average_price", 2]}  # Redondear a 2 decimales
                    }
                }
            ]

            result = list(collection.aggregate(pipeline))

            if not result:
                return Response({"message": f"No books found for year {year}"}, status=404)
            return Response(result[0], status=200)

        except ValueError:
            return Response({"error": "Invalid year format. Must be an integer."}, status=400)