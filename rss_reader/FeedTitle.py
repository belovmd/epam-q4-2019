class FeedTitle:
    def __init__(self, the_feed):
        self.title = the_feed.feed.get("title", "")
        self.link = the_feed.feed.get("link", "")
        self.description = the_feed.feed.get("description", "")
        self.published = the_feed.feed.get("published", "")

    def output(self):
        output_list = []
        if self.title:
            output_list.append('Новостой ресурс: ' + self.title)
        if self.link:
            output_list.append('Ссылка: ' + self.link)
        if self.description:
            output_list.append(self.description)
        if self.published:
            output_list.append('Обновлено: ' + self.published)
        return output_list



