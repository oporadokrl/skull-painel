import requests
from data import ui
def consultar(lang):
    bank_input = ui.input_dialog()
    try:
        bank_data = requests.get('https://brasilapi.com.br/api/banks/v1/{}'.format(bank_input)).json()
        if 'message' not in bank_data:
            msg= f'''
{lang[82]}: {bank_data['code']}
{lang[18]}: {bank_data['name']}
{lang[83]}: {bank_data['fullName']}
ISPB: {bank_data['ispb']}
            '''
        else:
            msg = lang[12]
    except:
         msg = lang[12]
    choice = ui.dialog_choice(msg)
    if choice == '1' or choice == '01':
        pass
    elif choice == '2' or choice == '02':
        Sair=True
    else:
        ui.dialog(lang[3]);time.sleep(3)