from django.urls import path

from . import views

urlpatterns = [
    path("discussion/<int:post_id>/", views.discussion, name="Discussions"),
    path("", views.forum, name="forum")
]
