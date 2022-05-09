from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('folder', FolderViewSet, basename='folder')
router.register('item', ItemViewSet, basename='item')
router.register('user', UserViewSet)

urlpatterns = [    
    path('api/', include(router.urls)),
]