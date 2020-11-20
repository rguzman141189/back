from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET(-1))
    address = models.CharField(max_length = 255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.user

class ProfileTwo(models.Model):
    profileModel = models.ForeignKey(ProfileModel, on_delete = models.SET(-1))
    address = models.CharField(max_length = 255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.profileModel

class Ejemplo2(models.Model):
    ejemplo_campo = models.CharField(max_length = 255, null=False)
    ejemplo_campo2 = models.CharField(max_length = 255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.ejemplo_campo

