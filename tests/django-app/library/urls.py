from django.urls import include
from django.urls import path
from library import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"authors", views.AuthorViewSet, basename="author")
router.register(r"books", views.BookViewSet, basename="book")
router.register(r"paper-sources", views.PaperSourceViewSet, basename="paper-source")

urlpatterns = [
    path("", include(router.urls)),
    path(r"book/delievery/", views.BookDelievery.as_view()),
    path(r"aws.s3", views.BookDelievery.as_view()),
    path(r"aws.events", views.BookDelievery.as_view()),
    path(r"my/context", views.BookDelievery.as_view()),
]
