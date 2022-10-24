from email.policy import default
from enum import unique
from random import choices
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class MaleUserData(models.Model):
    g = [
        ('Male', 'Male'),
        ('Female', 'Female')
        ]
    CID = models.IntegerField(unique=True)
    Name = models.CharField(max_length=150)
    DOB = models.DateField()
    Gender = models.CharField(max_length=20,choices= g)
    profile = models.ImageField(upload_to='image', null= True, default=None, blank=True)
    # Gender = models.CharField(max_length=20, default='Male')
    Village = models.CharField(max_length=100)
    Chiwog = models.CharField(max_length=100)
    ThramNo = models.CharField(max_length=100)
    HouseHoldNo = models.CharField(max_length=100)  
    Created = models.DateTimeField(auto_now_add=True)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

class FemaleUserData(models.Model):
    g = [
        ('Male', 'Male'),
        ('Female', 'Female')
        ]

    CID = models.IntegerField(unique=True)
    Name = models.CharField(max_length=150)
    profile = models.ImageField(upload_to='image', null= True)
    DOB = models.DateField()
    Gender = models.CharField(max_length=20,choices=g)
    # Gender = models.CharField(max_length=20, default='Female')
    Village = models.CharField(max_length=100)
    Chiwog = models.CharField(max_length=100)
    ThramNo = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    HouseHoldNo = models.CharField(max_length=100)  
    Created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.Name
    
  
class Marriage(models.Model):
    MarriageID = models.CharField(max_length=100)
    # YOUR_CId = models.OneToOneField(UserData, related_name="Your_CID", on_delete=models.CASCADE)
    # Spouce_ID = models.OneToOneField(UserData, related_name="Spouce", on_delete=models.CASCADE)
    YOUR_CId = models.ForeignKey(MaleUserData, related_name="Your_CID", on_delete=models.CASCADE, unique=True)
    Spouce_ID = models.ForeignKey(FemaleUserData, related_name="Spouce", on_delete=models.CASCADE,unique=True)
    # Marriage_certificate = models.ImageField(upload_to='image')
    # Marriage_certificate1 = models.ImageField(upload_to='image')
    Marriage_certificate = models.ImageField(upload_to='image', null = True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.YOUR_CId.Name + " & " + self.Spouce_ID.Name
        # return self.Name


class ChildData(models.Model):
    Child_name = models.CharField(max_length=255)
    DOB_child = models.DateField()
    Marriage_ID = models.ForeignKey(Marriage, related_name="parents_Marriage_ID", on_delete=models.CASCADE)

    def __str__(self):
        return self.Child_name

class Tender(models.Model):
    Tender_name = models.CharField(max_length=255)
    Tender_Image = models.ImageField(upload_to='tender/')
    Tender_description = models.CharField(max_length=255)
    contact = models.IntegerField(max_length=255)

    def __str__(self):
        return self.Tender_name

class Vacancy(models.Model):
    vacancy_name = models.CharField(max_length=255)
    vacancy_Image = models.ImageField(upload_to='tender/')
    vacancy_description = models.CharField(max_length=255)
    contact = models.IntegerField(max_length=255)

    def __str__(self):
        return self.vacancy_name
