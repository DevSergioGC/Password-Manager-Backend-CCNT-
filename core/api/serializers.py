from rest_framework import serializers
from .models import Folders, Items, User

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
            'full_name',
            'master_pwd',            
        ]    