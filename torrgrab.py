import urllib.request,urllib.parse
import os, sys, subprocess

banner = """
  ______                ______           __
 /_  __/___  __________/ ____/________ _/ /_
  / / / __ \/ ___/ ___/ / __/ ___/ __ `/ __ \\
 / / / /_/ / /  / /  / /_/ / /  / /_/ / /_/ /
/_/  \____/_/  /_/   \____/_/   \__,_/_.___/  V.1.0

"""
print(banner)

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
name=[]
link=[]
def scrapmagnet(site,se="pirate"):
	if "pirate" in se.lower():
		req = urllib.request.Request(site, headers=hdr)
		try:
		    page = urllib.request.urlopen(req)
		except:
		    pass
		page=page.read().decode('utf-8')
		p1=page.find('<dt>Info Hash:</dt><dd></dd>')+32
		p2=page.find('</dl',p1)
		print("Hash: ",page[p1:p2].strip())
		p1=page.find('href="magnet:?')+6
		p2=page.find('" title',p1)
		mglink=page[p1:p2].strip()
		return mglink
	else:
		return site
def piratebay(term):
	global name,link
#	term=term.replace(' ','+')
	pblnk="https://indiaboat.art"
	print('\n\n[i] Please Wait Searching Data...')
	term=urllib.parse.quote_plus(term.strip())
	site=pblnk+"/s/?q="+term+"&page=&orderby="
	np=0
	#site="https://indiaboat.art/s/?q=Sacred+games&page=&orderby="
	while True:
		print("\n\n[i] Fetching Data...\n\n")
		req = urllib.request.Request(site, headers=hdr)
		try:
		    page = urllib.request.urlopen(req)
		except:
		    print('[-] Connection Error')
		page=page.read().decode('utf-8')
		det=page.split('<div class="detName">')[1:]
		name=[]
		link=[]
		seed=[]
		info=[]
		for dt in det:
			tmp=dt[dt.find('href="')+6:dt.find('" class')]
			link.append(pblnk+tmp)
			tmp=dt[dt.find('">',dt.find('detLink')+10)+2:dt.find('</a>')]
			name.append(tmp)
			tmp=dt[dt.find('detDesc">')+9:dt.find('ULed')]
			info.append(tmp)
			tmp=dt[dt.find('align="right">')+14:dt.find('</td>',dt.find('align="right">')+13)]
			seed.append(tmp)
		for i in range(len(link)):
			print(f'''[ {i+1} ] TORRENT NUMBER #{i+1} ''')
			print('\tName: ',name[i])
			#print('\tLink: ',link[i])
			print('\tSeed: ',seed[i])
			print('\tInfo: ',info[i])
			print('\n')
		cho=input('\n\n\n[!] Load More (Y/N) : ')
		if cho.lower().strip()=='y':
			np+=1
			site=pblnk+"/s/?q="+term+"&page="+str(np)+"&orderby="
		else:
			break

def torrentz(term):
	global name,link
	term=term.replace(' ','+')
	pblnk="https://torrentz2eu.in"
	print('\n\n[i] Please Wait Searching Data...')
	term=urllib.parse.quote_plus(term.strip())
	site=pblnk+"/?q="+term
	np=0
	#site="https://torrentz2eu.in/?q=sacred+games"
	req = urllib.request.Request(site, headers=hdr)
	try:
	    page = urllib.request.urlopen(req)
	except:
	    print('[-] Connection Error')
	name=[]
	link=[]
	seed=[]
	info=[]
	page=page.read().decode('utf-8')
	det=page.split('<tr>')[2:]
	for dt in det:
		p1=dt.find('Name">')+6
		tmp=dt[p1:dt.find('</td>',p1)]
		name.append(tmp)
		p1=dt.find('Seeds">')+7
		tmp=dt[p1:dt.find('</td>',p1)]
		seed.append(tmp)
		p1=dt.find('Size">')+6
		tmp=dt[p1:dt.find('</td>',p1)]
		info.append('Size: '+tmp)
		p1=dt.find('magnet',p1)+6
		tmp=dt[p1:dt.find('"',p1)]
		link.append(tmp)
	for i in range(len(link)):
		print(f'''\n\n[ {i+1} ] TORRENT NUMBER #{i+1} ''')
		print('\tName: ',name[i])
		#print('\tLink: ',link[i])
		print('\tSeed: ',seed[i])
		print('\tInfo: ',info[i])
def mag2tor(name,hash):
	base="https://itorrents.org"
	base+="/torrent/"+hash+".torrent"
	opener = urllib.request.build_opener()
	opener.addheaders= [('User-agent', 'Mozilla/5.0')]
	urllib.request.install_opener(opener)
	try:
		urllib.request.urlretrieve(base, name)
		print("\n\n\n[i] Torrent File Saved To ",name)
		return True
	except:
		print("\n\n\n[!] You Need To use A VPN To Fetch Torrent...")
		return False

if len(sys.argv)==2:
	if "u" in sys.argv[1]:
		print('\n\nUpdating TorrGrab...')
		urllib.request.urlretrieve('https://raw.githubusercontent.com/PradumnUpadhyay/TorrGrab/master/torrgrab.py', 'torrgrab.py')
print("[i] Search Engines Available: 2\n")
print('\t[1]\tPirateBay')
print('\t[2]\tTorrentz')
print('\n\n')
se=''

cho=input("Choose Engine [ 1 - 2 ]: ")

term=input("[?] Enter What to search: ")
if "1" in cho:
	se='piratebay'
	while " " in term:
		print('Spaces Are Not Allowed In Searches \n You Can use WildCards.')
		term=input("[?] Enter What to search: ")
	piratebay(term)
elif "2" in cho:
	se='torrentz'
	torrentz(term)
else:
	print('[-] Wrong Input.. \n\n[i]Using PirateBay By default')
	piratebay(term)
if len(link)==0:
	print("Sorry No Links Found...\nExiting Termux")
	exit()
try:
	inp=int(input("Enter Link Number: "))
except:
	print('Exiting TorrGrab')
	exit()
name=name[inp-1]
magnet=scrapmagnet(link[inp-1],se)
hash=magnet[magnet.find('btih:')+5:magnet.find('&')]
fn=name.replace(" ","_")+".torrent"

print("[i] Files will be Downloaded by default torrent app on your System\n\n")
print("\n\n\n[i] Title: ",name)
print("[i] Magnet Link: ",magnet)
print("[i] Info Hash: ",hash)
print('\n\n Fetching .torrent File From Magnet Link...')
res=mag2tor(fn,hash)

if not res:
	print('[i] Exiting TorrGrab..')
	exit()


cho=input('\n\n\n[i] Start Download (Y/N) : ')
if cho.lower().strip()=='y':
	if sys.platform == "win32":
	    os.startfile(fn)
	else:
		opener = "open" if sys.platform == "darwin" else "xdg-open"
		subprocess.call([opener, fn])
# 	elif platform.system() == 'Darwin':  # macOS
# 	    subprocess.call(('open', fn))
# 	elif platform.system() == 'Linux':
# 	    subprocess.call(('xdg-open', fn))
else:
	print('[i] Exiting TorrGrab..')
	exit()
