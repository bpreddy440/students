from django.urls import path
from . import views

app_name='student'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create-student'),
    path('details/<int:id>/', views.details, name='student-detail'),

]