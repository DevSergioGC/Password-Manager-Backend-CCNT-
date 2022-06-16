from django.urls import path, include
from .views import *

urlpatterns = [     
    path('api/folder/', FolderList.as_view()),
    path('api/folder/<int:pk>/', FolderDetail.as_view()),
    path('api/item/', ItemList.as_view()),
    path('api/item/<int:pk>/', ItemDetail.as_view()),
    path('api/user/', UserList.as_view()),       
]