from django.urls import path
import blog.views as views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
]
