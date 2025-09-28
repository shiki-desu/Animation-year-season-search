from bs4 import BeautifulSoup
import requests

header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

def get_Anime_list(year,season):
    url = f'https://yuc.wiki/{year}{season}/'
    response = requests.get(url,headers=header)
    if response.status_code == 200 :
        soup = BeautifulSoup(response.text, 'lxml')
    title_main_r = soup.find_all('td',class_='title_main_r')
    type_tag_r = soup.find_all('td',class_='type_tag_r')
    print(f'{year}{season}的新番有：')
    print('--------')
    for title,tag in zip(title_main_r,type_tag_r):
        chinese_title = title.find('p',class_='title_cn_r')
        japanese_title = title.find('p',class_='title_jp_r')
        if chinese_title:
            print('中文标题：',chinese_title.get_text())
        if japanese_title:
            print('日文标题：',japanese_title.get_text())
        print('番剧类型：',tag.get_text())
        print("---")
if __name__ == '__main__':
    while True:
        print('在任何时候输入\'退出\'来退出程序')
        year=input('请输入年份(例如2025):')
        if year == '退出':
            break
        season=input('请输入季节(例如01，04，07等等):')
        if season == '退出':
            break
        get_Anime_list(year,season)