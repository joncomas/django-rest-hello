"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models


"""
Define he User Entity into your applcation model
"""
class User(models.Model):

    password = models.CharField(max_length=150, blank=False)
    email = models.CharField(max_length=150, blank=False)

"""
The UserSerializer is where you will specify what properties
from the ever User should be inscuded in the JSON response
"""
class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        # what fields to include?
        fields = ('id', 'password', 'email')