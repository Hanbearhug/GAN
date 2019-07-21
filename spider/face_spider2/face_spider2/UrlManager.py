import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

class UrlManager:
    def __init__(self):
        self.headers = {'Host': 'm.woyaogexing.com',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                           'Connection': 'keep-alive',
                           'Cookie': '__cfduid=d93472216030784a91b614b395f862d911563712586; Hm_lvt_0f4843d2ac6608e803f8c3154dc8c5e9=1563712589,1563713083; Hm_lpvt_0f4843d2ac6608e803f8c3154dc8c5e9=1563713733'}
        print('*'*50)
        print('开始获得美女主页链接！')
        self.category_url = self.get_category_url()
        print(f'获取主页链接完毕，共{len(self.category_url)}个主页！')
        print('*' * 50)
        print(f'开始获取头像图片地址！')
        self.img_urls = self.get_img_url()
        print(self.img_urls[0])



    def get_category_url(self):
        """
        获取一个未爬取的URL
        :return:
        """
        output = []
        i = 1
        pre_url = 'https://m.woyaogexing.com'
        while True:
            try:
                face_total_url = 'https://m.woyaogexing.com/touxiang/nv/top/index_' + str(i) + '.html'
                face_total_text = requests.get(face_total_url, headers=self.headers)
                soup = BeautifulSoup(face_total_text.text, 'html.parser')
                face_page = soup.find_all('a', attrs={'target': '_blank'})
                for page in face_page:
                    output.append(pre_url + page.get('href'))
                i += 1
                if i % 10 == 0:
                    print(f'已爬取{i}页')
            except:
                break
        return output

    def get_img_url(self):
        output_page = []
        pre_url = 'https:'
        for face_page_url in tqdm(self.category_url):
            face_page_text = requests.get(face_page_url, headers=self.headers)
            soup = BeautifulSoup(face_page_text.text, 'html.parser')
            imgs = soup.find_all('img', attrs={'class': 'lazy'})
            for img in imgs:
                output_page.append(pre_url + img.get('data-src'))
        return output_page