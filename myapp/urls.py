from django.urls import path
from myapp import views
from . views import productView

urlpatterns = [
    path('', views.indexView, name='index_home'),
   # path('contact/', views.contactView, name='contact'),
   path('path/', views.productView, name='product')
   
    
]