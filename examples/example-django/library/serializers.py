from library.models import Author
from library.models import Book
from library.models import PaperSource
from rest_framework_json_api import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    included_serializers = {"author": AuthorSerializer}

    class Meta:
        model = Book
        fields = "__all__"


class PaperSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperSource
        fields = "__all__"
