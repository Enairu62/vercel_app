from django.urls import path
from pommy.views import index

urlpatterns = [
        path('', index),
    ]
