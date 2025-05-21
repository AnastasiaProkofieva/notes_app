from django.urls import path
from .views import hello_world, test_data, note_list

urlpatterns = [
    path('hello/', hello_world),
    path('notes_old/', test_data),
    path('notes/', note_list),

]