from library.models import Author
from library.models import Book
from library.models import PaperSource
from library.serializers import AuthorSerializer
from library.serializers import BookSerializer
from library.serializers import PaperSourceSerializer
from rest_framework import viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class PaperSourceViewSet(viewsets.ModelViewSet):
    serializer_class = PaperSourceSerializer

    def get_queryset(self):
        return PaperSource.objects.all()
