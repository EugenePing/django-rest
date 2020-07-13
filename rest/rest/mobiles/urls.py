from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('mobile/create/', MobileCreateView.as_view()),
    path('list/', MobileViewList.as_view()),
    path('mobile/detail/<int:pk>/', MobileDetailView.as_view()),
]
