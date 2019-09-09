import urllib.request,urllib.parse
from bs4 import BeautifulSoup

term=input("Enter What to search: ")
term=urllib.parse.quote_plus(term.strip())
site="https://indiaboat.art/s/?q="+term+"&page=&orderby="
#print(site)
#site="https://indiaboat.art/s/?q=Sacred+games&page=&orderby="
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib.request.Request(site, headers=hdr)

try:
    page = urllib.request.urlopen(req)
except e:
    print(e.read())
print("\n\nResult Links...\n\n")
soup=BeautifulSoup(page.read(),features="html.parser")
k=soup.findAll('a')
for lnk in k:
	lnk=str(lnk)
	if lnk.find('class="detLink"')!=-1:
		print(lnk[lnk.find('>')+1:lnk.find('</a')])
#print(content)
