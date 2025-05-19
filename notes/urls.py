from django.urls import path
from .views import hello_world, test_data

urlpatterns = [
    path('hello/', hello_world),
    path('notes/', test_data),

]