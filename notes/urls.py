from django.urls import path, include

from . import views

urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>',views.detail),
]