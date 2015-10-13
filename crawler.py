from item import Item

class Crawler:
    def __init__(self):
        self.item_list = []

    def crawl_list(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def crawl_item(self):
        raise NotImplementedError("Subclass must implement abstract method")

class trumpetheraldCrawler(Crawler):
    def crawl_list(self):
        pass

    def crawl_item(self):
        pass

class vioworldCrawler(Crawler):
    def crawl_list(self):
        pass

    def crawl_item(self):
        pass

class kleinanzeigenCrawler(Crawler):
    def crawl_list(self):
        pass

    def crawl_item(self):
        pass

