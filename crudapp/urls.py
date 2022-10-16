from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChildDataView, MaleProject, MaleUserDataView, MarriageView, FemaleUserDataView, ChildDataView, MaleProject, TenderView, VacancyView #, success


# router = DefaultRouter()
# router.register("register", MarriageView)
urlpatterns = [
    path('createmale/', MaleUserDataView.as_view()),
    path('createfemale/', FemaleUserDataView.as_view()),
    path('Marriage_create/', MarriageView.as_view()),
    # path('Marriage_create/', include(router.urls)),
    # path('childregister/', ChildDataView.as_view()),
    path('childregister/', ChildDataView.as_view()),
    path('search/', MaleProject.as_view()),

    path('Tender/', TenderView.as_view()),
    path('vacancy/', VacancyView.as_view()),

    # path('email/', success)
]
