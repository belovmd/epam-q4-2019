"""There are all the logic of the utility in this module and only functions are

used here
"""

import __init__
from bs4 import BeautifulSoup
import colored
from datetime import datetime
from ebooklib import epub
import feedparser
import json
import logging
import os
from xml.dom import minidom


def choose_action(**kwargs):
    """Depending on the arguments passed by the user, determines what action

    will be performed next and calls related function. if called function
    returns not None, prints results in human-readable format. Also saves
    news into the cache in some cases.
    """
    source = kwargs['source']
    if kwargs['version']:
        version = show_version()
        print(version)
    elif kwargs['verbose']:
        show_logs(kwargs)
    elif kwargs['date']:
        news = show_date_news(source, kwargs['date'])
        print(news)
    else:
        tag_values = group_tag_values(source, kwargs['limit'])
        if tag_values:
            headers = tag_values[:6]
            cache = tag_values[6]
            save_news_into_cache(cache)
            if kwargs.get('json_'):
                json_output = show_news_as_json(headers)
                print(json_output)
            elif kwargs.get('to_fb2'):
                create_fb2(headers, kwargs['path'])
            elif kwargs.get('to_epub'):
                create_epub(headers, kwargs['path'])
            elif kwargs.get('colorize'):
                colored_news = show_colored_news(headers)
                print(colored_news)
            else:
                news = show_news_as_text(headers)
                print(news, end='')


def show_version():
    """Define current version of the program (current iteration number)."""
    version = 'Iteration ' + __init__.__version__
    return version


def show_logs(kwargs):
    """All arguments parsed by argparse are logged by the program. This

    function takes dict formed from these arguments and prints it in stdout.
    """
    args = ''
    for key, value in kwargs.items():
        arg = key + ' - ' + str(value) + '\n'
        args += arg
    logging.info('\nArguments: \n{}'.format(args))


def show_date_news(source, date):
    """Search for all news by specified date. If news are found the function

    returns compiled news for futher printing out. If not, error message is
    printed. See README.md for more details (paragraph 4 and "News caching"
    in the end of file).
    """
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'cache.json')
    try:
        with open(file_path, 'r') as cache_file:
            stored_cache = json.load(cache_file)
            if source in stored_cache and date in stored_cache[source]:
                all_news = stored_cache[source][date]
                date_to_edit = datetime.strptime(date, '%Y%m%d')
                news_to_print = date_to_edit.strftime('\n%A, %d %B:\n\n')
                for article in all_news:
                    news = all_news[article]
                    feed = '\nFeed: ' + news['Feed']
                    title = '\n\nTitle: ' + article
                    link = '\n\nLink: ' + news['Link']
                    text = '\n\nText: ' + news['Text']
                    img = '\n\nImage link: ' + news['image'] + '\n\n'
                    one_news = feed + title + link + text + img
                    news_to_print += one_news
                return news_to_print
            else:
                return 'Error: News are not found'
    except FileNotFoundError:
        return 'Error: News are not found'


def group_tag_values(source, limit):
    """Parse data and processes them. If "source" is not RSS URL, prints error

    message. If it's correct, right information is extracted from tags under
    the "limit" if it's indicated. Values of identical tags are grouped by
    lists and at the same time used for creating a dict with the news. Data
    from this dict further will be used for saving news into the cache.
    """
    data = feedparser.parse(source)
    entries = data.entries
    if entries:
        titles = []
        dates = []
        links = []
        texts = []
        images = []
        cache = {}
        feed = data.feed.get('title', 'Feed not found')
        news_limit = limit if limit and limit < len(entries) else len(entries)
        for ind in range(news_limit):
            title = entries[ind].get('title', 'Title not found')
            titles.append(title)
            pubDate = entries[ind].get('published', 'Date not found')
            dates.append(pubDate)
            link = entries[ind].get('link', 'Link not found')
            links.append(link)
            try:
                text = BeautifulSoup(entries[ind].summary, 'html.parser').text
            except AttributeError:
                text = 'Text not found'
            texts.append(text)
            soup = BeautifulSoup(str(entries[ind]), 'html.parser')
            try:
                image = soup.find("img")['src']
            except TypeError:
                image = 'Image link not found'
            images.append(image)
            date_edit = datetime.strptime(pubDate, '%a, %d %b %Y %H:%M:%S %z')
            edited_date = date_edit.strftime('%Y%m%d')
            cache[source] = cache.get(source, {})
            cache[source][edited_date] = cache[source].get(edited_date, {})
            cache[source][edited_date].update({title: {'Feed': feed,
                                                       'Link': link,
                                                       'Text': text,
                                                       'image': image}})
    else:
        print('Incorrect RSS URL')
        return False
    return feed, titles, dates, links, texts, images, cache


