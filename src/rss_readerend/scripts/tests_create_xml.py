from scripts.create_fb2 import create_fb2
import unittest


class TestsCreateXml(unittest.TestCase):

    def test_create_fb2_without_path(self):
        json_data = {'India': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date'],
                     'Europe': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date']}

        expect_xml_str = b'<?xml version="1.0" encoding="utf-8"?>\n<FictionBook ' \
                         b'xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" ' \
                         b'xmlns:l="http://www.w3.org/1999/xlink">\n  <description>\n    ' \
                         b'<title-info>\n      <author>\n        <first-name>Pavel</first-name>\n' \
                         b'        <last-name>Martysiuk</last-name>\n      </author>\n      ' \
                         b'<book-title>RSS-reader</book-title>\n    </title-info>\n    <document-info>\n' \
                         b'      <date>2019</date>\n    </document-info>\n  </description>\n  <body>\n    <title>\n' \
                         b'      <p>India</p>\n    </title>\n    <p>Sat, 07 Dec 2019 05:17:55 -0500</p>\n' \
                         b'    <a l:href="url">link</a>\n    <empty-line/>\n    <p>description</p>\n    <title>\n' \
                         b'      <image l:href="#0.jpg"/>\n    </title>\n    <p>Image not found</p>\n    <title>\n' \
                         b'      <p>Europe</p>\n    </title>\n    <p>Sat, 07 Dec 2019 05:17:55 -0500</p>\n' \
                         b'    <a l:href="url">link</a>\n    <empty-line/>\n    <p>description</p>\n    <title>\n' \
                         b'      <image l:href="#1.jpg"/>\n    </title>\n    <p>Image not found</p>\n' \
                         b'  </body>\n</FictionBook>\n'

        out_put_xml = create_fb2(json_data)
        self.assertEqual(expect_xml_str, out_put_xml)


if __name__ == '__main__':
    unittest.main()
