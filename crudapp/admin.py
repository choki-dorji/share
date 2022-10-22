from django.contrib import admin
from .models import MaleUserData, Marriage, FemaleUserData, ChildData, Tender, Vacancy

# Register your models here.
admin.site.register(MaleUserData)
admin.site.register(FemaleUserData)
admin.site.register(Marriage)
admin.site.register(ChildData)
admin.site.register(Tender)
admin.site.register(Vacancy)
# @admin.register(MaleUserData, FemaleUserData)
# @admin.register(Tender, Marriage, ChildData)
# class MaleUserDataAdmin(admin.ModelAdmin):
#     list_display = ['CID','Name', 'status']
#     list_filter = ['CID']
#     search_fields = ['CID']