def show_news_as_json(headers):
    """Prepare news for console output. Takes values of all tags for each

    individual news and creates a dict with all news. Then this dict is
    converted to json for further printing in this format. See paragraph 5
    of README.md for more details about chosen JSON structure.
    """
    feed, titles, dates, links, texts, images = headers
    news = {}
    news_limit = len(titles)
    for index in range(news_limit):
        title = titles[index]
        pubDate = dates[index]
        link = links[index]
        text = texts[index].replace('\n', '')
        image = images[index]
        news[title] = {'Feed': feed, 'Date': pubDate, 'Link': link,
                       'Text': text, 'Image link': image}
    json_output = json.dumps(news)
    return json_output


def show_news_as_text(headers):
    """Prepare news for console output. Takes values of all tags for each

    individual news and bringes them together in the string format for further
    printing in human-readable format.
    """
    feed, titles, dates, links, texts, images = headers
    news_limit = len(titles)
    news_to_print = ''
    for index in range(news_limit):
        Feed = '\nFeed: ' + feed
        title = '\n\nTitle: ' + titles[index]
        date = '\n\nDate: ' + dates[index]
        link = '\n\nLink: ' + links[index]
        text = '\n\nText: ' + texts[index]
        img = '\n\nImage link: ' + images[index] + '\n\n'
        one_news = Feed + title + date + link + text + img
        news_to_print += one_news
    return news_to_print


def save_news_into_cache(cache):
    """Save news into the cache. The function takes as argument the dict with

    the news from the specified URL (abbreviated as CACHE). See "News caching"
    in the end of README.md for more details about the format of this dict.
    The sequence of actions performed by the function:
    1. Checkes whether .json file with the cache already exists.
    2. If such file exists, cached news from it are unloaded in dict
    (abbreviated as STORED_CACHE). This dict is compared with CACHE.
    3. Checkes if specified URL from CACHE exist in STORED_CACHE.
    4. If this URL exists, checks each news from CACHE whether it exists in
    STORED_CACHE's specified URL's news. If news doesn't exist, STORED_CACHE's
    specified URL's is updated by this news.
    5. Converts STORED_CACHE to json and write it to the file.
    6. If the conditions of step 1 are not met, steps 2-5 are skipped. The
    function converts CACHE to json and write it to the file.
    """
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'cache.json')
    try:
        with open(file_path, 'r') as cache_file:
            stored_cache = json.load(cache_file)
            for key in cache:
                stored_cache[key] = stored_cache.get(key, {})
                if stored_cache[key]:
                    stored_dates = stored_cache[key]
                    cache_dates = cache[key]
                    for key2 in cache_dates:
                        stored_dates[key2] = stored_dates.get(key2, {})
                        stored_dates[key2].update(cache_dates[key2])
                else:
                    stored_cache[key].update(cache[key])
    except FileNotFoundError:
        stored_cache = cache
    with open(file_path, 'w') as cache_file:
        json.dump(stored_cache, cache_file)


