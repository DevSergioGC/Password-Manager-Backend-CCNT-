from rest_framework import serializers
from .models import Folders, Items, User
from rest_framework.authtoken.views import Token

class FolderSerializer(serializers.ModelSerializer):    
    class Meta:
        
        model = Folders
        fields = [
            'id_folders',
            'name',
        ]
            
class ItemSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Items
        fields = [
            'id_item',
            'name',
            'password',
            'description',
            'url',
            'id_folders',
            'id_user',
        ]
               
class UserSerializer(serializers.ModelSerializer):
    class Meta:        
        model = User
        fields = [
            'id_user',
            'username',
            'name',
            'password',            
        ]    
        
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}
        
    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        
        return user