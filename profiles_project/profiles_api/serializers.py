from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ sample serializer"""
    name = serializers.CharField(max_length = 10)
