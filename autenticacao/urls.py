from django.urls import path 
from . import views


urlpatterns = [
    path('login', views.login_usuario, name='login'),
    path('cadastro-usuario', views.cadastro, name='cadastro-usuario'),
    path('logout', views.logout_usuario, name='logout'),

]