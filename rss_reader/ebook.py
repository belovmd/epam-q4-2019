import requests
import os
import zipfile
import datetime


def create_html_for_epub(entry, file_name, entry_num=1, entries_count=1):
    file = open(file_name, "w", encoding="utf8")
    file.write('<html xmlns="http://www.w3.org/1999/xhtml">')
    file.write("\n<head>")
    file.write("\n<title>" + entry.title + "</title>")
    file.write("\n</head>")
    file.write("\n<body>")
    file.write("\n<strong>" + entry.title + "</strong>" + "\n<p>")
    file.write(entry.description)
    file.write("<br /><br /><i>Дата публикации: " + entry.published)
    file.write("<br />Новость " + str(entry_num) + "/" + str(entries_count)+"</i>")
    file.write("</p>")
    file.write("\n</body>")
    file.write("\n</html>")
    file.close()


def generate_epub(feed, path, file_name=None):

    info = {"link": "http://www.wuxiaworld.com/emperor-index/emperor-chapter-",
            "ChapterName": "Entry # ",
            "NovelName": feed.feed_title.title,
            "author": "Stychnevsky Anton"}
    today = datetime.datetime.now()
    if not file_name:
        title = "".join(
            [symb for symb in feed.feed_title.title if symb.isalpha() or symb.isdigit() or symb == ' ']).rstrip()
        file_name = title + ' ' + today.strftime("%b-%d-%Y")

    project_dir = os.getcwd()
    try:
        os.chdir(path)
    except Exception:
        print('Can not change direction to path. Files will be saved into RSS-reader directory')
    epub = zipfile.ZipFile(file_name + ".epub", "w")
    epub.writestr("mimetype", "application/epub+zip")

    epub.writestr("META-INF/container.xml", '''<container version="1.0"
    xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
      <rootfiles>
        <rootfile full-path="OEBPS/Content.opf" media-type="application/oebps-package+xml"/>
      </rootfiles>
    </container>''')

    index_tpl = '''<package version="3.1"
    xmlns="http://www.idpf.org/2007/opf">
      <metadata>
        %(metadata)s
          </metadata>
            <manifest>
              %(manifest)s
            </manifest>
            <spine>
              <itemref idref="toc" linear="no"/>
              %(spine)s
            </spine>
    </package>'''

    manifest = ""
    spine = ""
    metadata = '''<dc:title xmlns:dc="http://purl.org/dc/elements/1.1/">%(novelname)s</dc:title>
     <dc:creator xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:ns0="http://www.idpf.org/2007/opf" ns0:role="aut" ns0:file-as="NaN">%(author)s</dc:creator>
       <meta xmlns:dc="http://purl.org/dc/elements/1.1/" name="calibre:series" content="%(series)s"/>''' \
               % {
                   "novelname": info['NovelName'], "author": info['author'], "series": info['NovelName']}

    toc_manifest = '<item href="toc.xhtml" id="toc" properties="nav" media-type="application/xhtml+xml"/>'

    for num, entry in enumerate(feed.entries):
        html = info["ChapterName"] + str(num + 1) + ".xhtml"
        create_html_for_epub(entry, html, entry_num=num + 1, entries_count=len(feed.entries))
        basename = os.path.basename(html)
        manifest += '<item id="file_%s" href="%s" media-type="application/xhtml+xml"/>' % (num + 1, basename)
        spine += '<itemref idref="file_%s" />' % (num + 1)
        epub.write(html, "OEBPS/" + basename)
        os.remove(html)

    epub.writestr("OEBPS/Content.opf", index_tpl % {
        "metadata": metadata,
        "manifest": manifest + toc_manifest,
        "spine": spine, })

    toc_start = '''<?xml version='1.0' encoding='utf-8'?>
   <!DOCTYPE html>
   <html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
       <head>
           <title>%(novelname)s</title>
       </head>
           <body>
               <section class="frontmatter TableOfContents">
           <header>
               <h1>News digest</h1>
               <h1>%(today)s</h1>
           </header>
               <nav id="toc" role="doc-toc" epub:type="toc">
                   <ol>
                       %(toc_mid)s
                       %(toc_end)s'''
    toc_mid = ""
    toc_end = '''</ol></nav></section></body></html>'''

    epub.writestr("OEBPS/toc.xhtml", toc_start % {"novelname": info['NovelName'],
                                                  "toc_mid": toc_mid,
                                                  "toc_end": toc_end,
                                                  "today": today.strftime("%b-%d %H:%M")})
    epub.close()
    os.chdir(project_dir)


def generate_html(feed, path, file_name=None):
    today = datetime.datetime.now()
    if not file_name:
        title = feed.feed_title.title
        title = "".join([symb for symb in title if symb.isalpha() or symb.isdigit() or symb == ' ']).rstrip()
        file_name = title + ' ' + today.strftime("%b-%d-%Y") + '.html'


    project_dir = os.getcwd()
    try:
        os.chdir(path)
    except Exception:
        print('Can not change direction to path. Files will be saved into RSS-reader directory')
    file = open(file_name, "w", encoding="utf8")
    file.write('<h1 align="center">News digest - ' + today.strftime('%b-%d %H:%M') + '<br /></h1>')
    for entry in feed.entries:
        file.write(requests.get(entry.link).text)
    file.write('<h2><br />2020 Stychnevsky RSS-reader. Thank for using</h2>')
    file.close()
    os.chdir(project_dir)
