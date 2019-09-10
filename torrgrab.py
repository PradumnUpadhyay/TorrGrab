import urllib.request,urllib.parse
from bs4 import BeautifulSoup

pblnk="https://indiaboat.art"
term=input("Enter What to search: ")
print('\n\nPlease Wait Searching Data...')
term=urllib.parse.quote_plus(term.strip())
site=pblnk+"/s/?q="+term+"&page=&orderby="
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
except:
    print('Error')
soup=BeautifulSoup(page.read(),features="html.parser")
k=soup.findAll('a')
print("\n\nFetching Data...\n\n")
i=0
nm=[]
link=[]
mlink=[]
for lnk in k:
	lnk=str(lnk)
	if lnk.find('class="detLink"')!=-1:
		i+=1
		nm.append(lnk[lnk.find('>')+1:lnk.find('</a')])
		print('['+str(i)+'] '+nm[i-1])
		tlnk=lnk.find("href=")+6
		tlnk=lnk[tlnk:lnk.find('"',tlnk)]
		link.append(pblnk+tlnk)
		site=link[i-1]
		req = urllib.request.Request(site, headers=hdr)
		try:
		    page = urllib.request.urlopen(req)
		except:
		    pass
		soup=BeautifulSoup(page.read(),features="html.parser")
		kt=soup.findAll('a')
		for tlnk in kt:
			tlnk=str(tlnk)
			if 'magnet:?' in tlnk:
				ps=tlnk.find("magnet:?")
				tlnk=tlnk[ps:tlnk.find('"',ps)]
				mlink.append(tlnk)
				print(tlnk)
				print('')
				break
inp=input("Enter Link Number: ")

name=nm[inp-1]
magnet=mlink[inp-1]

