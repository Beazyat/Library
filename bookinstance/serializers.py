from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings 


from .models import *


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title',
            'summary',
            'isbn',
            'author',
        )


class jwtserializer(serializers.ModelSerializer):
    UserModel = User
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
  
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token
    
    class Meta:
        model = User
        fields = '__all__'