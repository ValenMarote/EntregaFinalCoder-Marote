from django import views
from django.urls import path
from Blog import views

urlpatterns = [

 path('', views.home, name='inicio'),
 path('about/', views.about, name= 'about'),
 path('general/', views.general, name= 'general'),
 path('programacion/', views.programacion, name= 'programacion'),
 path('libros/', views.libros, name= 'libros'),
 path('juegos/', views.juegos, name= 'juegos'),
 path('<slug:slug>/', views.detallePost, name='detallepost')
    

 ]
