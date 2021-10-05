from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view()),
    path('login', views.LoginInterfaceView.as_view(),name='login'),
    path('logout', views.LogoutInterfaceView.as_view()),
    path('signup', views.SignupView.as_view(),name='signup'),
]
