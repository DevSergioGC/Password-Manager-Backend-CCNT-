from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def folder_list(request):
    
    #! Get all folders
    
    if request.method == 'GET':
        
        folders = Folders.objects.all()
        serializer = FolderSerializer(folders, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':        
        
        serializer = FolderSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def folder_details(request, id_folders):
    
    try:
        
        folder = Folders.objects.get(id_folders=id_folders)
        
    except Folders.DoesNotExist:
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = FolderSerializer(folder)
        
        return Response(serializer.data)
    
    elif request.method == 'PUT':
                
        serializer = FolderSerializer(folder, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        folder.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def item_list(request):
    
    #! Get all items
    
    if request.method == 'GET':
        
        items = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':        
        
        serializer = ItemSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def item_details(request, id_item):
    
    try:
        
        item = Items.objects.get(id_item=id_item)
        
    except Items.DoesNotExist:
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = ItemSerializer(item)
        
        return Response(serializer.data)
    
    elif request.method == 'PUT':
                
        serializer = ItemSerializer(item, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        item.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def user_list(request):
    
    # ! Get all users
    
    if request.method == 'GET':
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':        
        
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, id_user):
    
    try:
        
        users = Folders.objects.get(id_user=id_user)
        
    except User.DoesNotExist:
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = UserSerializer(users)
        
        return Response(serializer.data)
    
    elif request.method == 'PUT':
                
        serializer = UserSerializer(users, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        users.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

