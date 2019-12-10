class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class FetchRssError(Error):
    def __init__(self, message):
        self.message = message


class RssReaderCriticalError(Error):
    def __init__(self, message):
        self.message = message
