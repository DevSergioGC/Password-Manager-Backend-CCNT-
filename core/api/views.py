from warnings import catch_warnings
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import Token
import cryptocode
from django.http import Http404
from rest_framework.response import Response

class FolderList(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    
    def get(self, request, format=None):        
        
        folder = Folders.objects.filter(user=self.request.user.id)
        serializer = FolderSerializer(folder, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, format=None):
        
        data = request.data        
        serializer = FolderSerializer(data=data, many=True)
        
        if serializer.is_valid():
            
            folder = Folders.objects.create(name=data['name'], user=self.request.user)
            folder.save()   
            
            serializer_class = FolderSerializer(folder)  
            
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FolderDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    
    def get_object(self, pk):
        
        try:
            
            return Folders.objects.get(pk=pk)
        
        except Folders.DoesNotExist:
            
            raise Http404

    def get(self, request, pk, format=None):
        
        folder = self.get_object(pk)
        serializer = FolderSerializer(folder)
        
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        
        folder = self.get_object(pk)
        serializer = FolderSerializer(folder, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        
        folder = self.get_object(pk)
        folder.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemList(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    
    def get(self, request, format=None):        
        
        item = (Items.objects.filter(user=self.request.user.id, folder=self.request.query_params.get('folder'))).values()
        
        new_query_set = [i for i in item]             
            
        for i in range(len(new_query_set)):      
                
            new_query_set[i]["password"] = cryptocode.decrypt(new_query_set[i]["password"], "new_key")         
        
        return Response(item)
    
    def post(self, request, format=None):
        
        try:
            
            data = request.data   
            folder = Folders.objects.filter(pk=data['folder']).first() 
            
            item = Items.objects.create(name=data['name'], password=cryptocode.encrypt(data['password'], "new_key"), 
                                            description=data['description'], url=data['url'], folder=folder, user=self.request.user)
            item.save()   
                
            serializer_class = ItemSerializer(item)  
                
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        
        except:
            
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)        

class ItemDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)   

    def get(self, request, pk, format=None):
        
        try:
            
            item = Items.objects.filter(pk=pk).values()
            new_item = [i for i in item]        
            new_item[0]['password'] = cryptocode.decrypt(new_item[0]["password"], "new_key")           
            
            return Response(new_item)
        
        except Items.DoesNotExist:
            
            raise Http404

    def put(self, request, pk, format=None):
        
        item = Items.objects.get(pk=pk)        
        
        serializer = ItemSerializer(item, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            Items.objects.filter(pk=pk).update(password=cryptocode.encrypt(serializer.data['password'], "new_key"))            
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)             

    def delete(self, request, pk, format=None):
        
        Items.objects.filter(pk=pk).first().delete()        
        
        return Response(status=status.HTTP_204_NO_CONTENT)

"""class ItemViewSet(APIView):
    
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Items.objects.all()
    
    def get(self, request, format=None):           
            
        queryset = self.queryset               
        query_set = (queryset.filter(user=self.request.user, folder=self.request.query_params.get('folder'))).values()   
        new_query_set = [i for i in query_set]             
            
        for i in range(len(new_query_set)):      
                
            new_query_set[i]["password"] = cryptocode.decrypt(new_query_set[i]["password"], "new_key")  
            
            print(f'\n\n{new_query_set[i]["password"]}\n\n')  
        
        return new_query_set     
    
    def post(self, request, format=None):
        
        item_data = request.data                 
        
        pwd = item_data['password']        
        new_pwd = cryptocode.encrypt(pwd, "new_key")
        
        folder = Folders.objects.filter(id_folders=item_data['folder']).first()               
        
        new_item=  Items.objects.create(name=item_data['name'], password=new_pwd, description=item_data['description'],
                                       url=item_data['url'], folder=folder, user=self.request.user)
        
        new_item.save()        
        serializer_class = ItemSerializer(new_item)
        
        return Response(serializer_class.data)"""
      
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    
    def create(self, request, *args, **kwargs):
        
        #? Create new user
        user_data = request.data
        new_user = User.objects.create(username=user_data['username'], first_name=user_data['first_name'])
        new_user.set_password(user_data['password'])
        new_user.save()
        
        #? Create 'default' folder related to created user
        new_folder = Folders.objects.create(name='Default', user=new_user)                
        new_folder.save()
        
        #? User & Folder Serializer
        serializer_class = FolderSerializer(new_folder)
        serializer_class2 = UserSerializer(new_user)
        
        #? Create a user's Token
        Token.objects.create(user=new_user)
        
        return Response(serializer_class2.data)