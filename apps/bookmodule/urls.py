from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= "books.index"),
    path('index2/<str:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links, name="books.links"),
    path('html5/text/formatting', views.formatting, name="books.formatting"),
    path('html5/listing', views.listing, name="books.listing"),
    path('html5/tables', views.tables, name="books.tables"),
    path('search/', views.search, name="books.search"),
    path('simple/query', views.simple_query, name="books.simple_query"),
    path('complex/query', views.complex_query, name="books.complex_query"),
    path('lab8/task1/', views.task1, name='books.task1'),
    path('lab8/task2/', views.task2, name='books.task2'),
    path('lab8/task3/', views.task3, name='books.task3'),
    path('lab8/task4/', views.task4, name='books.task4'),
    path('lab8/task5/', views.task5, name='books.task5'),
    path('lab8/task7/', views.task7, name='books.task7'),
    path('lab9/task1/', views.task9_1, name='books.task9_1'),
    path('lab9/task2/', views.task9_2, name='books.task9_2'),
    path('lab9/task3/', views.task9_3, name='books.task9_3'),
    path('lab9/task4/', views.task9_4, name='books.task9_4'),
    path('lab10/lab9_BookList/', views.task9_1_1, name='books.BookList'),
    path('lab10/lab9_add_book/', views.task9_1_2, name='books.add_book'),
    path('lab10/lab9_edit_book/<int:bookId>', views.task9_1_3, name='books.edit_book'),
    path('lab10/lab9_delete_book/<int:bookId>', views.task9_1_4, name='books.delete_book'),

    path('lab10/lab9p2_BookList/', views.task9_2_1, name='books.BookList2'),
    path('lab10/lab9p2_add_book/', views.task9_2_2, name='books.add_book2'),
    path('lab10/lab9p2_edit_book/<int:bookId>', views.task9_2_3, name='books.edit_book2'),
    path('lab10/lab9p2_delete_book/<int:bookId>', views.task9_2_4, name='books.delete_book2'),


]
 
