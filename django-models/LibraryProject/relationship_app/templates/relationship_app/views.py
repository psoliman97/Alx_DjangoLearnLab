from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # This makes views.register accessible

urlpatterns = [
    path('register/', views.register_view, name='register'),  # This is views.register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', views.home_view, name='home'),  # Optional home view
]
