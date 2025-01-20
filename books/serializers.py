from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
    genre = serializers.CharField(max_length=100)
    price = serializers.FloatField()