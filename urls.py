"""univentos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import produtor.views as produtor_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Produtor
    path('', produtor_views.home, name='home'),
    path('login/', produtor_views.login, name='login'),
    path('login/post', produtor_views.loginPost, name='loginPost'),
    path('register/', produtor_views.register, name='register'),
    path('register/post', produtor_views.registerPost, name='registerPost'),


    # Evento cadastro
    path('evento/cadatro', produtor_views.eventos_cadastrar,
         name='evento_cadastrar'),
    path('evento/editar', produtor_views.eventos_editar,
         name='evento_editar'),
    path('evento/cadatro/post', produtor_views.evento_cadastrar_post,
         name='evento_cadastrar_post'),
    path('evento/read/1', produtor_views.evento_read,
         name='evento_read'),
    path('eventos/', produtor_views.eventos_list, name='eventos'),
    path('evento/delete/',
         produtor_views.evento_delete, name="delete")

]
