import urllib
url = r"http://img.alicdn.com/bao/uploadedi3/65944481/TB2nejXpXXXXXa2XpXXXXXXXXXX_!!65944481.jpg_290x290xz.jpg"
path = r"my.jpg"
data = urllib.urlretrieve(url,path) 
