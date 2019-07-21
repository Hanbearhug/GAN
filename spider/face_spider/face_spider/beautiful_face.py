from HtmlDownload import HtmlDownloader
from UrlManager import UrlManager
class FaceSpider:
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.urlmanager = UrlManager()

    def crawl(self, path):
        url = self.urlmanager.img_urls
        self.downloader.save_fig(url, path)
if __name__ == "__main__":
    face = FaceSpider()
    face.crawl('beautifulFace')