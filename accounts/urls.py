from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
