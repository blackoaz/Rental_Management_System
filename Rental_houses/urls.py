from django.urls import path
from Rental_houses import views

urlpatterns = [
    path('',views.index,name='home')
]