# myapp/urls.py
from django.urls import path
from .views import index, delete_student,update_student,add_student

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:roll>/', delete_student, name='delete_student'),
        path('update/<int:roll>/', update_student, name='update_student'),
    path('add/', add_student, name='add_student'),

]
