from tkinter import E
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from urllib3 import HTTPResponse
from .models import ChildData, Marriage, MaleUserData, FemaleUserData, Tender, Vacancy
from .serializers import MaleUserDataSerializer, MarriageSerializer, FemaleUserDataSerializer, ChildDataSerializer, TenderSerializer, VacancySerializer
# from .permissions import IsAdminOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.conf import settings


# def success(request):
#     email = EmailMessage(
#         "head",
#         "body",
#         settings.EMAIL_HOST_USER,
#         ['12190019.gcit@rub.edu.bt'],
#     )
#     email.fail_silently = False
#     email.send()

#     return HttpResponse('okay')



# class MaleUserDataView(generics.ListCreateAPIView):
#     # queryset = UserData.objects.all()
#     queryset = MaleUserData.objects.filter(status = True)
#     serializer_class = MaleUserDataSerializer
#     # permission_classes  = [IsAdminOrReadOnly]

#     # email = EmailMessage(
#     #     "Successfully created",
#     #     "Hello samten you have successfukky created a census",
#     #     settings.EMAIL_HOST_USER,
#     #     ['12190019.gcit@rub.edu.bt'],
#     # )
#     # email.fail_silently = False
#     # email.send()
    

################################# MALE #################################################################
class MaleUserDataView(APIView):
 
    def get(self, request):
        platform = MaleUserData.objects.filter(status = True)
        serializer = MaleUserDataSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MaleUserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 

            email = EmailMessage(
            "Gewog Management System",
            "Hello " + serializer.data['Name'] + " you have successfully added Your Data in our system. Please wait for 12 hours, we have to process your details. THANK YOU",
            settings.EMAIL_HOST_USER,
            [serializer.data['email']],
            )
            email.fail_silently = False
            email.send()
    
            
            # print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FemaleUserDataView(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]

    def get(self, request):
        platform = MaleUserData.objects.filter(status = True)
        serializer = MaleUserDataSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MaleUserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 

            email = EmailMessage(
            "Gewog Management System",
            "Hello " + serializer.data['Name'] + " you have successfully added Your Data in our system. Please wait for 12 hours, we have to process your details. THANK YOU",
            settings.EMAIL_HOST_USER,
            [serializer.data['email']],
            )
            email.fail_silently = False
            email.send()
    
            
            # print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MaleProject(generics.ListAPIView):
    queryset = MaleUserData.objects.filter(status = True)
    serializer_class = MaleUserDataSerializer
    filter_backends = [filters.SearchFilter] 
    search_fields = ['CID']

# class ReviewList(generics.ListAPIView):
#     # queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     # permission_classes = [IsAuthenticated]
#     throttle_classes = [ReviewListThrottle, AnonRateThrottle]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['review_user__username', 'active']

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Review.objects.filter(watchlist=pk)


    # if UserData.status == False:
        
# class FemaleUserDataView(generics.ListCreateAPIView):
#     # queryset = UserData.objects.all()
#     queryset = FemaleUserData.objects.filter(status = True)
#     serializer_class = FemaleUserDataSerializer


# class CreatecidView(generics.ListCreateAPIView):
#     queryset = Createcid.objects.all()
#     serializer_class = CreateCIDSerializer

# class MarriageView(ModelViewSet):
#     serializer_class = MarriageSerializer
#     queryset = Marriage.objects.all()
 
class MarriageView(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    # throttle_classes = [AnonRateThrottle]

    def get(self, request):
        platform = Marriage.objects.all()
        serializer = MarriageSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MarriageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            print(serializer.data)

            email = EmailMessage(
            "Gewog Management System",
            "Hello " + serializer.data['Name'] + " You have registered your Marriage cerficate with our system, wait till we inform you about confirmation.",
            settings.EMAIL_HOST_USER,
            [serializer.data['Email']],
            )
            email.fail_silently = False
            email.send()
    
            
           
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    # def perform_create(self, serializer):
    #     serializer.save(self.request.data.get('img'))

# class PhotoViewSet(viewsets.ModelViewSet):

#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer
#     parser_classes = (MultiPartParser, FormParser)

#     def perform_create(self, serializer):
#         serializer.save(img=self.request.data.get('file'))

class ChildDataView(generics.ListCreateAPIView):
    queryset = ChildData.objects.all()
    serializer_class = ChildDataSerializer

# hK_rzw7WSKBylzADI4vBVVOd7Chlu6cduPeq3D0s twilo
    
class TenderView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer


    
class VacancyView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
       

