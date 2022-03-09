from django.urls import path
from . import views

app_name = 'general_ledger'

urlpatterns = [
    path('', views.task_home, name='home'),
    #path('add-dept/', views.add_dept_form, name='add-dept'),
    #path('add-task/', views.add_task, name='add-task'),
    #path('task/<slug:slug>/', views.task_detail, name='task-detail'),
    #path('category/<slug:category_slug>/', views.category_list, name='category_list'),


    #path('add-task-form/', views.add_task_form, name='add-task-form'),

]
