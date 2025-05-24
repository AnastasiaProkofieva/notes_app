from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.views import View
from django.utils.timezone import now
from .forms import NoteForm
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

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('my_notes')


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'
    context_object_name = 'note'


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'

    def get_success_url(self):
        return reverse_lazy('note_detail', kwargs={'pk': self.object.pk})


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('my_notes')
    template_name = 'note_confirm_delete.html'

class NoteListView(ListView):
    model = Note
    template_name = 'my_notes.html'
    context_object_name = 'notes'


    def get_queryset(self):
        queryset = Note.objects.all().select_related("category")
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset