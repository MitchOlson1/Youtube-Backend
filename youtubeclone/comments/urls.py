from django.urls import path
from . import views

urlpatterns = [
    path('youtube_clone_backend/', views.CommentsList.as_view()),
    # path('', views.something.as_view()),

]

# figure out what to change in URLS and add part = snippet to key/value
