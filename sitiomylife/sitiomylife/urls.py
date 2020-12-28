"""sitiomylife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import  include, url
from django.conf.urls.static import static 
from django.conf import settings
from mylife import views
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mylife/', include('mylife.urls')),
    #path('', views.welcome),
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('quienessomos', views.quienessomos),
    path('contacto', views.contacto),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #path('drafts/', views.post_draft_list, name='post_draft_list'),
    #path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    #path('post/<int:slug>/comment/', views.add_comment, name='add_comment'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    #path('post/new', views.nuevo_post, name='nuevo_post'),
    #path('comentario', views.post_detail),
     
   
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)