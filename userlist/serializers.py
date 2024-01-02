import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *


# class UserListModel:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = "__all__"




# def encode():
#     model = UserListModel('Sasha', 'Polovinko')
#     model_sr = UserListSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"first_name":"Sasha","last_name":"Polovinko"}')
#     data = JSONParser().parse(stream)
#     serializer = UserListSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
    
