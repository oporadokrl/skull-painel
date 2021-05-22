import requests
from data import ui
def consultar(lang):
    bin_input = ui.input_dialog()
    headers = {"Accept-Version": "3",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    req_data = requests.get('https://lookup.binlist.net/' + bin_input, headers=headers).json()
    try:
        msg=f'''
{lang[83]}: {req_data['scheme']}
{lang[56]}: {req_data['brand']}
{lang[34]}: {req_data['type']}
{lang[70]}: {req_data['country']['name']}
Latitude: {req_data['country']['latitude']}
Longitude: {req_data['country']['longitude']}
{lang[76]}: {req_data['country']['currency']}
        '''
        #Emoji: {req_data['country']['emoji']}  
    except:
        msg = lang[12]
            
    choice = ui.dialog_choice(msg)
    if choice == '1' or choice == '01':
        pass
    elif choice == '2' or choice == '02':
        Sair=True
    else:
        ui.dialog(lang[3]);time.sleep(3)
