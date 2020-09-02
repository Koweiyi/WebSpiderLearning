from urllib.parse import urlparse

url = 'http://www.baidu.com/index.html;user?id=5#comment'

result = urlparse(url)
print(type(result))
print(result)

# 指定协议，假如
result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(type(result))
print(result)

# 是否允许fragment,指定False将不再解析fragment
result = urlparse(url, allow_fragments=False)
print(result)





