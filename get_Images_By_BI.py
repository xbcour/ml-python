import urllib.request

import requests

x = 0


def get_images(url):
    headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}
    # timeout(5, 5):请求超时等待时间， 响应超时等待时间
    res = requests.get(url, headers=headers, timeout=(5, 5))
    for images in res.json()['data']['list']['vlist']:
        # global 定义变量为全局参数
        global x
        # 将URL对应的资源保存到给定的路径上
        urllib.request.urlretrieve(images['pic'], 'image\\%s.jpg' % x)
        print('Downloading image No.{}'.format(x))
        x += 1


url = 'https://api.bilibili.com/x/space/arc/search?mid=51606885&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
get_images(url)
