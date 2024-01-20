from django.urls import path
from .views import fizz_buzz, get_statistics, index

urlpatterns = [
    path('fizzbuzz/', fizz_buzz, name='fizz_buzz'),
    path('statistics/', get_statistics, name='get_statistics'),
    path('', index, name='index'),  
]
