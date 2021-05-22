import os
global optionsfile,userfile,login,user,cpf_api,ip_api,placa_api,cnpj_api,language
# Retornar uma lista nomeada de options
# remover o arquivo user e colocar na options o username
optionsfile = './data/save/options'
def clear_config():
    if os.path.exists(optionsfile):
        try:
            os.remove(optionsfile)
        except:
            os.system('rm '+optionsfile)

def write(language='pt',options='000000',user='yato'):
    clear_config()
    f = open(optionsfile,'a')
    f.write(language);f.write(',');f.write(options);f.write(',');f.write(user)
    f.close()

def read():
    if os.path.exists(optionsfile):
        f = open(optionsfile,'r')
        options = (f.read()).split(',')
        f.close()
    else:
        options = [
            'pt',
            '000000',
            'yato'
        ]
    return options