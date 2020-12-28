from django.urls import path
from . import views

app_name = 'telefoni'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:id>/', views.article, name='article'),
    path('article/edit/<int:id>/', views.edit, name='edit'),
    path('article/delete/<int:id>/', views.delete, name='delete'),
    path('article/new/', views.new, name='new'),
    path('article/newcomment/<int:id>/', views.newcomment, name='newcomment'),
    path('article/allcomments/<int:id>/', views.allcomments, name='allcomments'),
    path('article/signup/', views.signup, name='signup'),
]
