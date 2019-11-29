"""Cover function from 1.3 with tests."""

from exception_practice import add_to_list_in_dict
from contextlib import redirect_stdout
from io import StringIO
import unittest


class TestDict(unittest.TestCase):

    def test_not_existing(self):
        dct = {}

        out = StringIO()
        with redirect_stdout(out):
            add_to_list_in_dict(dct, "list1", 10)

        self.assertEqual(dct, {"list1": [10]})
        self.assertEqual(out.getvalue(),
                         "Created list1.\n"
                         "Added 10 to list1.\n")

    def test_existing(self):
        dct = {"list1": [10]}

        out = StringIO()
        with redirect_stdout(out):
            add_to_list_in_dict(dct, "list1", 20)

        self.assertEqual(dct, {"list1": [10, 20]})
        self.assertEqual(out.getvalue(),
                         "list1 already has 1 elements.\n"
                         "Added 20 to list1.\n")
