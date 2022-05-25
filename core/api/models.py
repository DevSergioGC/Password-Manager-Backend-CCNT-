from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        
        if not username:
            raise ValueError(('The given username must be set'))
        
        user = self.model(username=username, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password, True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):    
    
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    name = models.CharField(max_length=150)
    master_pwd = models.CharField(max_length=50, null=False, blank=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Folders(models.Model):
    
    id_folders = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)  
    #id_user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.name
    
class Items(models.Model):
    
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=300)
    url = models.CharField(max_length=255)
    
    id_folders = models.ForeignKey(Folders, null=True, blank=True, on_delete=models.DO_NOTHING)
    #id_user = models.ForeignKey(CustomUser, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        
        return self.name