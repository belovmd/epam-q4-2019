import io
import unittest
import unittest.mock

from m1_3 import add_to_list_in_dict


class AddToListInDict(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        add_to_list_in_dict(*n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_barBaz(self):
        self.assert_stdout(({'foo': [1], 'bar': [2]}, 'baz', 3),
                           'Created baz.\nAdded 3 to baz.\n')

    def test_barBar(self):
        self.assert_stdout(({'foo': [1], 'bar': [2]}, 'bar', 3),
                           'bar already has 1 elements.\n''Added 3 to bar.\n')

    def test_empty(self):
        with self.assertRaises(TypeError):
            add_to_list_in_dict()


if __name__ == '__main__':
    unittest.main()
