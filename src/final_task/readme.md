# One-shot command-line RSS reader

Version 0.2.0

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

Limit parsed data
`--limit 42`


## Test

Run all tests

`nosetests tests --with-coverage --cover-package=rss_reader`


## JSON sample
```json
[
    "Yahoo News - Latest News & Headlines",
    [
        {
            "Title": "GOP lawmaker says 'out-of-the-box strategy' could give Trump an 'advantage' in impeachment hearings",
            "Date": "Sun, 08 Dec 2019 12:28:50 -0500",
            "Link": "https://news.yahoo.com/gop-lawmaker-says-outofthebox-strategy-could-give-trump-an-advantage-in-impeachment-hearings-172850668.html",
            "Description": "Rep. Matt Gaetz said it would play to the \u201cpresident\u2019s advantage\u201d to have his top administration officials testify in the upcoming impeachment hearings."
        },
        {
            "Title": "Serial rapist given 33 life sentences after UK rampage while wrongly free",
            "Date": "Mon, 09 Dec 2019 10:55:27 -0500",
            "Link": "https://news.yahoo.com/serial-rapist-given-33-life-155527846.html",
            "Description": "A convicted burglar who assaulted and raped women and children during a two-week rampage across Britain while wrongly free from jail was given 33 life sentences on Monday, with the judge saying he would never cease to be a danger to society. Joseph McCann, 34, was convicted of 37 offences relating to 11 victims aged between 11 and 71, committed in April and May this year. Sentencing him at London's Old Bailey Court, judge Andrew Edis said he was \"a coward, a violent bully and a paedophile\"."
        },
    ]
]
```

