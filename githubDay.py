import requests
from bs4 import BeautifulSoup
url = 'https://github.com/trending?since=daily&spoken_language_code=zh'
message_notion_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/ed6bf4cb-8402-4e40-915b-e2c6fd6a498f'
resp = requests.get(url=url)
if(resp.status_code != 200):
    print('shibai')
html = resp.text
bs = BeautifulSoup(html, 'html.parser')
articles = bs.find_all('article', class_='Box-row')
github_trend_list = []
for article in articles:
    title = article.find('p')
    programmingLanguage = article.find('span', itemprop='programmingLanguage')
    title_name = ''
    link = '';
    if title:
      title_name = title.get_text().strip()
      print(title_name)
    else:
       title_name = 'has no tile'
       print('has no tile')
    if programmingLanguage:
       language = programmingLanguage.get_text()
       print(language)
    else:
       language = 'has no Language'
       print(language)
    h1 = article.find('h2', class_='h3 lh-condensed')
    link_a = h1.find('a')
    print(link_a)
    item = {
       'title':title_name,
       'language': language,
       'link':'https://github.com/' + link_a['href']
    }
    github_trend_list.append(item)
    print('#'*50)
data = {
   'msg_type':'text',
   'content': {
      'text': str(github_trend_list)
   }
}
for trend in github_trend_list:
    data = {
   'msg_type':'text',
   'content': {
      'text': str(trend)
   }
}
    resp = requests.post(message_notion_url, json=data)
    print(resp.text)

