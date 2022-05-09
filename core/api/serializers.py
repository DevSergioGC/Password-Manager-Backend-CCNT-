from rest_framework import serializers
from .models import Folders, Items, User

class FolderSerializer(serializers.Serializer):
    
    id_folders = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        
        return Folders.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        
        instance.id_folders = validated_data.get('id_folders', instance.id_folders)
        instance.name = validated_data.get('name', instance.name)
        
class ItemSerializer(serializers.Serializer):
    
    id_item = serializers.IntegerField()
    name = serializers.CharField(max_length=60)
    password = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=300)
    url = serializers.CharField(max_length=255)
    
    id_folders = serializers.IntegerField()
    id_user = serializers.IntegerField()
    
    def create(self, validated_data):
        
        return Items.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        
        instance.id_item = validated_data.get('id_item', instance.id_item)
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.description = validated_data.get('description', instance.description)
        instance.url = validated_data.get('url', instance.url)
        instance.id_folders = validated_data.get('id_folders', instance.id_folders)
        instance.id_user = validated_data.get('id_user', instance.id_user)
        
class UserSerializer(serializers.Serializer):
    
    id_user = serializers.IntegerField()
    username = serializers.CharField(max_length=50)
    full_name = serializers.CharField(max_length=100)
    master_pwd = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        
        return User.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        
        instance.id_user = validated_data.get('id_user', instance.id_user)
        instance.username = validated_data.get('username', instance.username)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.master_pwd = validated_data.get('master_pwd', instance.master_pwd)