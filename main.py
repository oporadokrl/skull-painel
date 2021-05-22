# Feito por Yato
import os,time
try:
	from data import data,ui,cpf,cnpj,cpf2,tools,placa,cep,covid,ip
except:
	choice = ui.dialog_choice('',2)
	if choice == '01' or choice == '1':
		os.system('pip3 install requests')
	elif choice == '02' or choice == '2':
		ui.dialog('Então instale por si ou isto é um adeus.\nSo install it by yourself or this is a goodbye.')
	exit()
def reload():
	global lang,login,cpf_api,ip_api,placa_api,cnpj_api,anim
	options = data.read()
	lang = options[0];user = options[2]
	options = options[1]
	login = options[0];cpf_api=options[1];ip_api=options[2];placa_api=options[3];cnpj_api=options[4];anim=options[5]

	file = open('./data/lang/'+lang,'r')
	lang=(file.read()).split('-')
	file.close()

def opt():
	def set_lang():
		choice = ui.menu('English\nPortuguês\n'+lang[4])
		if choice == '01' or choice == '1':
			data.write('en')
		elif choice == '02' or choice == '2':
			data.write('pt')
		elif choice == '03' or choice == '3':
			pass
		else:
			ui.dialog(lang[3])
			time.sleep(3)
	choice = ui.menu(lang[11]+'\n'+lang[39])
	if choice == '1' or choice == '01':
		set_lang()
	elif choice == '2' or choice == '02':
		pass
	else:
		ui.dialog(lang[3])
		time.sleep(3)

reload()
Sair=False
while(Sair == False):
	choice = ui.menu(lang[8]+lang[14]+'\n'+lang[8]+lang[15]+'\n'+lang[8]+lang[16]+'\n'+lang[8]+lang[17]+'\n'+lang[8]+'Covid-19'+'\n'+lang[8]+'IP'+'\n'+lang[8]+lang[81]+'\n'+lang[50]+'\n'+lang[10]+'\n'+lang[4])
	if choice == '1' or choice == '01':
		choice2 = ui.menu(lang[14]+' 1'+'\n'+lang[14]+' 2'+'\n'+lang[39])
		if choice2 == '1' or choice2 =='01':
			cpf.consultar(lang)
		elif choice2 == '2' or choice2 == '02':
			cpf2.consultar(lang)
		elif choice2 == '3' or choice2 == '03':
			pass
		else:
			ui.dialog(lang[3])
			time.sleep(3);del choice2
	elif choice == '2' or choice == '02':
		cnpj.consultar(lang)
	elif choice == '3' or choice == '03':
		placa.consultar(lang)
	elif choice == '4' or choice == '04':
		cep.consultar(lang)
	elif choice == '5' or choice == '05':
		covid.consultar(lang)
	elif choice == '6' or choice == '06':
		ip.consultar(lang)
	elif choice == '7' or choice == '07':
		choice = ui.menu(lang[8]+'BIN\n'+lang[8]+lang[81]+'\n'+lang[39])
		if choice == '1' or choice == '01':
			tools.dos()
		elif choice == '2' or choice == '02':
			tools.bruteforce()
	elif choice == '8' or choice == '08':
		choice = ui.menu('DoS\nBrute force\nWordlist\nNMAP\n'+lang[39])
		if choice == '1' or choice == '01':
			tools.dos(lang)
		elif choice == '2' or choice == '02':
			tools.bruteforce(lang)
		elif choice == '3' or choice == '03':
			tools.wordlist(lang)
		elif choice == '4' or choice == '04':
			tools.nmap(lang)
		elif choice == '5' or choice == '05':
			pass
		else:
			ui.dialog(lang[3])
			time.sleep(3)
	elif choice == '9' or choice == '09':
		opt()
		reload()
	elif choice == '10':
		Sair = True
	else:
		ui.dialog(lang[3])
		time.sleep(3)
ui.clear();print(lang[9])