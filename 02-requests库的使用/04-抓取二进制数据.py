import requests

resp = requests.get('https://pic4.zhimg.com/v2-c5dfb79437f7e32e8d31e246d18be381_400x224.jpg?source=172ae18b')

filename = 'zhihu.png'
with open(filename, 'wb') as f:
    f.write(resp.content)
