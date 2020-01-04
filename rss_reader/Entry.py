import html
from bs4 import BeautifulSoup
import re


class Entry:
    """ Entry is object of peace of news. It consist of some metadata, description and links for images, wich was
    founded in description. """
    def __init__(self, entry):
        self.title = html.unescape(entry.get('title', ''))
        self.link = entry.get('link', '')
        desc = html.unescape(entry.get('description', ''))
        self.published = entry.get('published', '')

        soup = BeautifulSoup(desc, 'html.parser')
        images = soup.find_all('img')
        self.img_links = [image.get('src', '') for image in images]
        self.img_titles = [image.get('alt', 'no title') for image in images]
        img_tag = re.compile('<img.*?>')
        for number_of_img in range(len(images)):
            img_title = self.img_titles[number_of_img]
            if img_title:
                img_title = ': ' + img_title
            desc = re.sub(img_tag, ' [image ' + str(number_of_img + 1) + img_title + '] ', desc, count=1)
        self.description = BeautifulSoup(desc, 'html.parser').get_text()

    def output(self):
        """ Function takes data from Entry and prepare it to printing. Output list is list of all Entry variables"""
        output_list = []
        if self.title:
            output_list.append(self.title)
        if self.link:
            output_list.append('Подробнее: ' + self.link)
        if self.description:
            output_list.append('\n' + self.description + '\n')
        if self.img_links:
            for img_url in enumerate(self.img_links, start=1):
                output_list.append('[' + str(img_url[0]) + ']: ' + img_url[1])
        if self.published:
            output_list.append('Дата публикации: ' + self.published)
        return output_list

    def output_to_json(self):
        """ Function which take data from Entry and prepare it to put in Feed JSON."""
        data = {
            'title': self.title,
            'link': self.link,
            'description': self.description,
            'img_links:': self.img_links,
            'published': self.published
        }
        return data
