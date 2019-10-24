import json
from datetime import datetime

from django.test import TestCase
from library.models import Author
from library.models import Book


class TestBook(TestCase):
    def test_get_something_that_does_not_exist(self):
        response = self.client.get("/exists")
        self.assertEqual(404, response.status_code)

    def test_get_books(self):
        response = self.client.get("/books/")
        self.assertEqual(200, response.status_code)
        self.assertEqual([], json.loads(response.content))

    def test_get_a_book(self):
        book = Book.objects.create(name="Title", published=datetime.utcnow())
        expected = {"id": book.pk, "name": "Title", "published": book.published.date().isoformat(), "author": None}
        response = self.client.get(f"/books/{book.id}/")
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, json.loads(response.content))

    def test_create_a_book(self):
        book = {"name": "Moon landing", "published": "1969-07-20"}
        response = self.client.post("/books/", data=book)
        self.assertEqual(201, response.status_code)
        expected = {"author": None, "id": 1, "name": "Moon landing", "published": "1969-07-20"}
        self.assertEqual(expected, json.loads(response.content))

    def test_update_a_book(self):
        book = Book.objects.create(name="Title", published=datetime.utcnow())
        first_response = self.client.get(f"/books/{book.id}/")
        self.assertEqual(200, first_response.status_code)
        self.assertEqual(json.loads(first_response.content)["name"], "Title")
        response = self.client.patch(f"/books/{book.id}/", data={"name": "Something"}, content_type="application/json")
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content)["name"], "Something")

    def test_delete_a_book(self):
        book = Book.objects.create(name="Title", published=datetime.utcnow())
        response = self.client.delete(f"/books/{book.id}/")
        self.assertEqual(204, response.status_code)
        self.assertEqual(b"", response.content)


class TestAuthor(TestCase):
    def test_get_authors(self):
        response = self.client.get("/authors/")
        self.assertEqual(200, response.status_code)
        self.assertEqual([], json.loads(response.content))

    def test_get_a_author(self):
        author = Author.objects.create(first_name="First", last_name="Last")
        expected = {"id": author.pk, "first_name": "First", "last_name": "Last"}
        response = self.client.get(f"/authors/{author.id}/")
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, json.loads(response.content))

    def test_create_a_author(self):
        author = {"first_name": "First", "last_name": "Last"}
        response = self.client.post("/authors/", data=author)
        self.assertEqual(201, response.status_code)
        expected = {"id": 1, "first_name": "First", "last_name": "Last"}
        self.assertEqual(expected, json.loads(response.content))

    def test_update_a_author(self):
        author = Author.objects.create(first_name="First", last_name="Last")
        first_response = self.client.get(f"/authors/{author.id}/")
        self.assertEqual(200, first_response.status_code)
        self.assertEqual(json.loads(first_response.content)["first_name"], "First")
        response = self.client.patch(
            f"/authors/{author.id}/", data={"first_name": "Buzz"}, content_type="application/json"
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content)["first_name"], "Buzz")

    def test_delete_a_author(self):
        author = Author.objects.create(first_name="First", last_name="Last")
        response = self.client.delete(f"/authors/{author.id}/")
        self.assertEqual(204, response.status_code)
        self.assertEqual(b"", response.content)


class TestBookDelievery(TestCase):
    def test_book_delievery(self):
        response = self.client.post("/book/delievery/", data={"blah": 1234})
        self.assertEqual(201, response.status_code)
        self.assertEqual({"blah": "1234"}, json.loads(response.content))
