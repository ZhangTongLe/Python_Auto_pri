from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id15
import os

htmlpath = "F:\Python自动化办公训练营\Day3\爬虫基础\example.html"

print(htmlpath)

with open(htmlpath, 'r',encoding='utf-8') as f:
    htmlstr =f.read()


soup = BeautifulSoup(htmlstr, 'html.parser') #加载我们的html文件

soup.find('div') # 找到 div 标签
li =soup.find_all('li') # 找到所有 li 标签



for i in li:
    print(i.text)    #获取每个 li 标签的内容



# print(soup.prettify())  # 按照源文档的格式进行输出


# BeautifulSoup API 学习
# 1、获取标题
print(soup.title)

# 2、获取标题名字
print(soup.title.text)

# 3、获取title的父节点
print(soup.title.parent.name)

# 4、获取网页的p标签
print(soup.p)


# 5、按照 p标签的类型来进行获取
print(soup.p['class'])

#6、获取html中存在的标签
# 通过点取属性的方式只能获得当前名字的第一个tag:
print(soup.a)  # 只取出第一个标签。

print(soup.find_all('a')) # 以列表形式取出所有a标签、
# 7、查找内容
print(soup.find(text="今天天气很好"))
print(soup.find(id="bd"))

# 8、遍历html中的所有a标签

for link in soup.find_all('a'):
    print(link.get('href'))

# 9、从文档中获取所有文字内容:
print('---------文本内容-------')
print(soup.get_text())

# 10、获取head
print('我是head',soup.head)
print('我是head-contents',soup.head.contents)
print('我是head-contents[1]',soup.head.contents[1])

# 11、获取节点下的节点
print('节点下的节点-', soup.a.p)
# 12、通过tag的 .children 生成器,可以对tag的子节点进行循环:
for child in soup.head.children:
    print('我是head下节点的遍历',child)
for child in soup.a.descendants:
    print("我是a标签的迭代",child)

# 13、如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:
print('打印子节点字符串',soup.title.string)


# u'The Dormouse's story'



# 14、循环获取标签里面多个字符串
#
# for string in soup.strings:
#     print('循环用string取出tag下多个字符串',repr(string))

# 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:
# 全部是空格的行会被忽略掉,段首和段末的空白会被删除

for string in soup.stripped_strings:
    print('循环用string取出tag下多个字符串',repr(string))



# 15、操作父节点

print('父节点',soup.title.parent)

# 文档title的字符串也有父节点:<title>标签

print('父节点的字符串',soup.title.string.parent)

link = soup.a

for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)


# 16、操作兄弟节点

print('操作兄弟节点1',soup.p.next_sibling)
print('操作兄弟节点2',soup.p.previous_sibling)

# 17、过滤器

# 如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.
# 下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到:


import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
    print(tag.string)


print(soup.find_all(["a", "b"]))



# 返回所有标签

for tag in soup.find_all(True):
    print('打印所有标签',tag.name)

#过滤函数 下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


# 将这个方法作为参数传入 find_all() 方法,将得到所有<p>标签:
# soup.find_all(has_class_but_no_id)



from bs4 import NavigableString
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print (tag.name)



'''
# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件.这里有几个例子:

soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
soup.find(text=re.compile("sisters"))
# u'Once upon a time there were three little sisters; and their names were\n'



下面的例子在文档树中查找所有包含 id 属性的tag,无论 id 的值是什么:


soup.find_all(id=True)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


使用多个指定名字的参数可以同时过滤tag的多个属性:

soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]


有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(data-foo="value")
# SyntaxError: keyword can't be an expression


但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:

data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]


find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.

文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量:


soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]


调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,
如果只想搜索tag的直接子节点,可以使用参数 recursive=False .

soup.html.find_all("title", recursive=False)


 BeautifulSoup 对象和 tag 对象可以被当作一个方法来使用,
 这个方法的执行结果与调用这个对象的 find_all() 方法相同,下面两行代码是等价的:



# find( name , attrs , recursive , text , **kwargs )
find_parents( name , attrs , recursive , text , **kwargs )

find_parent( name , attrs , recursive , text , **kwargs )



find_next_siblings( name , attrs , recursive , text , **kwargs )

find_next_sibling( name , attrs , recursive , text , **kwargs )

这2个方法通过 .next_siblings 属性对当tag的所有后面解析 [5] 的兄弟tag节点进行迭代, find_next_siblings() 方法返回所有符合条件的后面的兄弟节点, 
find_next_sibling() 只返回符合条件的后面的第一个tag节点.


'''

# Pyqt5 \TKINTER