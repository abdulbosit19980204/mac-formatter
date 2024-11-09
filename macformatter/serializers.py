from rest_framework import serializers


class TextFormatSerializer(serializers.Serializer):
    # text = aa:11:bb:22:cc:33
    text = serializers.CharField(max_length=17)
