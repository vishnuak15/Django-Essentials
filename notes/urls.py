from django.urls import path, include

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>',views.NotesDetailView.as_view(), name="notes.detial"),
]