from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import Token
import cryptocode
from rest_framework.response import Response

class FolderViewSet(viewsets.ModelViewSet):
    
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Folders.objects.all()
    
    def get_queryset(self):
        
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        
        return query_set   
    
    def create(self, request, *args, **kwargs):
        
        folder = request.data
        
        new_folder = Folders.objects.create(name=folder['name'], user=self.request.user)
        new_folder.save()
        
        serializer_class = FolderSerializer(new_folder)
        
        return Response(serializer_class.data)
    
    def put(self, request, id, *args, **kwargs):
        
        folder = request.data
        
        new_folder = Folders.objects.filter(id_folders=id).first()
        new_folder.update(name=folder.name, user=self.request.user)
        new_folder.save()
        
        serializer_class = FolderSerializer(new_folder)
        
        return Response(serializer_class.data)
    
    def destroy(self, request, *args, **kwargs):
        
        user = self.request.user
        default_folder = Folders.objects.filter(user=user, name="Default").first()
        folder = self.get_object()
        items = Items.objects.filter(folder=folder.id_folders)
        items.update(folder=default_folder)
        folder.delete()
        
        serializer_class = FolderSerializer(folder)
        
        return Response(serializer_class.data)
    
class ItemViewSet(viewsets.ViewSet):
    
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    queryset = Items.objects.all()
    
    def get_queryset(self):           
            
        queryset = self.queryset               
        query_set = (queryset.filter(user=self.request.user, folder=self.request.query_params.get('folder'))).values()   
        new_query_set = [i for i in query_set]             
            
        for i in range(len(new_query_set)):      
                
            new_query_set[i]["password"] = cryptocode.decrypt(new_query_set[i]["password"], "new_key")        
        
        return new_query_set     
    
    def create(self, request, *args, **kwargs):
        
        item_data = request.data                 
        
        pwd = item_data['password']        
        new_pwd = cryptocode.encrypt(pwd, "new_key")
        
        folder = Folders.objects.filter(id_folders=item_data['folder']).first()               
        
        new_item=  Items.objects.create(name=item_data['name'], password=new_pwd, description=item_data['description'],
                                       url=item_data['url'], folder=folder, user=self.request.user)
        
        new_item.save()        
        #serializer_class = ItemSerializer(new_item)
        
        return Response("Success!")   
    
    def destroy(self, request, *args, **kwargs):
        
        item = self.get_object()
        item_delete = Items.objects.filter(id_item = item["id_item"])
        print(f'\n\n{item["id_item"]}\n\n')
        item_delete.delete()
        
        #serializer_class = ItemSerializer(item_delete)
        
        return Response("Success")
    
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