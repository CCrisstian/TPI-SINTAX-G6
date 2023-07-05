import ply.lex as lex
import sys
import re
import codecs
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from termcolor import colored

contsect=0
conILIST=0
valor_href=' '
#definimos una lista con los tokens a utilizar
tokens  =   [
    'TEXTO', #Texto alfanumerico
    'NUMERO',
    'DOCTYPE',
    'OPART', #Apertura - ARTICLE (Open)
    'CLART', #Cierre - ARTICLE  (Close)
    'OPSECT', #SECTION
    'CLSECT',
    'OPSSECT', #simplesection
    'CLSSECT',
    'OPINFO', 
    'CLINFO',
    'OPABST',
    'CLABST',
    'OPADD',    
    'CLADD',
    'OPAUTHOR',
    'CLAUTHOR',
    'OPCOPY',
    'CLCOPY',
    'OPTIT',
    'CLTIT',
    'OPSPARA',
    'CLSPARA',
    'OPEMPH',
    'CLEMPH',
    'OPCOM',
    'CLCOM',   
    'OPPARA',
    'CLPARA',
    'OPFNAME',
    'CLFNAME',
    'OPSNAME',
    'CLSMANE',
    'OPSTREET',
    'CLSTREET',
    'OPCITY',
    'CLCITY',
    'OPSTATE',
    'CLSTATE',
    'OPPHONE',
    'CLPHONE',
    'OPEMAIL',
    'CLEMAIL',
    'OPDATE',
    'CLDATE',
    'OPYEAR',
    'CLYEAR',
    'OPHOLDER',
    'CLHOLDER',
    'OPMOBJ', #MEDIA OBJECT
    'CLMOBJ',
    'OPVOBJ', #VIDEO  OBJECT
    'CLVOBJ',
    'VIDAT', #VIDEO DATA
    'OPIMOBJ', #IMAGEN OBJECT
    'CLIMOBJ',
    'IMDATA', #IMAGEN DATA
    'OPILIST', #ITEMIZED LIST
    'CLILIST',
    'OPLITEM', #LIST ITEM
    'CLLITEM',
    'OPINTAB', #INFORMAL TABLE
    'CLINTAB',
    'OPTGROUP',
    'CLTGROUP',
    'OPHEAD',
    'CLHEAD',
    'OPFOOT',
    'CLFOOT',
    'OPBODY',
    'CLBODY',
    'OPROW',
    'CLROW',
    'OPENTRY',
    'CLENTRY',
    'OPLINK',
    'CLLINK',
    'OPIMPORT',
    'CLIMPORT'
]

#tokens especiales
def t_ignore_tab(t):
    r'\t'

t_ignore_blank= '\s'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Definicion de la expresion regular del tag del dockbook
def t_DOCTYPE(t):
    r'<\!DOCTYPE\s+article\s*\>'
    print(colored('Se encontro el token DOCBOOK' ,'green'))
    return t 

