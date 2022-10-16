from django.contrib import admin
from .models import MaleUserData, Marriage, FemaleUserData, ChildData, Tender, Vacancy

# Register your models here.
admin.site.register(MaleUserData)
admin.site.register(FemaleUserData)
admin.site.register(Marriage)
admin.site.register(ChildData)
admin.site.register(Tender)
admin.site.register(Vacancy)