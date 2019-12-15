# One-shot command-line RSS reader

Version 0.4.0

## Build

Update build tools before installation `python -m pip install --upgrade pip setuptools wheel`

Run from root folder `python setup.py sdist bdist_wheel`

##  Install 

After running build, run `pip install ./dist/rss_reader-0.2.0-py3-none-any.whl`

To uninstall, run `pip uninstall rss-reader`

## Launch

Print all newsitems from RSS 

### From sources

`python -m rss_reader.py https://news.yahoo.com/rss`

### From python packages

`python -m rss_reader https://news.yahoo.com/rss`

### From console

`rss-reader https://news.yahoo.com/rss`

Options

Print version and exit
`--version`

Dump data to JSON
`--json`

Limit printed data
`--limit 42`

Display cached data for specific day
`--date 20191214`

Covert to fb2
`--to-fb2`

Covert to epb
`to-epub`

Save converted file, do not pass extension or not-existing folders 
`--output-path ./dir/file`

## Test

Run all tests

`nosetests tests --with-coverage --cover-package=rss_reader`


## JSON sample
```json
[
    "Yahoo News - Latest News & Headlines",
    [
        {
            "Title": "F-35: Would You Spend $1,500,000,000,000 On a Plane That Can't Fly?",
            "Date": "2019-12-12 13:26:00-05:00",
            "Link": "https://news.yahoo.com/f-35-spend-1-500-182600680.html",
            "Description": "That's what the U.S. government did on the F-35.",
        },
        {
            "Title": "Parents of girl who fell to her death sue cruise company",
            "Date": "2019-12-12 19:53:54-05:00",
            "Link": "https://news.yahoo.com/parents-girl-fell-her-death-173512426.html",
            "Description": "The Indiana parents of a toddler who fell to her death out of an open cruise ship window in Puerto Rico filed a lawsuit Wednesday against Royal Caribbean Cruises, accusing the company of negligence by allowing the window to be opened. Chloe Wiegand fell to her death in July after her grandfather lifted her to the window on Royal Caribbean\u2019s Freedom of the Seas ship while the vessel docked. \u201cWe should be celebrating with presents and a birthday cake, but instead we are talking about her death,\u201d Chloe's mother, Kim Wiegand of Granger, Indiana, told reporters at a news conference in nearby South Bend.",
        }
    ]
]
```

## Data cache

Using sqlite to stash and retrieve data.


## Format conversion

Covert news items as HTML to a folder, then user pandoc to convert to other formats.