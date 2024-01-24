from rest_framework import generics, viewsets
from rest_framework.response import Response

from library.models import Author, Book, PaperSource
from library.serializers import AuthorSerializer, BookSerializer, PaperSourceSerializer


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


class BookDelievery(generics.CreateAPIView):
    serializer_class = None
    queryset = None

    def post(self, request):
        return Response(request.data, status=201)
