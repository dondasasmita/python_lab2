# import the requests Python library for programmatically making HTTP requests
# after installing it according to these instructions:
# http://docs.python-requests.org/en/latest/user/install/#install
import requests

# import the BeautifulSoup Python library according to these instructions:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
# use this syntax as described on the documentation page:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup
from bs4 import BeautifulSoup

site = requests.get('https://news.detik.com/berita/d-4011709/menaker-bentuk-satgas-pengawasan-untuk-cegah-tka-ilegal?_ga=2.104324544.1790807633.1525794648-657603881.1525148050').text
page = BeautifulSoup(site, 'html.parser')

filename = input('Save file as : ')

with open(filename + '.txt', 'w') as open_file:
    for lines in page.find_all('p'):
        open_file.write(lines)
