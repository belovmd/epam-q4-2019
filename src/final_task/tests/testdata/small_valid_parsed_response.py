import datetime
from dateutil.tz import tzoffset

title = "Yahoo News - Latest News & Headlines"
items = [
    {
        "Title": "Mueller witness bragged about access to Clintons secured "
        "with illegal campaign cash, says Justice Department",
        "Date": datetime.datetime(
            2019, 12, 5, 14, 38, 14, tzinfo=tzoffset(None, -18000)
        ),
        "Link": "https://news.yahoo.com/nader-bragged-to-middle-east-"
        "government-about-access-to-clintons-secured-with-illegal-"
        "campaign-cash-says-justice-department-193814757.html",
        "Description": "An emissary for two Arab princes boasted to unnamed "
        "officials of a Middle Eastern government about his "
        "direct access to Hillary and Bill Clinton while "
        "funneling more than $3.5 million in illegal campaign "
        "contributions to the 2016 Clinton campaign and "
        "Democratic fundraising committees, according to a "
        "federal indictment.",
    },
    {
        "Title": "Indiana judge grants stay of execution for federal inmate",
        "Date": datetime.datetime(
            2019, 12, 5, 21, 31, 33, tzinfo=tzoffset(None, -18000)
        ),
        "Link": "https://news.yahoo.com/indiana-judge-grants-stay-execution-"
        "023133024.html",
        "Description": "A convicted murderer set to become the first federal "
        "inmate to be executed in 16 years was granted a stay "
        "of execution on Thursday by a judge in Indiana. Daniel "
        "Lewis Lee, a white supremacist convicted in Arkansas "
        "of murdering a family of three, was granted the stay "
        "by U.S. District Judge James Patrick Hanlon. Lee's "
        "execution had been set for Monday, but a separate "
        "ruling by a judge in Washington last month put his "
        "execution and that of three other federal "
        "inmates on hold.",
    },
]
