import requests
from data import ui
def consultar(lang):
    Sair=False
    while(Sair==False):
        placa_input = ui.input_dialog()
        placa_data = requests.get('https://apicarros.com/v1/consulta/{}/json'.format(placa_input), verify = False).json() # JSQ7436
        try:
            if (placa_data['codigoRetorno']) == "0":
                msg=f'''
{lang[51]}: {placa_data['ano']}
{lang[52]}: {placa_data['data']}
{lang[53]}:  {placa_data['modelo']}
{lang[52]} {lang[54]} {lang[53]}:  {placa_data['anoModelo']}
{lang[55]}:  {placa_data['cor']}
{lang[56]}:  {placa_data['marca']}
{lang[57]}:  {placa_data['dataAtualizacaoRouboFurto']}
{lang[58]}:  {placa_data['situacao']}
{lang[16]}:  {placa_data['placa']}
{lang[59]}:  {placa_data['chassi']}
{lang[27]}:  {placa_data['uf']}
{lang[28]}:  {placa_data['municipio']}
{lang[60]}:  {placa_data['dataAtualizacaoCaracteristicasVeiculo']}
{lang[64]}:  {placa_data['dataAtualizacaoAlarme']}
{lang[65]}:  {placa_data['mensagemRetorno']}'''
            else:
                msg = lang[61]
        except:
            msg = lang[3]
        choice = ui.dialog_choice(msg)
        if choice  == '1' or choice == '01':
            pass
        elif choice == '2' or choice == '02':
            Sair = True
        else:
            pass
