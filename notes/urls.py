from django.urls import path
from .views import hello_world, test_data, note_list, NoteListView, NoteCreateView, NoteDetailView, NoteUpdateView, \
    NoteDeleteView

urlpatterns = [
    path('hello/', hello_world),
    path('notes_old/', test_data),
    path('notes/', note_list),
    path('', NoteListView.as_view(), name='my_notes'),
    path('create/', NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),

]