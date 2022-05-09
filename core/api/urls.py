from django.urls import path
from .views import *

urlpatterns = [
    path('folder/', folder_list),
    path('folder/<int:id_folders>/', folder_details),
    path('item/', item_list),
    path('item/<int:id_item>/', item_details),
    path('user/', user_list),
    path('user/<int:id_user>/', user_details),
]