import requests,time
from data import ui
def consultar(lang):
    cep_input = ui.input_dialog()
    if len(cep_input) != 8:
        msg = lang[61]
    else:
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
        adress_data = request.json()
        try:
            msg=f'''
    {lang[17]}: {adress_data['cep']}
    {lang[29]}: {adress_data['logradouro']}
    {lang[30]}: {adress_data['complemento']}
    {lang[49]}: {adress_data['bairro']}
    {lang[68]}: {adress_data["localidade"]}
    {lang[69]}: {adress_data['uf']}
    IBGE: {adress_data['ibge']}
    GIA: {adress_data['gia']}
    SIAFI: {adress_data['siafi']}
    DDD: {adress_data['ddd']}
            '''
        except:
            msg = lang[12]
    choice = ui.dialog_choice(msg)
    if choice == '1' or choice == '01':
        pass
    elif choice == '2' or choice == '02':
        Sair=True
    ui.dialog(lang[3])
    time.sleep(3)