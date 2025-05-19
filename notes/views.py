from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
     return HttpResponse('Hello from Notes app.')

def test_data(request):
    context = {
        'title': 'Notes',
        'items': ['Make python hometasks', 'Cook dinner', 'Feed stray cats']
    }
    return render(request, 'my_notes.html', context)
