from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer