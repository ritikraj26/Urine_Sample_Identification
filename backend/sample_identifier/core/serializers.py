from rest_framework import serializers

class ColorSerializer(serializers.Serializer):
    R = serializers.IntegerField()
    G = serializers.IntegerField()
    B = serializers.IntegerField()
