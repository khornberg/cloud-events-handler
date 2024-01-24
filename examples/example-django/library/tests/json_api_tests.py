import json
from datetime import datetime

from django.test import TestCase
from library.models import Author
from library.models import Book
from library.models import PaperSource


class TestBook(TestCase):
    def test_get_something_that_does_not_exist(self):
        response = self.client.get("/exists")
        self.assertEqual(404, response.status_code)

    def test_get_books(self):
        response = self.client.get("/books/", HTTP_ACCEPT="application/vnd.api+json")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"data": []}, json.loads(response.content))

    def test_get_a_book(self):
        book = Book.objects.create(name="Title", published=datetime.utcnow())
        expected = {
            "data": {
                "type": "books",
                "id": "1",
                "attributes": {"name": "Title", "published": book.published.date().isoformat()},
                "relationships": {"author": {"data": None}},
            }
        }
        response = self.client.get(f"/books/{book.id}/", HTTP_ACCEPT="application/vnd.api+json")
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected, json.loads(response.content))

    def test_create_a_book(self):
        book = {"data": {"type": "books", "attributes": {"name": "Moon Landing", "published": "1968-07-20"}}}
        response = self.client.post(
            "/books/", data=book, HTTP_ACCEPT="application/vnd.api+json", content_type="application/vnd.api+json"
        )
        self.assertEqual(201, response.status_code)
        returned_content = json.loads(response.content)
        returned_content["data"].pop("id")
        book["data"]["relationships"] = {"author": {"data": None}}
        self.assertEqual(book, returned_content)

    def test_update_a_book(self):
        book = Book.objects.create(name="Title", published=datetime.utcnow())
        first_response = self.client.get(f"/books/{book.id}/", HTTP_ACCEPT="application/vnd.api+json")
        self.assertEqual(200, first_response.status_code)
        content = json.loads(first_response.content)
        self.assertEqual(content["data"]["attributes"]["name"], "Title")
        content["data"]["attributes"]["name"] = "Something"
        content["data"].pop("relationships")
        response = self.client.patch(
            f"/books/{book.id}/",
            data=content,
            content_type="application/vnd.api+json",
            HTTP_ACCEPT="application/vnd.api+json",
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content)["data"]["attributes"]["name"], "Something")

    def test_delete_a_book(self):
        book = Book.objects.create(name="Title", published=datetime.utcnow())
        response = self.client.delete(f"/books/{book.id}/", HTTP_ACCEPT="application/vnd.api+json")
        self.assertEqual(204, response.status_code)
        self.assertEqual(b"", response.content)

    def test_add_relationship_to_a_book(self):
        book = Book.objects.create(name="Title", published=datetime.utcnow())
        author = Author.objects.create(first_name="First", last_name="Last")
        book_response = self.client.get(f"/books/{book.id}/", HTTP_ACCEPT="application/vnd.api+json")
        content = json.loads(book_response.content)
        content["data"]["relationships"]["author"]["data"] = {"id": str(author.pk), "type": "authors"}
        response = self.client.patch(
            f"/books/{book.id}/",
            data=content,
            content_type="application/vnd.api+json",
            HTTP_ACCEPT="application/vnd.api+json",
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content)["data"]["relationships"]["author"]["data"]["id"], str(author.id))

    def test_use_sparse_fieldset(self):
        author = Author.objects.create(first_name="First", last_name="Last")
        response = self.client.get(
            f"/authors/{author.id}/?fields[authors]=last_name", HTTP_ACCEPT="application/vnd.api+json"
        )
        content = json.loads(response.content)
        self.assertEqual({"last_name": "Last"}, content["data"]["attributes"])

    def test_use_sorting(self):
        Author.objects.create(first_name="First", last_name="A")
        Author.objects.create(first_name="First", last_name="Z")
        response = self.client.get("/authors/?sort=last_name", HTTP_ACCEPT="application/vnd.api+json")
        content = json.loads(response.content)
        self.assertEqual("A", content["data"][0]["attributes"]["last_name"])
        self.assertEqual("Z", content["data"][1]["attributes"]["last_name"])

    def test_use_sorting_descending(self):
        Author.objects.create(first_name="First", last_name="A")
        Author.objects.create(first_name="First", last_name="Z")
        response = self.client.get("/authors/?sort=-last_name", HTTP_ACCEPT="application/vnd.api+json")
        content = json.loads(response.content)
        self.assertEqual("Z", content["data"][0]["attributes"]["last_name"])
        self.assertEqual("A", content["data"][1]["attributes"]["last_name"])

    def test_get_included(self):
        author = Author.objects.create(first_name="First", last_name="Last")
        book = Book.objects.create(name="Title", published=datetime.utcnow(), author=author)
        book_response = self.client.get(f"/books/{book.id}/?include=author", HTTP_ACCEPT="application/vnd.api+json")
        content = json.loads(book_response.content)
        expected = {
            "data": {
                "type": "books",
                "id": "1",
                "attributes": {"name": "Title", "published": book.published.date().isoformat()},
                "relationships": {"author": {"data": {"type": "authors", "id": "1"}}},
            },
            "included": [{"type": "authors", "id": "1", "attributes": {"first_name": "First", "last_name": "Last"}}],
        }
        self.assertEqual(expected, content)

    def test_get_dasherized_type(self):
        paper = PaperSource.objects.create(company="GeorgiaPacific")
        book_response = self.client.get(f"/paper-sources/{paper.id}/", HTTP_ACCEPT="application/vnd.api+json")
        content = json.loads(book_response.content)
        expected = {"data": {"type": "paper-sources", "id": "1", "attributes": {"company": "GeorgiaPacific"}}}
        self.assertEqual(expected, content)
