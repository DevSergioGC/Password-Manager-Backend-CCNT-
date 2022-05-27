from django.db import models
from django.contrib.auth.models import User

class Folders(models.Model):
    
    id_folders = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)  
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.name
    
class Items(models.Model):
    
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=300)
    url = models.CharField(max_length=255)
    
    folder = models.ForeignKey(Folders, null=True, blank=True, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.name