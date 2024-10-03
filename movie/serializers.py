from rest_framework.serializers import ModelSerializer
from movie.models import Movie_data

class MovieDataSerializer(ModelSerializer):

    class Meta:
        model = Movie_data
        fields = "__all__"