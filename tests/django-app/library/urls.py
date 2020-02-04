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
    path(r"sns.amazonaws.com", views.BookDelievery.as_view()),
    path(r"aws.codecommit", views.BookDelievery.as_view()),
    path(r"aws.dynamodb", views.BookDelievery.as_view()),
    path(r"aws.ec2", views.BookDelievery.as_view()),
    path(r"aws.kinesis", views.BookDelievery.as_view()),
    path(r"aws.sqs", views.BookDelievery.as_view()),
    path(r"aws.sns", views.BookDelievery.as_view()),
    path(r"aws.ses", views.BookDelievery.as_view()),
    path(r"aws.lex", views.BookDelievery.as_view()),
    path(r"aws.kinesis.firehose", views.BookDelievery.as_view()),
    path(r"myChargedEvent", views.BookDelievery.as_view()),
    path(r"aws.cognito", views.BookDelievery.as_view()),
    path(r"aws.config", views.BookDelievery.as_view()),
    path(r"aws.cloudfront", views.BookDelievery.as_view()),
    path(r"aws.cloudformation", views.BookDelievery.as_view()),
    path(r"aws.alexa", views.BookDelievery.as_view()),
    path(r"my/context", views.BookDelievery.as_view()),
]
