from django.contrib import admin
from .models import MaleUserData, Marriage, FemaleUserData, ChildData, Tender, Vacancy
from django.core.mail import EmailMessage
from django.conf import settings
from .serializers import *
import email, smtplib, ssl
from .provider import PROVIDERS
from twilio.rest import Client

# from django.contrib import admin
# from .models import Article

# Register your models here.
# admin.site.register(MaleUserData)
# admin.site.register(FemaleUserData)
# admin.site.register(Marriage)
# admin.site.register(ChildData)
# admin.site.register(Tender)
# admin.site.register(Vacancy)
@admin.register(MaleUserData, FemaleUserData)
# @admin.register(Tender, Marriage, ChildData)



# class MaleUserDataAdmin(admin.ModelAdmin):
#     list_display = ['CID','Name', 'status']
#     # list_filter = ['CID']
#     search_fields = ['CID']
#     # actions = ['make_published']



class MaleUserDataAdmin(admin.ModelAdmin):
    list_display = ['CID','Name', 'email', 'status']
    # list_filter = ['CID']
    search_fields = ['CID']
    actions = ['make_published']
    
    

    

    def make_published(self, request, queryset):
        model = FemaleUserData
        queryset.update(status=True)
        # email = EmailMessage(
        #     "Gewog Management System",
        #     "Hello " + "Dechen " + "You have successfully added your data.",
        #     settings.EMAIL_HOST_USER,
        #     # [MaleUserData.email],
        #     ['ceedeejee9@gmail.com']
        #     )
        # email.fail_silently = False
        # email.send()

        print("model "+ str(model.contact_number))

        account_sid = 'ACf70ad91e8f4df46cf76d6a474df9b45a'
        auth_token = 'a41f8a27a9cdd87669caf8b0c9017e2b'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body='Dear Customer have succesfully added your data to Gewog management system',
        from_='[+18582408109]',
        to=[model.data['contact_number']]
        )
        print(message.sid)
        
        
        


        
    

       

        
    make_published.short_description = "Confirm the selected user"


