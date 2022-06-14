from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

"""router = DefaultRouter()
router.register('folder', FolderViewSet, basename='folder')
router.register('item', ItemViewSet, basename='item')
router.register('user', UserViewSet, basename='user')"""

urlpatterns = [    
    #path('api/'),
    path('folder/', FolderList.as_view()),
    path('folder/<int:pk>/', FolderDetail.as_view()),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
]