import requests
from data import ui
def consultar(lang):
    Sair = False
    while(Sair==False):
        choice = ui.input_dialog()
        data = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}'.format(choice)).json()
        msg = f'''
Data e horario local: {data['datetime']}
Estado: {data['state']}
UF: {data['uf']}
UID: {data['uid']}
Casos: {data['cases']}
Mortes: {data['deaths']}
Suspeitas: {data['suspects']}
Recusados: {data['refuses']}
        '''
        choice = ui.dialog_choice(msg)
        if choice == '1' or choice == '01':
        	pass
        elif choice == '2' or choice == '02':
        	Sair = True
        else:
        	pass