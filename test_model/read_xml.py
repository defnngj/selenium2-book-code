from xml.dom import minidom

# 打开 xml 文档
dom = minidom.parse('./config_file/info.xml')
# 得到文档元素对象
root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

###### 获得任意标签名 #####
tagname = root.getElementsByTagName('browser')
print(tagname[0].tagName)
tagname = root.getElementsByTagName('login')
print(tagname[1].tagName)
tagname = root.getElementsByTagName('province')
print(tagname[2].tagName)

###### 获得标签的属性值 #####
logins = root.getElementsByTagName('login')
# 获得 login 标签的 username 属性值
username = logins[0].getAttribute("username")
print(username)
# 获得 login 标签的 password 属性值
password = logins[0].getAttribute("password")
print(password)
# 获得第二个 login 标签的 username 属性值
username = logins[1].getAttribute("username")
print(username)
# 获得第二个 login 标签的 password 属性值
password = logins[1].getAttribute("password")
print(password)


###### 获得标签对之间的数据 #####
provinces = dom.getElementsByTagName('province')
citys = dom.getElementsByTagName('city')
# 获得第二个 province 标签对的值
p2 = provinces[1].firstChild.data
print(p2)
# 获得第一个 city 标签对的值
c1 = citys[0].firstChild.data
print(c1)
# 获得第二个 city 标签对的值
c2 = citys[1].firstChild.data
print(c2)

