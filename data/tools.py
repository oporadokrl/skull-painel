import os,socket,random,time
from data import ui
# Verificar a tradução do bruteforce
def bruteforce(lang):
	Sair = False
	while(Sair==False):
		wordlist = ['true','false']
		if os.path.exists('wordlist.txt'):
			file = open('wordlist.txt','r')
			wordlist = file.read().split()
			file.close()
		comando=str(ui.input_dialog('Digite o comando do brute force substituindo o lugar onde vai a senha por "::"')).split('::');expect_result=ui.input_dialog('Digite o que esperar na saida em caso de sucesso')
		if len(comando) < 2:
			... #Error,sem uso do ::
		encontrado = False
		while(encontrado == False):
			tentativa = tentativa + 1 
			password = wordlist[tentativa]
			result = os.popen(comando[0]+password+comando[1]).read()
			if str(expect_result) in str(result):
				encontrado = True
				msg = 'Sucesso!'
			else:
				msg = 'Falhou!'
			print('['+tentativa+']'+'Tentando senha:'+password+'Resultado:'+msg)
		Sair=True
def dos(lang):
	ip = ui.input_dialog()
	port = ui.input_dialog()
	sent = 0
	while True:
		socket.send(bytes, (ip,port))
		sent = sent + 1
		print ("Enviado {} pacotes para {} pela porta:{}".format(sent,ip,port))
		if port == 65534:
			port = 1
def nmap(lang):
	Sair = False
	while(Sair==False):
		ip = ui.input_dialog()
		retorno = os.popen(f'nmap {ip}').read()
		#print(retorno)
		choice = ui.dialog_choice(retorno)
		if choice == '1' or choice == '01':
			pass
		elif choice == '2' or choice == '02':
			Sair=True
		else:
			ui.dialog(lang[3]);time.sleep(3)
def wordlist(lang):
	Sair = False
	while(Sair == False):
		ui.dialog('under construction');time.sleep(3)
		Sair=True