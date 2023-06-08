from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TagSerializer
from .models import Tag
from .serializers import GameSerializer
from .models import Game
from .serializers import GameTagSerializer
from .models import GameTag

# Create your views here.


class TagView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class GameView(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameTagView(viewsets.ModelViewSet):
    serializer_class = GameTagSerializer
    queryset = GameTag.objects.all()
