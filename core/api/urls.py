from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = [    
    path('api/', include(router.urls)),
    path('api/folder/', FolderList.as_view()),
    path('api/folder/<int:pk>/', FolderDetail.as_view()),
    path('api/item/', ItemList.as_view()),
    path('api/item/<int:pk>/', ItemDetail.as_view()),
]