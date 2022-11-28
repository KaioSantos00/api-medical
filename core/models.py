from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Recommendation(models.Model):
    name = models.CharField(max_length=255, null=False)
    avatar = models.ImageField(upload_to='medical/avatars/%Y/%m/%d/')
    phone = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    #procedure = models.ManyToManyField(Procedure)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.name)


class Procedure(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    days_limit = models.IntegerField(null=False)
    recommendation = models.ManyToManyField(Recommendation)
    #user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title)


class Users(AbstractUser):
    cpf = models.CharField('CPF', max_length=50, null=True)
    avatar = models.ImageField(
        upload_to='medical/avatars/%Y/%m/%d/')
    birth_date = models.DateField(null=True)
    street = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=100, null=True)
    uf = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    # -email = models.CharField(max_length=100, null=True)
    procedure = models.ManyToManyField(
        Procedure)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.username)
