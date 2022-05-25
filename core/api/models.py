from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=150)
    master_pwd = models.CharField(min_length=8, null=False, blank=False)

class Folders(models.Model):
    
    id_folders = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)  
    id_user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.name
    
class Items(models.Model):
    
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=300)
    url = models.CharField(max_length=255)
    
    id_folders = models.ForeignKey(Folders, null=True, blank=True, on_delete=models.DO_NOTHING)
    id_user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.name