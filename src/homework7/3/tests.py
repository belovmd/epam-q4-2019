from contextlib import redirect_stdout
from io import StringIO
import sys
from task_1_3 import add_to_list_in_dict
import unittest

sys.path.insert(1, "../1")


class TestRunner(unittest.TestCase):
    def test_empty_dict(self):
        months = {}
        output = StringIO()
        with redirect_stdout(output):
            add_to_list_in_dict(months, 1, "January")
            self.assertEqual(output.getvalue(),
                             "Created 1.\n" +
                             "Added January to 1.\n")

    def test_add_value(self):
        months = {1: ["January"]}
        output = StringIO()
        with redirect_stdout(output):
            add_to_list_in_dict(months, 1, "Janvier")
            self.assertEqual(output.getvalue(),
                             "1 already has 1 elements.\n" +
                             "Added Janvier to 1.\n")

    def test_add_key(self):
        months = {1: ["January", "Janvier"]}
        output = StringIO()
        with redirect_stdout(output):
            add_to_list_in_dict(months, 2, "February")
            self.assertEqual(output.getvalue(),
                             "Created 2.\n" +
                             "Added February to 2.\n")

    def test_add_duplicate_value(self):
        months = {1: ["January", "Janvier"], 2: ["February"]}
        output = StringIO()
        with redirect_stdout(output):
            add_to_list_in_dict(months, 1, "January")
            self.assertEqual(output.getvalue(),
                             "1 already has 2 elements.\n" +
                             "Added January to 1.\n")


if __name__ == '__main__':
    unittest.main()