def create_fb2(headers, path):
    """Generate .fb2 file with news. Takes values of all tags for each

    individual news and creates a string with xml marking from them. This
    string is written to the file in .fb format. This file is saved to the
    directory specified in "output-path" or to the directory of executable
    file if the argument "output-path" wasn't provided. Saved file contains
    pictures if there were found links to images to the indicated RSS URL.
    """
    titles, dates, links, texts, images = headers[1:]
    doc = minidom.Document()
    root = doc.createElement('FictionBook')
    root.setAttribute('xmlns:l', 'http://www.w3.org/1999/xlink')
    root.setAttribute('xmlns', 'any')
    doc.appendChild(root)
    body = doc.createElement('body')
    root.appendChild(body)
    news_limit = len(titles)
    for ind in range(news_limit):
        body_title = doc.createElement('title')
        body.appendChild(body_title)
        title = doc.createElement('p')
        title_text = doc.createTextNode(titles[ind])
        title.appendChild(title_text)
        body_title.appendChild(title)
        link = doc.createElement('a')
        link.setAttribute('l:href', '{}'.format(links[ind]))
        link_text = doc.createTextNode('Read more')
        link.appendChild(link_text)
        body.appendChild(link)
        date = doc.createElement('p')
        date_text = doc.createTextNode(dates[ind])
        date.appendChild(date_text)
        body.appendChild(date)
        empty_line = doc.createElement('empty-line')
        body.appendChild(empty_line)
        news = doc.createElement('p')
        news_text = doc.createTextNode(texts[ind])
        news.appendChild(news_text)
        body.appendChild(news)
        empty_line = doc.createElement('empty-line')
        body.appendChild(empty_line)
        image = doc.createElement('image')
        image.setAttribute('l:href', '#{}'.format(images[ind]))
        body.appendChild(image)
    xml_str = doc.toprettyxml(indent="  ", encoding='utf-8')
    script_dir = os.path.dirname(__file__)
    if path:
        file_path = os.path.join(path, 'news.fb2')
    else:
        file_path = os.path.join(script_dir, 'news.fb2')
    with open(file_path, "wb") as file:
        file.write(xml_str)


def create_epub(headers, path):
    """Generate .epub file with news.

    1. Sets the file's metadata.
    2. Creates chapters using values of all tags for each individual news.
    3. Creates navigation.
    4. Write all data to the file in .epub format.
    This file is saved to the directory specified in "output-path" or to
    the directory of executable file if the argument "output-path" wasn't
    provided.
    """
    feed, titles, dates, links, texts = headers[:5]
    book = epub.EpubBook()
    book.set_identifier('Breaking_news')
    book.set_title(feed)
    book.set_language('en')
    book.add_author('User')
    spine = ['nav']
    news_limit = len(titles)
    for i in range(news_limit):
        news = epub.EpubHtml(title=titles[i], file_name='{}.xhtml'.format(i))
        tags = u'<h1>{}</h1><p>{}</p><p>{}</p><p>{}</p>'
        news.content = tags.format(titles[i], dates[i], links[i], texts[i])
        book.add_item(news)
        book.toc.append(epub.Link('{}.xhtml'.format(i), titles[i], titles[i]))
        spine.append(news)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = spine
    script_dir = os.path.dirname(__file__)
    if path:
        file_path = os.path.join(path, 'news.epub')
    else:
        file_path = os.path.join(script_dir, 'news.epub')
    epub.write_epub(file_path, book, {})


def show_colored_news(headers):
    """Prepare news for console output in colorized mode.

    Takes values of all tags for each individual news and bringes them
    together in the string format simultaneously changing their foreground
    and (or) background color.
    """
    feed, titles, dates, links, texts, images = headers
    reset = colored.attr('reset') + '\n'
    bold = colored.attr('bold')
    white = colored.fg('white')
    black = colored.fg('black')
    turquoise_fg = colored.fg('turquoise_2')
    magenta = colored.bg('light_magenta')
    turquoise_bg = colored.bg('turquoise_2')
    light_yellow = colored.bg('light_yellow')
    light_green = colored.bg('light_green')
    light_red = colored.bg('light_red')

    feed_colored = '\n' + magenta + white + bold + 'Feed: '
    title_colored = reset + '\n' + turquoise_bg + black + 'Title: '
    date_colored = reset + light_yellow + black + 'Date: '
    link_colored = reset + light_green + black + 'Link: '
    text_colored = reset + light_red + white + 'Text: '
    img_colored = reset + turquoise_fg + bold + 'Image link: '

    news_limit = len(titles)
    colored_news = ''
    for index in range(news_limit):
        Feed = feed_colored + feed
        title = title_colored + titles[index]
        date = date_colored + dates[index]
        link = link_colored + links[index]
        text = text_colored + texts[index]
        img = img_colored + images[index] + '\n\n'
        one_news = Feed + title + date + link + text + img
        colored_news += one_news
    return colored_news
