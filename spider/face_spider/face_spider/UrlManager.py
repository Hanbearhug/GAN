import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

class UrlManager:
    def __init__(self):
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
        face_total_url = 'http://www.zhaogexing.com/nvtouxiang/meinv/'
        face_total_text = requests.get(face_total_url).text
        soup = BeautifulSoup(face_total_text, 'html.parser')
        pageNums = soup.find('a', attrs={'class': 'end'}).get_text().split('.')[-1]
        output_face_profile = []
        for page in tqdm(range(1, int(pageNums) + 1)):
            try:
                face_total_url = 'http://www.zhaogexing.com/nvtouxiang/meinv/list_' + str(page) + '.html'
                face_total_text = requests.get(face_total_url).text
                soup = BeautifulSoup(face_total_text, 'html.parser')
                face_page = soup.find_all('a', attrs={'class': 'litpic'})
                for face in face_page:
                    output_face_profile.append(face.get('href'))
            except:
                continue
        return output_face_profile

    def get_img_url(self):
        output_picture = []
        for face_page_url in tqdm(self.category_url):
            try:
                face_page_text = requests.get(face_page_url).text
                soup = BeautifulSoup(face_page_text, 'html.parser')
                imgs = soup.find_all('img')
                for img in imgs:
                    output_picture.append(img.get('src'))
            except:
                continue
        return output_picture