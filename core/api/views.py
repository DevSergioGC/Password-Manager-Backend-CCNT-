from django.shortcuts import render, HttpResponse
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def folder_list(request):
    
    #! Get all folders
    
    if request.method == 'GET':
        
        folders = Folders.objects.all()
        serializer = FolderSerializer(folders, many=True)
        
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serializer = FolderSerializer(data=data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def folder_details(request, id_folders):
    
    try:
        
        folder = Folders.objects.get(id_folders=id_folders)
        
    except Folders.DoesNotExist:
        
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        
        serializer = FolderSerializer(folder)
        
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        
        data = JSONParser().parse(request)
        serializer = FolderSerializer(folder, data=data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        
        folder.delete()
        
        return HttpResponse(status=204)
    
@csrf_exempt
def item_list(request):
    
    #! Get all items
    
    if request.method == 'GET':
        
        items = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def item_details(request, id_item):
    
    try:
        
        item = Items.objects.get(id_item=id_item)
        
    except Items.DoesNotExist:
        
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        
        serializer = ItemSerializer(item)
        
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        
        item.delete()
        
        return HttpResponse(status=204)

@csrf_exempt
def user_list(request):
    
    # ! Get all users
    
    if request.method == 'GET':
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def user_details(request, id_user):
    
    try:
        
        users = Folders.objects.get(id_user=id_user)
        
    except User.DoesNotExist:
        
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        
        serializer = UserSerializer(users)
        
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        
        data = JSONParser().parse(request)
        serializer = UserSerializer(users, data=data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        
        users.delete()
        
        return HttpResponse(status=204)

