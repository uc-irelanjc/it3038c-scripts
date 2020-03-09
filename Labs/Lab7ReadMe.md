This is how to run a Python script I wrote, that uses the plugin called BeutifulSoup. First create a Virtual ENV by typing the following in the command line:
virtualenv venv/webscraping/
venv/websraping/Scripts/activate.ps1
pip install bs4
pip install lxml

Now, find a website to webscrape;
source = urllib.request.urlopen('http://website.com')

Now the code;
print(soup.title.text)
for paragraph in soup.find_all('p'):
    print(paragraph.text)
for url in soup.find_all('a'):
    print(url.get('href'))
will show the title, all paragraph text, and all url links in the webpage.

That is the end, remember to deactivate the virtualenv.
deactivate