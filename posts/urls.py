from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="home"),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blog-titles/', views.blog_titles, name='blog_titles'),
    path('blog-description/<int:pk>/', views.blog_description, name='blog_description'),
    path('delete-blog/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('edit/<int:id>/', views.blog_update_view,name="edit"),

]

