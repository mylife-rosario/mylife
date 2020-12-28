from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^post/<int:pk>/', views.post_detail, name='post_detail'),
    path(r'post/<int:pk>/', views.post_detail, name='post_detail'),
    #url(r'^comenta/$',views.nuevo_comentario,  name='nuevo_comentario'),
    #url(r'^$', views.index, name='media'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detalle'),
] 