from django.contrib import admin
from django.urls import path
from VK import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('registration/', views.registration, name='registration'),
]