#Definicion de la expresion regular de Abrir articulo
def t_OPART(t):
    r'<article>'
    print(colored('Se encontro el token <article>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar articulo
def t_CLART(t):
    r'</article>'
    print(colored('Se encontro el token </article>' ,'green'))
    return t 

#Definicion de la expresion regular de Abrir section
def t_OPSECT(t):
    r'<section>'
    print(colored('Se encontro el token <section>' ,'green'))
    global contsect
    contsect+=1
    traducir('OPSECT')
    return t 

#Definicion de la expresion regular de Cerrar section
def t_CLSECT(t):
    r'</section>'
    print(colored('Se encontro el token </section>' ,'green'))
    global contsect
    contsect=0
    traducir('CLSECT')
    return t 

#Definicion de la expresion regular de Abrir simlpesection
def t_OPSSECT(t):
    r'<simplesect>'
    print(colored('Se encontro el token <simplesect>' ,'green'))
    traducir('OPSSECT')
    return t 

#Definicion de la expresion regular de Abrir simplesection
def t_CLSSECT(t):
    r'</simplesect>'
    print(colored('Se encontro el token </simplesect>' ,'green'))
    traducir('CLSSECT')
    return t 

#Definicion de la expresion regular de Abrir info
def t_OPINFO(t):
    r'<info>'
    print(colored('Se encontro el token <info>' ,'green'))
    traducir('OPINFO')
    return t 

#Definicion de la expresion regular de Cerrar info
def t_CLINFO(t):
    r'</info>'
    print(colored('Se encontro el token </info>' ,'green'))
    traducir('CLINFO')
    return t 

#Definicion de la expresion regular de Abrir abstract
def t_OPABST(t):
    r'<abstract>'
    print(colored('Se encontro el token <abstract>' ,'green'))
    traducir('OPABST')
    return t 

#Definicion de la expresion regular de Cerrar abstract
def t_CLABST(t):
    r'</abstract>'
    print(colored('Se encontro el token </abstract>' ,'green'))
    traducir('CLABST')
    return t 

#Definicion de la expresion regular de Abrir address
def t_OPADD(t):
    r'<address>'
    print(colored('Se encontro el token <address>' ,'green'))
    traducir('OPADD')
    return t 

#Definicion de la expresion regular de Cerrar address
def t_CLADD(t):
    r'</address>'
    print(colored('Se encontro el token </address>' ,'green'))
    traducir('CLADD')
    return t 

#Definicion de la expresion regular de Abrir author
def t_OPAUTHOR(t):
    r'<author>'
    print(colored('Se encontro el token <author>' ,'green'))
    traducir('OPAUTHOR')
    return t 

#Definicion de la expresion regular de Cerrar author
def t_CLAUTHOR(t):
    r'</author>'
    print(colored('Se encontro el token </author>' ,'green'))
    traducir('CLAUTHOR')
    return t 

#Definicion de la expresion regular de Abrir copyright
def t_OPCOPY(t):
    r'<copyright>'
    print(colored('Se encontro el token <copyright>' ,'green'))
    traducir('OPCOPY')
    return t 

#Definicion de la expresion regular de Cerrar copyright
def t_CLCOPY(t):
    r'</copyright>'
    print(colored('Se encontro el token </copyright>' ,'green'))
    traducir('CLCOPY')
    return t

#Definicion de la expresion regular de Abrir title
def t_OPTIT(t):
    r'<title>'
    print(colored('Se encontro el token <title>' ,'green'))
    traducir('OPTIT')
    return t 

#Definicion de la expresion regular de Cerrar title
def t_CLTIT(t):
    r'</title>'
    print(colored('Se encontro el token </title>' ,'green'))
    traducir('CLTIT')
    return t

#Definicion de la expresion regular de Abrir simpara
def t_OPSPARA(t):
    r'<simpara>'
    print(colored('Se encontro el token <simpara>' ,'green'))
    traducir('OPSPARA')
    return t 

#Definicion de la expresion regular de Cerrar simpara
def t_CLSPARA(t):
    r'</simpara>'
    print(colored('Se encontro el token </simpara>' ,'green'))
    traducir('CLSPARA')
    return t

#Definicion de la expresion regular de Abrir emphasis
def t_OPEMPH(t):
    r'<emphasis>'
    print(colored('Se encontro el token <emphasis>' ,'green'))
    traducir('OPEMPH')
    return t 

#Definicion de la expresion regular de Cerrar emphasis
def t_CLEMPH(t):
    r'</emphasis>'
    print(colored('Se encontro el token </emphasis>' ,'green'))
    traducir('CLEMPH')
    return t

#Definicion de la expresion regular de Abrir comment
def t_OPCOM(t):
    r'<comment>'
    print(colored('Se encontro el token <comment>' ,'green'))
    traducir('OPCOM')
    return t 

#Definicion de la expresion regular de Cerrar comment
def t_CLCOM(t):
    r'</comment>'
    print(colored('Se encontro el token </comment>' ,'green'))
    traducir('CLCOM')
    return t

#Definicion de la expresion regular de Abrir para
def t_OPPARA(t):
    r'<para>'
    print(colored('Se encontro el token <para>' ,'green'))
    traducir('OPPARA')
    return t 

#Definicion de la expresion regular de Cerrar para
def t_CLPARA(t):
    r'</para>'
    print(colored('Se encontro el token </para>' ,'green'))
    traducir('CLPARA')
    return t

#Definicion de la expresion regular de Abrir firstname
def t_OPFNAME(t):
    r'<firstname>'
    print(colored('Se encontro el token <firstname>' ,'green'))
    traducir('OPFNAME')
    return t 

#Definicion de la expresion regular de Cerrar firstname
def t_CLFNAME(t):
    r'</firstname>'
    print(colored('Se encontro el token </firstname>' ,'green'))
    traducir('CLFNAME')
    return t

#Definicion de la expresion regular de Abrir surname
def t_OPSNAME(t):
    r'<surname>'
    print(colored('Se encontro el token <surname>' ,'green'))
    traducir('OPSNAME')
    return t 

#Definicion de la expresion regular de Cerrar surname
def t_CLSMANE(t):
    r'</surname>'
    print(colored('Se encontro el token </surname>' ,'green'))
    traducir('CLSMANE')
    return t

#Definicion de la expresion regular de Abrir street
def t_OPSTREET(t):
    r'<street>'
    print(colored('Se encontro el token <street>' ,'green'))
    traducir('OPSTREET')
    return t 

#Definicion de la expresion regular de Cerrar street
def t_CLSTREET(t):
    r'</street>'
    print(colored('Se encontro el token </street>' ,'green'))
    traducir('CLSTREET')
    return t

#Definicion de la expresion regular de Abrir city
def t_OPCITY(t):
    r'<city>'
    print(colored('Se encontro el token <city>' ,'green'))
    traducir('OPCITY')
    return t 

#Definicion de la expresion regular de Cerrar city
def t_CLCITY(t):
    r'</city>'
    print(colored('Se encontro el token </city>' ,'green'))
    traducir('CLCITY')
    return t

#Definicion de la expresion regular de Abrir state
def t_OPSTATE(t):
    r'<state>'
    print(colored('Se encontro el token <state>' ,'green'))
    traducir('OPSTATE')
    return t 

#Definicion de la expresion regular de Cerrar state
def t_CLSTATE(t):
    r'</state>'
    print(colored('Se encontro el token </state>' ,'green'))
    traducir('CLSTATE')
    return t

#Definicion de la expresion regular de Abrir phone
def t_OPPHONE(t):
    r'<phone>'
    print(colored('Se encontro el token <phone>' ,'green'))
    traducir('OPPHONE')
    return t 

#Definicion de la expresion regular de Cerrar phone
def t_CLPHONE(t):
    r'</phone>'
    print(colored('Se encontro el token </phone>' ,'green'))
    traducir('CLPHONE')
    return t

#Definicion de la expresion regular de Abrir email
def t_OPEMAIL(t):
    r'<email>'
    print(colored('Se encontro el token <emails>' ,'green'))
    traducir('OPEMAIL')
    return t 

#Definicion de la expresion regular de Cerrar email
def t_CLEMAIL(t):
    r'</email>'
    print(colored('Se encontro el token </emails>' ,'green'))
    traducir('CLEMAIL')
    return t

#Definicion de la expresion regular de Abrir date
def t_OPDATE(t):
    r'<date>'
    print(colored('Se encontro el token <date>' ,'green'))
    traducir('OPDATE')
    return t 

#Definicion de la expresion regular de Cerrar date
def t_CLDATE(t):
    r'</date>'
    print(colored('Se encontro el token </date>' ,'green'))
    traducir('CLDATE')
    return t

#Definicion de la expresion regular de Abrir year
def t_OPYEAR(t):
    r'<year>'
    print(colored('Se encontro el token <year>' ,'green'))
    traducir('OPYEAR')
    return t 

#Definicion de la expresion regular de Cerrar year
def t_CLYEAR(t):
    r'</year>'
    print(colored('Se encontro el token </year>' ,'green'))
    traducir('CLYEAR')
    return t

#Definicion de la expresion regular de Abrir holder
def t_OPHOLDER(t):
    r'<holder>'
    print(colored('Se encontro el token <holder>' ,'green'))
    traducir('OPHOLDER')
    return t 

#Definicion de la expresion regular de Cerrar holder
def t_CLHOLDER(t):
    r'</holder>'
    print(colored('Se encontro el token </holder>' ,'green'))
    traducir('CLHOLDER')
    return t

#Definicion de la expresion regular de Abrir mediaobject
def t_OPMOBJ(t):
    r'<mediaobject>'
    print(colored('Se encontro el token <mediaobject>' ,'green'))
    traducir('OPMOBJ')
    return t 

#Definicion de la expresion regular de Cerrar mediaobject
def t_CLMOBJ(t):
    r'</mediaobject>'
    print(colored('Se encontro el token </mediaobject>' ,'green'))
    traducir('CLMOBJ')
    return t

#Definicion de la expresion regular de Abrir videoobject
def t_OPVOBJ(t):
    r'<videoobject>'
    print(colored('Se encontro el token <videoobject>' ,'green'))
    traducir('OPVOBJ')
    return t 

#Definicion de la expresion regular de Cerrar videoobject
def t_CLVOBJ(t):
    r'</videoobject>'
    print(colored('Se encontro el token </videoobject>' ,'green'))
    traducir('CLVOBJ')
    return t

def t_VIDAT(t):
    r'<(videodata)(\s+fileref=)(”|"|\')(http?|ftp?|https?|ftps?|[\w]?):(\\|[\w])+\/([\w])+.(mp4?|ogg?|webm?|avi?|mov?|MP4?|Ogg?|WebM?|AVI?|MOV?)(”|"|\')\s*\/>'
    print(colored('Se encontro el token <videodata>' ,'green'))
    global href_value
    href_value = re.search(r'"([^"]+)"', t.value, re.IGNORECASE)
    traducir('VIDATA')
    return t


#Definicion de la expresion regular de Abrir imageobject
def t_OPIMOBJ(t):
    r'<imageobject>'
    print(colored('Se encontro el token <imagenobject>' ,'green'))
    traducir('OPIMOBJ')
    return t 

#Definicion de la expresion regular de Cerrar imageobject
def t_CLIMOBJ(t):
    r'</imageobject>'
    print(colored('Se encontro el token </imagenobject>' ,'green'))
    traducir('CLIMOBJ')
    return t

def t_IMDATA(t):
    r'<(imagedata)(\s+fileref=)(”|"|\')(http?|ftp?|https?|ftps?|[\w]?):(\\|[\w])+\/([\w])+.(gif?|png?|jpeg?|svg?|GIF?|PNG?|JPEG?|SVG?)(”|"\')\s*\/>'
    print(colored('Se encontro el token <imagendata>' ,'green'))
    global href_value
    href_value = re.search(r'href="([^"]+)"', t.value, re.IGNORECASE)
    traducir('IMDATA')
    return t

#Definicion de la expresion regular de Abrir itemizedlist
def t_OPILIST(t):
    r'<itemizedlist>'
    print(colored('Se encontro el token <itemizedlist>' ,'green'))
    global conILIST
    conILIST+=1
    traducir('OPILIST')
    return t 

#Definicion de la expresion regular de Cerrar itemizedlist
def t_CLILIST(t):
    r'</itemizedlist>'
    print(colored('Se encontro el token </itemizedlist>' ,'green'))
    global conILIST
    conILIST=0
    traducir('CLILIST')
    return t

#Definicion de la expresion regular de Abrir listitem
def t_OPLITEM(t):
    r'<listitem>'
    print(colored('Se encontro el token <listitem>' ,'green'))

    return t 

#Definicion de la expresion regular de Cerrar listitem
def t_CLLITEM(t):
    r'</listitem>'
    print(colored('Se encontro el token </listitem>' ,'green'))

    return t

#Definicion de la expresion regular de Abrir informaltable
def t_OPINTAB(t):
    r'<informaltable>'
    print(colored('Se encontro el token <informaltable>' ,'green'))
    traducir('OPINTAB')
    return t 

#Definicion de la expresion regular de Cerrar informaltable
def t_CLINTAB(t):
    r'</informaltable>'
    print(colored('Se encontro el token </informaltable>' ,'green'))
    traducir('CLINTAB')
    return t

#Definicion de la expresion regular de Abrir tgroup
def t_OPTGROUP(t):
    r'<tgroup>'
    print(colored('Se encontro el token <tgroup>' ,'green'))
    traducir('OPTGROUP')
    return t 

#Definicion de la expresion regular de Cerrar tgroup
def t_CLGROUP(t):
    r'</tgroup>'
    print(colored('Se encontro el token </tgroup>' ,'green'))
    traducir('CLGROUP')
    return t

#Definicion de la expresion regular de Abrir thead
def t_OPHEAD(t):
    r'<thead>'
    print(colored('Se encontro el token <thead>' ,'green'))
    traducir('OPHEAD')
    return t 

#Definicion de la expresion regular de Cerrar thead
def t_CLHEAD(t):
    r'</thead>'
    print(colored('Se encontro el token </thead>' ,'green'))
    traducir('CLHEAD')
    return t

#Definicion de la expresion regular de Abrir tfoot
def t_OPFOOT(t):
    r'<tfoot>'
    print(colored('Se encontro el token <tfoot>' ,'green'))
    traducir('OPFOOT')
    return t 

#Definicion de la expresion regular de Cerrar tfoot
def t_CLFOOT(t):
    r'</tfoot>'
    print(colored('Se encontro el token </tfoot>' ,'green'))
    traducir('CLFOOT')
    return t

#Definicion de la expresion regular de Abrir tbody
def t_OPBODY(t):
    r'<tbody>'
    print(colored('Se encontro el token <tbody>' ,'green'))
    traducir('OPBODY')
    return t 

#Definicion de la expresion regular de Cerrar tbody
def t_CLBODY(t):
    r'</tbody>'
    print(colored('Se encontro el token </tbody>' ,'green'))
    traducir('CLBODY')
    return t

#Definicion de la expresion regular de Abrir row
def t_OPROW(t):
    r'<row>'
    print(colored('Se encontro el token <row>' ,'green'))
    traducir('OPROW')
    return t 

#Definicion de la expresion regular de Cerrar row
def t_CLROW(t):
    r'</row>'
    print(colored('Se encontro el token </row>' ,'green'))
    traducir('CLROW')
    return t

#Definicion de la expresion regular de Abrir entry
def t_OPENTRY(t):
    r'<entry>'
    print(colored('Se encontro el token <entry>' ,'green'))
    traducir('OPENTRY')
    return t 

#Definicion de la expresion regular de Cerrar entry
def t_CLENTRY(t):
    r'</entry>'
    print(colored('Se encontro el token </entry>' ,'green'))
    traducir('CLENTRY')
    return t

#Definicion de la expresion regular de link PENDIENTE
def t_OPLINK(t):
    r'<(link)(\s+xlink:href=)(http?|ftp?|https?|ftps?):\/\/([\w\-])((\.|\:)[\w\-]+)*([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?>'
    print(colored('Se encontro el token LINK' ,'green'))
    global valor_href
    href_value = re.search(r'href="([^"]+)"', t.value, re.IGNORECASE)
    if href_value:
        valor_href = href_value.group(1)
    traducir('OPLINK')
    return(t)


def t_CLLINK(t):
    r'</link>'
    print(colored('Se encontro el token </link>' ,'green'))
    traducir('CLLINK')
    return(t)

#Definicion de la expresion regular de un texto
def t_TEXTO(t):
    r'([0-9]*[\w,.;#:&?+/()_][0-9]*[\wñáéíóúÁÉÍÓÚ ,.;#:&?+/()_-]*[0-9]*)'
    if t.value.upper() in tokens:
        t.value = t.value.upper()
        t.type= t.value
    print(colored('Se encontro el token TEXTO' ,'green'))
    traducir(t.value)
    return t

#Definicion de la expresion regular de un numero
def t_NUMERO(t):
    r'[0-9][0-9]*'
    print(colored('Se encontro el token NUMERO' ,'green'))
    traducir(t.value)
    return t

def t_OPIMPORT(t):
    r'<important>'
    print(colored('Se encontro el token OPIMPORT' ,'green'))
    traducir('OPIMPORTANT')
    return t

def t_CLIMPORT(t):
    r'</important>'
    print(colored('Se encontro el token CLIMPORT' ,'green'))
    traducir('CLIMPORTANT')
    return t

def t_error(t):
    print(colored("Error lexico en la linea", "red"), str(t.lineno))
    t.lexer.skip(1)

def inicioTraduccion(nombreDireccion):
    #variable que comprobara si se termino de traducir una vez. Esto porque luego el parser realiza un segundo analisis
    global traduccionCompleta
    traduccionCompleta=False
    global tituloCanal
    tituloCanal = True
    global archivo
    archivo = open(nombreDireccion,'w')
    archivo.write('<!DOCTYPE html>\n<html lang="es">\n<head>\n<meta charset="UTF-8">\n<body>\n')

def traducir(token):
    global valor_href
    global archivo
    global contsect
    global conILIST
    token_values = {
        'OPTIT': '<h1>' if contsect==0 else '<h2>',
        'CLTIT': '</h1>' if contsect==0 else '</h2>',
        'OPINFO': '<p style="background-color: green; color:white: font-size:8px;"> INFO:',
        'CLINFO': '</p>',
        'OPPARA': '<p>'if conILIST==0 else'<l1>',
        'OPSECT': '<p>',     
        'OPSSECT': '<p>',
        'OPSPARA': '<p>'if conILIST==0 else'<l1>',
        'OPABST': '<p>'if conILIST==0 else'<l1>',
        'OPADD': '<p>'if conILIST==0 else'<l1>',
        'OPAUTHOR': '<p>',
        'OPCOPY': '<p>',
        'OPEMPH': '<p>',
        'OPCOM': '<p>'if conILIST==0 else'<l1>',
        'OPFNAME': '<p>',
        'OPSNAME': '<p>',
        'OPSTREET': '<p>',
        'OPCITY': '<p>',
        'OPSTATE': '<p>',
        'OPPHONE': '<p>',
        'OPEMAIL': '<p>',
        'OPDATE': '<p>',
        'OPYEAR': '<p>',
        'OPMOBJ': '<p>'+token+'</p>'if conILIST==0 else'<l1>'+token+'</l1>',
        'OPVOBJ': '<p>',
        'OPIMOBJ': '<p>',
        'OPHOLDER': '<p>',
        'OPTGROUP': '<p>',
        'OPHEAD': '<p>',
        'OPFOOT': '<p>',
        'OPBODY': '<p>',
        'OPROW': '<p>',
        'CLPARA': '</p>'if conILIST==0 else'</l1>',
        'CLSECT': '</p>',
        'CLSSECT': '</p>',
        'CLSPARA': '</p>'if conILIST==0 else'</l1>',
        'CLABST': '</p>'if conILIST==0 else'</l1>',
        'CLADD': '</p>'if conILIST==0 else'</l1>',
        'CLAUTHOR': '</p>',
        'CLCOPY': '</p>',
        'CLEMPH': '</p>',
        'CLCOM': '</p>'if conILIST==0 else'</l1>',
        'CLFNAME': '</p>',
        'CLSMANE': '</p>',
        'CLSTREET': '</p>',
        'CLCITY': '</p>',
        'CLSTATE': '</p>',
        'CLPHONE': '</p>',
        'CLEMAIL': '</p>',
        'CLDATE': '</p>',
        'CLYEAR': '</p>',
        'CLMOBJ': '</p>',
        'CLVOBJ': '</p>',
        'CLIMOBJ': '</p>',
        'CLHOLDER': '</p>',
        'CLGROUP': '</p>',
        'CLHEAD': '</p>',
        'CLFOOT': '</p>',
        'CLBODY': '</p>',
        'CLROW': '</p>',
        'OPIMPORTANT': '<p style="background-color: red; color:white: font-size:24px">' if conILIST==0 else '<ul style="background-color: red; color:white: font-size:24px">',
        'CLIMPORTANT': '</p>'if conILIST==0 else'</ul>',
        'OPLINK': '<a'+valor_href+'>',
        'CLLINK': '</a>',
        'VIDATA': '<video src="',
        'IMDATA': '<img src="',
        'OPILIST': '<ul>',
        'CLILIST': '</ul>'
    }

    if token in token_values:
        archivo.write(token_values[token])
    else:
        archivo.write(token)
        




def finTraduccion():
    archivo.write('</body>\n</html>')
    archivo.close()
    global traduccionCompleta
    traduccionCompleta=True


analizador = lex.lex(reflags=re.IGNORECASE)

