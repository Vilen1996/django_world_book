from django.urls import path, include
from . import views
from django.urls import re_path


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path('^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('create/', views.create, name='create'),
    path('edit1/<int:id>', views.edit1, name='edit1'),
    path('delete/<int:id>/', views.delete, name='delete'),
    re_path(r'^book/create/$', views.BookCreate.as_view(), name = 'book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name = 'book_update'),
    re_path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name = 'book_delete'),
]
