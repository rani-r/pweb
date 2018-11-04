#Linking to locallibrary/urls.py file

#This is where we'll add our patterns as we build the application

from django.conf.urls import url
from . import views

#^ is a string start marker and $ is an end of string marker
urlpatterns = [
    url(r'^$', views.index, name='index'),       #Will call views.index is pattern is detected
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name="author-detail"),
]