from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class FolderViewSet(viewsets.ModelViewSet):
    
    queryset = Folders.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication)
    
class ItemViewSet(viewsets.ModelViewSet):
    
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication)
    
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer