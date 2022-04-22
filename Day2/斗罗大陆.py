import  requests
from bs4 import BeautifulSoup
import time

# 小说的主页面地址
home = 'https://www.biquwx.la/10_10218/'

# 获取一个页内容
def one_page(url):

    # 把代码包装成浏览器
    headers = {
        # 用户标识
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    r  =requests.get(url,headers=headers,stream=True)
    # 编码统一成utf-8
    r.encoding = 'utf-8'

    soup = BeautifulSoup(r.text,'html.parser')
    # 标题
    title = soup.find('div',class_='bookname').find('h1').text

    content =soup.find('div',id='content') # 小说文字内容
    content = str(content)

    # 内容过滤
    content = content.replace('<div id="content"><!--go-->','')
    content = content.replace('<br>','\n')
    content = content.replace('<br/>','\n')
    content = content.replace('<!--over-->','')
    content = content.replace('</div>','')

    # 把内容都分开存到单独的txt文件中
    # with open(title+'.txt','a+', encoding='utf-8') as f:
    #     f.write(content)

    print(title +'爬取完成~')
    return content,title


for i in range(5001501,5001505):  # 结局：5002115
    url =home+str(i)+'.html'  # https://www.biquwx.la/10_10218/5001501.html
    time.sleep(1.5)
    content,title =  one_page(url)
    # 把内容都放到一个txt文件中
    with open('斗罗大陆.txt','a+', encoding='utf-8') as f:
        f.write('\r'+title+'\r'+content)