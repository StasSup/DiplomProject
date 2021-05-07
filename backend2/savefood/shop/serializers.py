from rest_framework import serializers
from . import models
from django.contrib.auth.models import User



#компания
class CompanyDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

#Карта компаний
class CompanyMapSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'address', 'lat', 'lon', 'id')

#Компании юзера
class CompanyUserDetatilSerializers(serializers.ModelSerializer):
    class Meta:
        models.Company
        fields = ('name', 'image', 'food_type', 'id')



#Еда
class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = '__all__'


#Еда для корзины
class FoodCartSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = ('name',  'price', 'quantity', 'company')


#Вывод информации о компании с едой
class CompanyInfoSerializers(serializers.ModelSerializer):
    food = FoodSerializers(source='company', many=True, read_only=True)
    class Meta:
        model = models.Company
        fields = ('name', 'image', 'description', 'address', 'food')



#телефон
class TelephoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = TelephoneSerializers()
    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'last_name', 'profile']