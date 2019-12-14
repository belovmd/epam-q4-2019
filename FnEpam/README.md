RSS reader is a command utility, which receives RSS URL and prints the result in convenient output format

Input data has the following interface:

`rss_reader.py source S [-h] [--limit LIMIT] [--verbose] [--version] [--json]
                   [--epub] [--date DATE] [--output OUTPUT]`
````
positional arguments:
S - URL which provides a RSS feed
optional arguments:
-h - prints this help page
--version - prints in stdout current version
--verbose - prints all logs in stdout
--json - prints news in JSON format
--limit LIMIT - limits the amount of news entries in the output
-- date DATE - retrieves news from local storage by date.
-- epub  - conver news to epub format.
--output OUTPUT - CLI saves news in fb2 format along this path
````
How use?
````

news-parser https://news.yahoo.com/rss -prints news from site(default 1)

````
JSON structure:
	 
```

{
		"Title":[date, link, description]  
		...
	},
Example:
{
  "Title:Yes, China&#39;s New Submarine-Launched Nuclear Missiles Could Destroy America": [
        "Thu, 12 Dec 2019 10:00:00 -0500",
        "Link:https://news.yahoo.com/yes-chinas-submarine-launched-nuclear-150000893.html\n",
        [
            "But that's why we have M.A.D."
        ]
    ]
}

````
Cache JSON structure
	 
```

{
		"Date":[Title]  
		...
	},
Example:
{
    "20191212": [
        "Title:For Gaetz to raise Hunter Biden&#39;s substance abuse is &#39;the pot calling the kettle black,&#39; Johnson says",
        "Title:Fire on Russia&#39;s only aircraft carrier kills 1, injures 11",
        "Title:Jersey City shooting: Who are the Black Hebrew Israelites?"
    ],
    "20191213": [
        "Title:How North Korea Could Start a War: Test a Nuclear Weapon in the Atmosphere",
        "Title:British Author Found Dead and Buried in Woods Near Her Dominican Republic Home",
        "Title:Impeachment charges head to House; Trump cries anew: &#39;Hoax&#39;"
    ]
}

````
How install?
````
1) python setup.py install
2) news-parser https://news.yahoo.com/rss 	
