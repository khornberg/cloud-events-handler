from rest_framework_json_api import serializers

from library.models import Author, Book, PaperSource


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
