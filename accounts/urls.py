from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import MyAuthenticationForm

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=MyAuthenticationForm)),
    path('', include('django.contrib.auth.urls')),
]
