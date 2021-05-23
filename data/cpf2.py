import requests,time
from data import ui
# 00000000272
def consultar(lang):
    cpf_input = ui.input_dialog()
    api = requests.get('http://192.53.165.231/cCPF/{}'.format(cpf_input)).json()
    msg = f'''
{lang[18]}: {api['nome']}
{lang[14]} : {api['cpf']}
{lang[40]} : {api['cns']}
{lang[19]}: {api['sexo']}
{lang[29]}: {api['enderecoLogradouro']}, {api['enderecoNumero']}
{lang[30]}: {api['enderecoComplemento']}
{lang[17]} : {api['enderecoCep']}
{lang[49]} : {api['enderecoBairro']}
{lang[18]} {lang[41]}: {api['nomeMae']}
{lang[18]} {lang[42]}: {api['nomePai']}
{lang[43]} : {api['nacionalidade']}
{lang[44]} : {api['encontradoReceita']}
{lang[47]} : {api['nomade']}
{lang[48]} : {api['tipoSanguineo']}
    '''
    mensage = ''
    for i in range(0,10):
        try:
            mensage=f'''
{lang[25]}: ({api['telefone'][i]['ddd']}){api['telefone'][i]['numero']}
{lang[34]}: {api['telefone'][i]['tipoDescricao']}
        '''
        except:
            i=10
        mensage = msg+mensage 
    msg = msg.replace('true',lang[45]).replace('false',lang[46])
    choice = ui.dialog_choice(msg)
    if choice == '1' or choice == '01':
        pass
    elif choice == '2' or choice == '02':
        Sair=True
    else:
        ui.dialog(lang[3])
        time.sleep(3)
