from django.test import TestCase


class TestMyApp(TestCase):
    def test_pass(self):
        self.assertTrue(True)


def test_pass():
    assert True
