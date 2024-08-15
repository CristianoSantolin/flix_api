from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from actors.serializer import ActorSerializer
from genres.serializer import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.review.aggregate(Avg('stars'))['stars__avg']
        return rate if rate is not None else None


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model= Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.review.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None