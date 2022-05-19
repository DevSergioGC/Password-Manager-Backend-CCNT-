from django.db import models
class User(models.Model):
    
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, blank=False)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    master_pwd = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        
        return self.username
class Folders(models.Model):
    
    id_folders = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)   
    
    def __str__(self):
        
        return self.name
class Items(models.Model):
    
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=300)
    url = models.CharField(max_length=255)
    
    id_folders = models.ForeignKey(Folders, null=False, blank=False, on_delete=models.DO_NOTHING)
    id_user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.name