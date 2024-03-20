from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('contact/',views.contact,name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('blog/',views.blog,name='blog'),
   

]