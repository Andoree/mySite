from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_page, name='application'),
    url(r'^page1/', views.post_page1, name='page1'),
    url(r'^page2/', views.post_page2, name='page2'),
    url(r'^page3/', views.post_page3, name='page3')
]