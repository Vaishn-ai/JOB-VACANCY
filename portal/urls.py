from .views import create_job, show_job, update_job, delete_job, info_job, home, About, Contact
from django.urls import path

urlpatterns = [
    path('', home, name='home_url'),
    path('about/', About, name='about_url'),
    path('contact/', Contact, name='contact_url'),
    path('create/', create_job, name='create_url'),
    path('jobs/', show_job, name='show_url'),
    path('update/<int:pk>/', update_job, name='update_url'),
    path('delete/<int:pk>/', delete_job, name='delete_url'),
    path('info/<int:pk>/', info_job, name='info_url'),
]