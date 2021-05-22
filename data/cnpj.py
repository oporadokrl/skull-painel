import requests,time
from data import ui
def consultar(lang,cnpj_input=''):
    if len(cnpj_input) < 1:
        cnpj_input = ui.input_dialog()
    msg=''
    try:
        cnpj_data = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input)).json()
    except:
        msg = lang[12]
    if cnpj_data['status'] != "ERROR":
        msg=f"""
{lang[15]}: {cnpj_data['cnpj']}
        """
        message=f"""
{lang[23]}: {cnpj_data['atividade_principal'][0]['text']}
{lang[18]}: {cnpj_data['nome']}
{lang[17]}: {cnpj_data['cep']}
        """
        msg = msg + message
        try:
            message=f"{lang[25]}: {cnpj_data['telefone']}"
            msg = msg + message
        except:
            pass
        try:
            message=f"\nEmail: {cnpj_data['email']}"
            msg = msg + message
        except:
            pass
        message=f"""
{lang[26]}: {cnpj_data['situacao']}
{lang[27]}: {cnpj_data['uf']}
{lang[28]}: {cnpj_data['municipio']}
{lang[29]}: {cnpj_data['logradouro']}, {cnpj_data['numero']}
{lang[30]}: {cnpj_data['complemento']}
{lang[31]}: {cnpj_data['porte']}
{lang[32]}: {cnpj_data['natureza_juridica']}
{lang[33]}: {cnpj_data['abertura']}
{lang[34]}: {cnpj_data['tipo']}
{lang[35]}: {cnpj_data['capital_social']}
        """
        msg = msg + message
        for i in range(0,10):
            try:
                message=f"""
{lang[36]}: {cnpj_data['qsa'][i]['nome']}
{lang[37]}: {cnpj_data['qsa'][i]['qual']}
                """
                msg = msg + message
            except:
                pass
    else:
        msg=cnpj_data['message']
    choice = ui.dialog_choice(msg)
    if choice == '1' or choice == '01':
        pass
    elif choice == '2' or choice == '02':
        Sair=True
    else:
        ui.dialog(lang[3])
        time.sleep(3)
def gerar(lang):
    token="f01e0024a26baef3cc53a2ac208dd141"
    cnpj_data=requests.get('http://geradorapp.com/api/v1/cnpj/generate?token={}'.format(token)).json()
    cnpj_input = int(cnpj_data['data']['number'])
    consultar(lang,cnpj_input)