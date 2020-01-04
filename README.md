## RSS_reader by Stychnevsky Anton
This packege will help you to manage news in RSS format: take them from websites, print in different easy-to-read formats, cach and so on.

## Requirement
You need to have Python >= 3.7 and Linux OS to use this package.<br/>
Also program need to some external libraries:<br/>
-feedparser<br/>
-bs4<br/>

They will be installed automaticly using "install_requires" argument in setup.py file


## Package instalation

1) Please install wheel and setuptools if you dont have it:<br/>
    pip install wheel<br/>
    pip install setuptools

2) Install RSS reader:<br/>
    pip install git+https://github.com/Stychnevsky/RSS_reader
    
3) Now you can use CLI ("rss-parser" command)<br/>
    rss-reader https://news.yahoo.com/rss/ #example<br/>

## Program improvment
Now you see 2.0 utility version. It is better than the 1.0, but published later than the deadline on EPAM courses.
If you want to see 1.0 version, please look at this commit: 
https://github.com/Stychnevsky/RSS_reader/tree/c19590afb8584e612f9c96f7f5d3673d8285afb9

## Usage 
Usage: rss_reader.py [-h] [--version] [--json] [-v][--verbose] [-l][--limit LIMIT] [-d][--date]<br/>
                     source
Positional arguments:<br/>
'sourse' - URL to parse feed

Optional reguments:<br/>
'-h', '--help' - Pring information about package and exit program<br/>
'--version' - Print version of program and exit program. It will change after every usage of programe<br/>
'--json' - News will be printed in json format<br/>
'--verbose' - Turn on outputing verbose statuse messages<br/>
'--limit LIMIT - - limit number of news from sourse if this parametr provided<br/>
'date DATE''- prints cached feeds starting out for some date. If source provided, it will print only news from this sourse, another way.


JSON structure (1 JSON = 1 Feed, not Feeds list):<br/>
{<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'access_time': 01.01.1900 00:00:00,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'feed_url': example.com/rss,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'published': 01.01.2019 00:00:00,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'source': , example.com,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'feed_description': self.feed_title.description,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'entries':<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'title': 'News title',<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'link': 'example.com/news1.html',<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'description': 'News summary',<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'img_links:':<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'img_saver.com/1234.png',<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;']<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'published': 01.01.2018 00:00:00,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br/>
&nbsp;&nbsp;&nbsp;&nbsp;']<br/>
}<br/>
        

# Examples
rss_reader.py https://onliner.by/feed --json -l 5<br/>
Print 5 latest news from onliner.by i json format<br/>

rss_reader.py https://news.yahoo.com/rss/ -v <br/>
Print all news from yahoo and output verbosr status messages<br/>

rss_reader.py --date 20191210 <br/>
Print all news from cache file, which are loaded not later than 10.12.2019<br/>
