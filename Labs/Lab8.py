import bs4 as bs
import urllib.request
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

nav = soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))

for div in soup.find_all('div', class_='body'):
    print(div.text)