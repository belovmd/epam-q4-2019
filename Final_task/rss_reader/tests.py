"""This module is intended for testing modules "news_functions" and "reader"

using unittest
"""

import __init__
import news_functions
import reader
import unittest


class TestNewsFunctions(unittest.TestCase):
    """In this class module 'news_functions' is tested"""

    def test_choose_action(self):
        """Сhecks if an error occurs when passing arguments to the function

        "choose_action"
        """
        with self.assertRaises(TypeError):
            news_functions.choose_action('key')

    def test_show_version(self):
        """Tests whether the function "show_version" shows current

        iteration version correctly.
        """
        version = 'Iteration ' + __init__.__version__
        self.assertEqual(news_functions.show_version(), version)

    def test_create_fb2(self):
        """Сhecks if ValueError error occurs when passing list of dicts to

        the function "create_fb2".
        """
        to_pass = [{'Feed': 'Yahoo'}, {'Title': 'Main'}, {'Link': 'No'}]
        with self.assertRaises(ValueError):
            news_functions.create_fb2(to_pass, __file__)

    def test_create_epub(self):
        """Tests whether IndexError would be raised when passing too long

        list to the function "create_epub".
        """
        to_pass = ['Feed', 'Title', 'Date', 'Text', 'Link', 'Img']
        with self.assertRaises(IndexError):
            news_functions.create_epub(to_pass, 'path')

    def test_show_logs(self):
        """Сhecks whether the function "show_logs" returns None."""
        self.assertIsNone(news_functions.show_logs({'news': 'BBC'}))

    def test_show_date_news(self):
        """Сhecks if the "show_date_news" function's return value is equal

        to the specified message.
        """
        result = news_functions.show_date_news('Shop', '2030')
        self.assertEqual(result, 'Error: News are not found')

    def test_group_tag_values(self):
        """Сhecks if an TypeError error occurs when not passing arguments to

        the function "group_tag_values".
        """
        with self.assertRaises(TypeError):
            news_functions.group_tag_values()

    def test_show_news_as_json(self):
        """Сhecks if the "show_date_news" function's returning dict is not

        equal to another dict.
        """
        tags = 'Yahoo', ['First'], ['2020'], ['page'], ['Now'], ['No']
        result = news_functions.show_news_as_json(tags)
        self.assertNotEqual(result, {'Yahoo': 'First', 'page': '2020'})

    def test_show_news_as_text(self):
        """Сhecks whether the "show_news_as_text" function's returning dict

        is equal to the specified dict.
        """
        tags = 'Yahoo', ['First'], ['2020'], ['page'], ['Now'], ['No']
        feed = '\nFeed: ' + 'Yahoo'
        title = '\n\nTitle: ' + 'First'
        date = '\n\nDate: ' + '2020'
        link = '\n\nLink: ' + 'page'
        text = '\n\nText: ' + 'Now'
        img = '\n\nImage link: ' + 'No' + '\n\n'
        expected = feed + title + date + link + text + img
        self.assertEqual(news_functions.show_news_as_text(tags), expected)

    def test_save_news_into_cache(self):
        """Tests whether TypeError would be raised when calling the function

        "save_news_into_cache" with incorrect argument's type.
        """
        with self.assertRaises(TypeError):
            news_functions.save_news_into_cache(10)

    def test_colored_news(self):
        """Сhecks if the result of calling "colored_news" function is not

        equal to a certain string.
        """
        to_pass = 'Yahoo', ['Title'], ['2020'], ['Link'], ['Text'], ['Img']
        result = news_functions.show_colored_news(to_pass)
        expected = 'Yahoo: Title: 2020: Link: Text: Img:'
        self.assertNotEqual(result, expected)


class TestReader(unittest.TestCase):
    """In this class module 'reader' is tested"""

    def test_date(self):
        """Сhecks whether the result of calling function "main"

        with two different non-existent dates would be equal.
        """
        result = reader.main(['news', '--date', '20201301'])
        expected = reader.main(['news', '--date', '20201132'])
        self.assertEqual(result, expected)

    def test_verbose(self):
        """Сhecks if the function "main" returns None after taking "verbose"

        argument.
        """
        result = reader.main(['http', '--verbose'])
        self.assertIsNone(result)

    def test_my_namespace(self):
        """Сhecks whether the module "reader" has no attribute

        "my_namespace".
        """
        self.assertFalse(hasattr(reader, 'my_namespace'))

    def test_version(self):
        """Сhecks if the "main" function's returning value is not

        equal to a certain string.
        """
        result = reader.main(['address', '--version'])
        self.assertNotEqual(result, 'Latest_version')


if __name__ == "__main__":
    unittest.main()
