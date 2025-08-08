from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # This makes views.register available

urlpatterns = [
    path('register/', views.register, name='register'),  # ✅ match "views.register"
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅ match "LoginView.as_view(template_name="
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # ✅ match "LogoutView.as_view(template_name="
    path('', views.home_view, name='home'),  # Optional home
]
