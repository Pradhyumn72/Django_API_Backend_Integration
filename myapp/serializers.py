# from rest_framework import serializers

# class Student(serializers.Serializer):
#     name=serializers.CharField()
#     email=serializers.EmailField()
#     contact=serializers.CharField()
from rest_framework import serializers
from myapp.models import Studentt

class Student(serializers.ModelSerializer):
    class Meta:
        model = Studentt
        fields = ['id', 'name', 'email', 'contact']
