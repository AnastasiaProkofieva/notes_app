from django.shortcuts import render
from django.http import HttpResponse

from notes.models import Note


# Create your views here.
def hello_world(request):
     return HttpResponse('Hello from Notes app.')

def test_data(request):
    context = {
        'title': 'Notes',
        'items': ['Make python hometasks', 'Cook dinner', 'Feed stray cats']
    }
    return render(request, 'my_notes_old.html', context)
def note_list(request):
    notes = Note.objects.all().select_related("category")
    return render(request, 'my_notes.html', {'notes': notes})

