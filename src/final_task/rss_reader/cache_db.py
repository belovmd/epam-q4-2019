import logging.config
import os
import sqlite3
from sqlite3 import Error

from dateutil.parser import parse

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "news.db")
cache_db_logger = logging.getLogger("cache_db_logger")


def create_connection(db_file=DB_PATH):
    """Create a database connection to the SQLite database specified by db_file

    :param db_file: database file
    :return: Connection object or None
    """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        cache_db_logger.error(e)
    return conn


def create_news_table(conn):
    """Create a new news table if none exists"""
    cur = conn.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    cache_db_logger.debug("SQLite version:", cur.fetchone())

    newsitems_tbl_sql = """CREATE TABLE IF NOT EXISTS news (
                        channel text,
                        title text UNIQUE,
                        date DATE UNIQUE,
                        link text UNIQUE,
                        description text,
                        HTML_desc text
                        )"""
    cur.execute(newsitems_tbl_sql)
    return cur.lastrowid


def create_newsitem(conn, channel, values):
    digested_values = values.values()
    cur = conn.cursor()
    newsitem_item_sql = """INSERT OR IGNORE INTO news
                        (channel, title, date, link, description, HTML_desc)
                        VALUES (?, ?, ?, ?, ?, ?)
                        """
    cur.execute(newsitem_item_sql, (channel, *digested_values))
    return cur.lastrowid


def show_db(conn, user_date):
    cur = conn.cursor()
    digested_date = parse(user_date)
    newsitem_item_sql = (
        "SELECT * FROM news "
        "WHERE date > ?"
        "AND date < date(?, '+1 day')"
        "ORDER BY date DESC"
    )
    cur.execute(newsitem_item_sql, (digested_date, digested_date))
    result = cur.fetchall()
    if result:
        return result
    else:
        return Exception("No news for this date")
