import requests
import os
os.chdir('D:/Dr.HanInXMU/读书挖坑之旅/GAN/beautilful_girl_dataset')
from tqdm import tqdm

class HtmlDownloader:
    def download(self, url):
        if url is None:
            return None

        r = requests.get(url)
        if r.status_code == 200:
            return r.content

    def save_fig(self, urls, path):
        if not os.path.exists(path):
            os.makedirs(path)
        for url in tqdm(urls):
            try:
                image_data = self.download(url)
            except:
                continue

            file_name = path + '/' + url.split('/')[-1]
            with open(file_name, 'wb') as image:
                image.write(image_data)
