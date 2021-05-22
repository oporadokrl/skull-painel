import requests
def consultar(crm_input,uf_input):
    token = 5072097263
    try:
        url = 'https://www.consultacrm.com.br/api/index.php?tipo=crm&uf='+uf_input
        data = requests.get(url+'&q={}&chave={}&destino=json'.format(crm_input,token))
        crm_data = data.json()
    except:
        return 'CRM ou UF invalido'
        limite = int(crm_data['api_limite'])
        consultas= int(crm_data['api_consultas'])
        restantes = int(limite - consultas) 
    if (crm_data['status']) == "true":
        try:
            msg = f'''
            CRM: {crm_data["item"][0]["numero"]}
            Nome: {crm_data["item"][0]["nome"]}
            UF: {crm_data["item"][0]["uf"]}
            Situacao: {crm_data["item"][0]["situacao"]}
            Profiss?o: {crm_data["item"][0]["profissao"]}
            Consultas restantes = {restantes}
            '''
            return msg
        except:
            return 'Erro! dados invalidos!'
    else:
        return 'CRM invalido'