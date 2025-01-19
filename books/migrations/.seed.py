from pymongo import MongoClient
from datetime import datetime, date

client = MongoClient("mongodb://localhost:27017/")
db = client["book_db"]
collection = db["book"]

books = [
    
   {
    "title": "1984",
    "author": "George Orwell",
    "published_date": "1949-06-08",
    "genre": "Distopía",
    "price": 12.99
  },
  {
    "title": "Cien años de soledad",
    "author": "Gabriel García Márquez",
    "published_date": "1967-05-30",
    "genre": "Realismo mágico",
    "price": 14.99
  },
  {
    "title": "El código Da Vinci",
    "author": "Dan Brown",
    "published_date": "2003-03-18",
    "genre": "Misterio",
    "price": 10.99
  },
  {
    "title": "Orgullo y prejuicio",
    "author": "Jane Austen",
    "published_date": "1813-01-28",
    "genre": "Romance",
    "price": 9.99
  },
  {
    "title": "Dune",
    "author": "Frank Herbert",
    "published_date": "1965-08-01",
    "genre": "Ciencia ficción",
    "price": 15.49
  },
  {
    "title": "Drácula",
    "author": "Bram Stoker",
    "published_date": "1897-05-26",
    "genre": "Terror",
    "price": 8.99
  },
  {
    "title": "Los pilares de la Tierra",
    "author": "Ken Follett",
    "published_date": "1989-10-01",
    "genre": "Histórico",
    "price": 16.99
  },
  {
    "title": "El arte de la guerra",
    "author": "Sun Tzu",
    "published_date": "0500-01-01",
    "genre": "Estrategia",
    "price": 7.99
  },
  {
    "title": "El Hobbit",
    "author": "J.R.R. Tolkien",
    "published_date": "1937-09-21",
    "genre": "Fantasía",
    "price": 13.99
  },
  {
    "title": "Sapiens: De animales a dioses",
    "author": "Yuval Noah Harari",
    "published_date": "2011-09-04",
    "genre": "Divulgación científica",
    "price": 18.99
  }
]

collection.insert_many(books)
print("Datos insertados en MongoDB")
