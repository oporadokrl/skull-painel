global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m'
error=f'{C}[{R}ERROR{C}]'
warning=f'{C}[{Y}!{C}]'
info=f'{C}[{G}i{C}]'
import os,sys
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
	clear()
	print(f'''{C}
{G}   <==================Feito por YATO=====================>{R}
    .o oOOOOo                                         OOOo
    Ob.OOOOOo  OOOo.      oOo.                    .adOOOOO
    OboO"""""""""".OOo. .oOOo.    OOOo.oOOOo..""""""""'OO
    OOP.oOOOOOOOOO "POOOOOOOo.   `"OOOOOOOP,OOOOOOOOOOOB'
    `O'OO'     `OOOOo"OOOOOO` .adOOOOOOO"oOOO'   `OOOOo
    .OO'            `OOOOOOOOOOOOOOOOOOOO'        `OO
    OOO               '"OOOOOOOOOOOO"`             oOO
   oOOOba.             .adOOOOOOOOOa              .adOOOOo.
  oOOOOOOOOOOOba.    .adOOOOOO@^OOOOba.     .adOOOOOOOOOO
 OOOOOOOOOOOOOOO.OOOOOOOOOOO"`  '"OOOOOOOOOO.OOOOOOOOOOOO
 "OOOO"      "YOoOMOIONODOO"`  .   '"OROAOEOOOoOY"    "OOO"
    Y          'OOOOOOOOOO: .oOOo. :OOOOOOOO?'         :`
    :           .oO%OOOOOOo.OOOOOO.oOOOOOOOOO?         .
    .           oOOP"%OOOOOoOOOOO?oOOO?OOOO"OOo
               'o  OOOO"%OOO%"%OOOOO"OOOOO"OOO':
                    `$"  `OO' `O"Y ' `OOOO'  o         .
    .                .    OP"          : o   .
                          :
                          .{C}''')

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def dialog(text='',tiled='='):
  clear()
  banner()
  file = open('./data/save/options','r')
  lang = (file.read()).split(',')[0]
  file.close()
  file = open('./data/lang/'+lang,'r')
  lang=(file.read()).split('-')
  file.close()
  #messg = lang[choice_text]
  text = text.split('\n')
  maior = 0
  for txt in text:
    tamanho = len(txt)
    if tamanho > maior:
      maior = tamanho
  print(str(C)+str(G)+tiled+tiled+tiled*maior+tiled+tiled+str(C));
  for txt in text:
    print(str(warning)+' '+txt);
  print(str(C)+str(G)+tiled+tiled+tiled*maior+tiled+tiled+str(C))

def menu(text,choice_text=0,tiled='='):
  file = open('./data/save/options','r')
  lang = (file.read()).split(',')[0]
  file.close()
  file = open('./data/lang/'+lang,'r')
  lang=(file.read()).split('-')
  file.close()
  messg = lang[choice_text]
  clear()
  banner()
  text = text.split('\n')
  maior = 0
  for txt in text:
    tamanho = len(txt)
    if tamanho > maior:
      maior = tamanho
  print(tiled+tiled+tiled*maior+tiled+tiled);
  number = 0
  for txt in text:
    number = number + 1
    print(str(C)+'['+str(G)+str(number)+str(C)+'] '+txt);
  print(tiled+tiled+tiled*maior+tiled+tiled)
  print(info+' '+messg)
  return input('===>')

def dialog_choice(text='',choice_text=1,tiled='='):
  file = open('./data/save/options','r')
  lang = (file.read()).split(',')[0]
  file.close()
  file = open('./data/lang/'+lang,'r')
  lang=(file.read()).split('-')
  file.close()
  messg = lang[choice_text]

  clear()
  banner()
  text = text.split('\n')
  maior = 0
  for txt in text:
    tamanho = len(txt)
    if tamanho > maior:
      maior = tamanho
  if maior > 2:
    print(tiled+tiled*maior+tiled+tiled);
    for txt in text:
      print(txt);
    print(tiled+tiled*maior+tiled+tiled)
  print(info+' '+messg)
  print(str(C)+'['+str(G)+str(1)+str(C)+']'+' '+lang[5])
  print(str(C)+'['+str(G)+str(2)+str(C)+']'+' '+lang[6])
  return input('===>')

def input_dialog(text='',choice_text=13,tiled='='):
  file = open('./data/save/options','r')
  lang = (file.read()).split(',')[0]
  file.close()
  file = open('./data/lang/'+lang,'r')
  lang=(file.read()).split('-')
  file.close()

  clear()
  banner()
  text = text.split('\n')
  maior = 0
  for txt in text:
    tamanho = len(txt)
    if tamanho > maior:
      maior = tamanho
  if maior > 2:
    messg = text[0]
  else:
    messg = lang[choice_text]
  print(info+' '+messg)
  return input('===>')