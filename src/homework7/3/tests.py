from contextlib import redirect_stdout
from io import StringIO
import sys
from task_1_3 import add_to_list_in_dict
import unittest

sys.path.insert(1, "../1")


class TestRunner(unittest.TestCase):
    def test_run(self):
        months = {1: ["January"], 3: ["March"], 4: ["April"], 5: ["May"],
                  6: ["June"], 7: ["July"], 8: ["August"], 9: ["September"],
                  10: ["October"], 11: ["November"], 12: ["December"]}
        output = StringIO()
        with redirect_stdout(output):
            add_to_list_in_dict(months, 3, "M?rz")
            add_to_list_in_dict(months, 2, "February")
            add_to_list_in_dict(months, 2, "Februar")
            self.assertEqual(output.getvalue(),
                             "3 already has 1 elements.\n" +
                             "Added M?rz to 3.\n" +
                             "Created 2.\n" +
                             "Added February to 2.\n" +
                             "2 already has 1 elements.\n" +
                             "Added Februar to 2.\n")


if __name__ == '__main__':
    unittest.main()
