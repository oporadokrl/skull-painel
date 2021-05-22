import requests
from data import ui
def consultar(lang):
    ip_input = ui.input_dialog()
    try:
        api=requests.get('http://ipwhois.app/json/'+ip_input).json()
        lat = api['latitude'];lon = api['longitude']
        #api2 = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=25d800a8b8e8b99d77c809567aa291b8').json()
    except:
        msg = lang[12]
    try:
        msg=f'''
IP: {api['ip']}
{lang[34]}: {api['type']}
{lang[69]}: {api['continent']}
{lang[70]}: {api['country']}
{lang[71]}: {api['country_capital']}
{lang[72]}: {api['country_phone']}
{lang[73]}: {api['country_neighbours']}
{lang[67]}: {api['region']}
{lang[66]}: {api['city']}
LATITUDE: {api['latitude']}
LONGITUDE: {api['longitude']}
ASN: {api['asn']}
ORG: {api['org']}
ISP: {api['isp']}
{lang[75]}: {api['timezone']}
{lang[75]}: {api['timezone_name']}
GMT: {api['timezone_gmt']}
{lang[76]}: {api['currency']}
{lang[76]}: {api['currency_code']}
{lang[79]} {lang[78]} {lang[76]}: {api['currency_symbol']}
        '''
    except:
        msg = lang[12]
        #{lang[81]}: {api2["weather"][0]["main"]}
    choice = ui.dialog_choice(msg)
    if choice == '1' or choice == '01':
        pass
    elif choice == '2' or choice == '02':
        Sair=True
    else:
        ui.dialog(lang[3]);time.sleep(3)