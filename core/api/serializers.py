from rest_framework import serializers
from .models import Folders, Items
from rest_framework.authtoken.views import Token
from django.contrib.auth.models import User

class FolderSerializer(serializers.ModelSerializer):    
    class Meta:
        
        model = Folders
        fields = "__all__"
        
        extra_kwargs = {'user': {            
            'required': False
        }}
            
class ItemSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Items
        fields = "__all__"
        
        extra_kwargs = {
            'user': {'required': False},
            'folder': {'required': False}
        }
               
class UserSerializer(serializers.ModelSerializer):
    class Meta:        
        model = User
        fields = [
            'id',
            'username',
            'first_name',
        ]    
        
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }} 