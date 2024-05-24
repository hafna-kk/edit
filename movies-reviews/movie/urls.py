from django.urls import path

from . import views
app_name = 'movie'

urlpatterns = [
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('create_review/<int:movie_id>/', views.create_review, name='create_review'),
    path('<int:movie_id>/update', views.update_review, name='update_review'),
    path('<int:movie_id>/delete', views.delete_review, name='delete_review'),
    path('add/', views.add_movie, name='add_movie'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),

]
