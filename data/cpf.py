import requests,os,time
from data import ui
def consultar(lang):
    Sair = False
    while(Sair==False):
        os.system("clear")
        cpf_input = ui.input_dialog()
        data = requests.get('http://api.trackear.com.br/basepv/cpf/{}/noip'.format(cpf_input)).json()
        try:
        	msg = f"""
{lang[14]}: {data['cpf']}
{lang[18]}: {data['nome']}
{lang[19]}: {data['sexo']}
{lang[20]}: {data['dtNascimento']}
{lang[21]}: {data['idade']}
{lang[22]}: {data['dtConsulta']}
            """
        except:
            msg = lang[12]
        	
        choice = ui.dialog_choice(msg)
        if choice == '1' or choice == '01':
            pass
        elif choice == '2' or choice == '02':
            Sair=True
        else:
            ui.dialog(lang[3]);time.sleep(3)