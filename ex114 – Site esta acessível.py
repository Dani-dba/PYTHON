import urllib
from urllib import request
try:
    site = urllib.request.urlopen('http://www.google.com.br')
except:
    print('Não foi possivel acessar o site no momento')
else:
    print('Consegui acessar o site')
    # print(site.read())