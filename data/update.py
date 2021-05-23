import os,subprocess,time
from data import ui
def upgrade():
    ui.clear();ui.dialog('Checando por atualizacoes...')
    update = subprocess.check_output('git pull', shell=True)
    if 'Already up to date' not in update.decode():
        ui.dialog('Atualizacao instalada!\nReiniciando o painel...');ui.clear();ui.restart()
    else:
        ui.dialog('Nenhuma atualizacao disponivel.')
        time.sleep(2)
def old_upgrade():
	url="https://github.com/oporadokrl/skull-painel.git"
	os.popen('git clone '+url).read()
	os.popen('mv ./skull-painel/* ./ ')
	os.popen('rm -rf skull-painel')