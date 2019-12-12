import base64
import datetime
import requests
from xml.dom import minidom

"""Converts all saved news to fb2 format
If path saves the book to a directory on this path
Data is data from sites in json format or local storage.
json format  is {title:[pub_date,link, img_link, description, format_date]}
"""


def create_fb2(data, path=None):
    DATE_INDEX = 0
    LINK_INDEX = 1
    IMG_URL_INDEX = 2
    DESCRIPTION_INDEX = 3

    doc = minidom.Document()

    root = doc.createElement('FictionBook')
    root.setAttribute('xmlns:l', 'http://www.w3.org/1999/xlink')
    root.setAttribute('xmlns', 'http://www.gribuser.ru/xml/fictionbook/2.0')
    doc.appendChild(root)

    description = doc.createElement('description')
    root.appendChild(description)

    title_info = doc.createElement('title-info')
    description.appendChild(title_info)

    author = doc.createElement('author')
    title_info.appendChild(author)

    first_name = doc.createElement('first-name')
    first_name_text = doc.createTextNode('Pavel')
    first_name.appendChild(first_name_text)
    author.appendChild(first_name)

    last_name = doc.createElement('last-name')
    last_name_text = doc.createTextNode('Martysiuk')
    last_name.appendChild(last_name_text)
    author.appendChild(last_name)

    book_title = doc.createElement('book-title')
    book_title_text = doc.createTextNode('RSS-reader')
    book_title.appendChild(book_title_text)
    title_info.appendChild(book_title)

    document_info = doc.createElement('document-info')
    description.appendChild(document_info)

    date = doc.createElement('date')
    date_text = datetime.datetime.today().strftime('%Y')
    date_text = doc.createTextNode(date_text)
    date.appendChild(date_text)
    document_info.appendChild(date)

    body = doc.createElement('body')
    root.appendChild(body)

    keys = list(data.keys())
    length_data = len(data)
    for element in range(length_data):
        title = keys[element]
        info = data[title]
        date = info[DATE_INDEX]
        link = info[LINK_INDEX]
        img_url = info[IMG_URL_INDEX]
        description = info[DESCRIPTION_INDEX]

        body_title = doc.createElement('title')
        body.appendChild(body_title)

        p_title = doc.createElement('p')
        p_title_text = doc.createTextNode(title)
        p_title.appendChild(p_title_text)
        body_title.appendChild(p_title)

        p_date = doc.createElement('p')
        p_date_text = doc.createTextNode(date)
        p_date.appendChild(p_date_text)
        body.appendChild(p_date)

        """FB2 format does't support <a href= link>link</a>
        and <link>link</link>"""

        a_link = doc.createElement('a')
        a_link.setAttribute('l:href', f'{link}')
        a_link_text = doc.createTextNode('link')
        a_link.appendChild(a_link_text)
        body.appendChild(a_link)

        empty_line = doc.createElement('empty-line')
        body.appendChild(empty_line)

        p_description = doc.createElement('p')
        p_description_text = doc.createTextNode(description) if description \
            else doc.createTextNode('No description')
        p_description.appendChild(p_description_text)
        body.appendChild(p_description)

        if img_url:

            title = doc.createElement('title')
            body.appendChild(title)

            image = doc.createElement('image')
            image.setAttribute('l:href', '#{0}.jpg'.format(element))
            title.appendChild(image)

            binary = doc.createElement('binary')
            binary.setAttribute('id', '{0}.jpg'.format(element))
            binary.setAttribute('content-type', 'image/jpeg')

            binary_text = retrieve_image_from_url(img_url)

            if binary_text == 'Error':
                p = doc.createElement('p')
                p_text = doc.createTextNode('Image not found')
                p.appendChild(p_text)
                body.appendChild(p)
            else:
                binary_text = doc.createTextNode(binary_text)
                binary.appendChild(binary_text)
                root.appendChild(binary)
        else:
            p = doc.createElement('p')
            p_text = doc.createTextNode('Image not found')
            p.appendChild(p_text)
            body.appendChild(p)
    xml_str = doc.toprettyxml(indent="  ", encoding='utf-8')
    if path:
        with open(path + r'\data.fb2', 'wb') as file:
            file.write(xml_str)
    else:
        with open('data.fb2', "wb") as file:
            file.write(xml_str)
    return xml_str


"""url - img_url. Function opens  the img_url,
reads image  and conversion to base64 format"""


def retrieve_image_from_url(url):
    try:
        img = requests.get(url).content
        base64_img = str(base64.b64encode(img), encoding='utf-8')
        return base64_img
    except IOError:
        return 'Error'
