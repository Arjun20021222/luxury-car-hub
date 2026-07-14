from rest_framework import serializers
from showroom.models import Car
from student.models import Student
from django.contrib.auth import get_user_model

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

User=get_user_model()
        
class RegisterSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=[
            "username",
            "email",
            "password",
            "password2"
        ]
    
    def validate(self, attrs):
        if attrs["password"]!=attrs["password2"]:
            raise serializers.ValidationError(
                {"password":"Password do not match"}
            )
        return attrs
    
    def create(self,validated_data):
        validated_data.pop("password2")
        user=User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
    
