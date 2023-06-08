from rest_framework import serializers
from .models import Tag
from .models import Game
from .models import GameTag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'label')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'releaseYear', 'publisher', 'logoUrl')


class GameTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameTag
        fields = ('game', 'tag')
