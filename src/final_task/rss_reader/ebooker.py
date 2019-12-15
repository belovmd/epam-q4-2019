import os
import string
import subprocess

WD = os.path.dirname(os.path.realpath(__file__))  # Current working Directory
HTML_DIR = "HTML_Out"  # Storage location for the extracted HTML source
EBOOK_NAME = "test.epub"


def prepare_dirs(html_dir=HTML_DIR):
    """Create HTML storage dir"""
    if not os.path.exists(html_dir):
        os.mkdir(html_dir)


def cook_html(
    channel_title, channel_link, digested_news_item, html_dir=HTML_DIR
):
    """Make news HTML files"""
    of = html_dir + "/s{}.html".format(
        "".join(
            filter(
                lambda m: m in string.digits,
                digested_news_item["Date"].isoformat(),
            )
        )
    )
    with open(of, "w") as nif:
        nif.write("<h1>{}</h1>".format(digested_news_item["Title"]))
        nif.write("<p>{}<p>".format(digested_news_item["Date"]))
        nif.write(digested_news_item["HTML_desc"])
        nif.write(
            "<p href={}>{}</p>".format(
                digested_news_item["Link"], digested_news_item["Link"]
            )
        )
    # Feed title and Link to TOC
    toc_template = (
        "<!DOCTYPE html><html><head>"
        '< meta name = "author" content = "{}" / > '
        "<title>{}</title>"
        "</head></html>"
    )
    with open(HTML_DIR + "/s00000.html", "w") as tof:
        tof.write(toc_template.format(channel_link, channel_title))


def convert(EBOOK_NAME, EBOOK_FORMAT, output_dir=HTML_DIR):
    """Convert the directory of (Ordered HTML file's into a single EPub)"""
    subprocess.Popen(
        "pandoc -s -i {}/*.html -t {} -o {} --toc".format(
            output_dir, EBOOK_FORMAT, EBOOK_NAME
        ),
        cwd=WD,
        shell=True,
    ).wait()
