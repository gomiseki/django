from django.contrib import admin
from django.urls import path
from homeapp import views


urlpatterns = [
    path('home/', views.home, name ='home'),
    path('search/', views.search, name ='search'),
    path('detail/<int:id>', views.detail, name="detail"),
    path('new/<int:id>', views.new, name ='new'),
    path('create/<int:id>', views.create, name = 'create'),
    path('update/<str:title>/<int:id>', views.update, name ='update'),
    path('delete/<int:id>', views.delete, name ='delete'),
    path('db/', views.db, name="db")
]
