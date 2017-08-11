import os
import urllib.request
import shutil
from bs4 import BeautifulSoup

URL = '----------------Link Disabled----------------'   # 在哪找这个链接我想应该不用我提醒
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7', }


def crawl(location):
    file_name = []
    j = 0
    print('Starting...')
    for i in range(14):
        print('Opening web page No.' + str(i + 1) + '...')
        req = urllib.request.Request(URL + '/{}'.format(i + 1), None, headers)
        data = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(data, 'html5lib')
        print('Finding urls...')
        for link in soup.find_all('img'):
            u = link.get('src')
            j += 1
            file_name.append(str(j))
            req2 = urllib.request.Request(u, None, headers)
            with urllib.request.urlopen(req2) as photo, open(os.path.join(location, file_name[j - 1] + '.jpg'),
                                                             'wb') as localFile:
                shutil.copyfileobj(photo, localFile)
                photo.close()


if __name__ == '__main__':
    sav = input('Enter the File location you want to save pics in: ')
    crawl(sav)
    print('Downloading Finished!')
