from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
from .models import Notes
from .forms import *


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_detial.html"


def detail(request,pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Notes does'nt exist")
    return render(request, 'notes/notes_detial.html',{'notes':note})