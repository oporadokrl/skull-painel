import os
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m'
def breach_pass():
	wordlist = 'word.txt'
	file=''
	print(f'{C}[{G}*{C}] Tentando ler wordlist.')
	file = open(wordlist,'r')
	passwords = (file.read()).split()
	file.close()
	for word in passwords:
		print(f'{C}[{G}*{C}] Tentando senha: '+word)
		os.popen('unzip -p '+word+' '+file)
		os.system('clear')