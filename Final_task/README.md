RSS reader
==========

    This is a command-line utility which receives RSS URL and prints results 
in human-readable format. Depending on the arguments, the program operates in 
different ways. It is used argparse module for parsing arguments. Utility is 
wrapped into distribution package with setuptools.

    There is one mandatory argument in the program: "source". All other 
arguments are positional: "version", "json", "verbose", "limit", "date". 
    
    HERE IS HOW IT WORKS:

- it is expected that argument "source" is always provided. That's why it's 
not indicated in all the situations described below.


GENERAL cases:


a) The following order of activities is established on any other cases except 
arguments "version", "verbose" or "date" are provided:

    Program tries to parse data from specified in "source" URL. If provided 
"source" is not RSS URL, utility prints error message and completing its work. 
If it's correct, program processes parsed data and convertes to news. Then 
news are saved into the cache ***

b) If argument "limit" is provided: 

    Program handles exactly as many news as is indicated in "limit" argument 
(not all the news). In case "limit" is bigger than number of found news, all 
news are processed.

    - it can be used without any other arguments or along with "json", "to-fb2", "to-epub", "colorize".


INDIVIDUAL cases:


1. If no arguments were provided:
    News are printed in console output using this format:

Feed, News title, Date published, Link to full news, Brief text, Link to image.

2. If argument is "version":
    Utility prints program's current version (iteration number).

3. If argument is "verbose":
    Utility prints all logs in stdout.

4. If argument is "date":
    Program checkes whether the file with the cache exists. If true, the cache 
from the file is unloaded. Then specified RSS URL in the cache is checked. If 
URL exists, program checkes whether specified date exist in this URL's cache. 
If true, all news from this date are printed out. If any of the above-mentioned 
conditions is not met, error message is printed.

5. If argument is "json":
    News are converted to json using this format:

{key: {key1: value1, key2: value2, key3: value3, key4: value4, key5: value5}}

In the case of the news it looks like this:

{News title: {Feed: ..., Date published: ..., Link to full news: ..., 
        Brief text: ..., Link to image: ...}}

When converted, json is printed in console output.

6. If argument is "to-fb2":
    Utility write news to the file to the directory of executable file in .fb 
format. Other than the header lines (including brief text of the news), this 
file contains pictures if there were found links to images to the indicated 
RSS URL.

7. If argument is "to-epub":
    Utility write news to the file to the directory of executable file in 
.epub format. Other than the header lines (including brief text of the news), 
this file has navigation menu of the news.

8. If argument is "output-path" with "to-epub" or with "to-fb2":
    Utility write news to the file to the directory specified in "output-path".

9. If argument is "colorize":
    News are printed in console output in colorized mode.



*** News caching

News are stored in the cache using JSON format: 

{RSS URL: {Date published: {News title: 
{Feed: ..., Link to full news: ..., Brief text: ..., Link to image: ...}}}}

This format allows easily search for news on the specified URL and date.

To save news into the cache the following order of activities is established:
    Program checkes whether the file with the cache already exists. 
    a) If not, the news that where just processed from specified URL are 
       saved into the cache. 
    b) If such file exists: 
       1) the cache from the file is unloaded;
       2) program takes only that processed news from specified URL which are 
          not in this URL's cache;
       3) these taken news are added to unloaded cache and the result is saved 
          into the cache.