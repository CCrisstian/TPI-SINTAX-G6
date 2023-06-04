import ply.lex as lex
import sys
import re
import codecs
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from termcolor import colored


#definimos una lista con los tokens a utilizar
tokens=[
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
    'VFORM', #VIDEO FORMATO
    'OPIMOBJ', #IMAGEN OBJECT
    'CLIMOBJ',
    'IMDATA', #IMAGEN DATA
    'IMFORM', #IMAGEN FORMAT
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
    return t 

#Definicion de la expresion regular de Cerrar section
def t_CLSECT(t):
    r'</section>'
    print(colored('Se encontro el token </section>' ,'green'))
    return t 

#Definicion de la expresion regular de Abrir simlpesection
def t_OPSSECT(t):
    r'<simplesect>'
    print(colored('Se encontro el token <simplesect>' ,'green'))
    return t 

#Definicion de la expresion regular de Abrir simplesection
def t_CLSSECT(t):
    r'</simplesect>'
    print(colored('Se encontro el token </simplesect>' ,'green'))
    return t 

#Definicion de la expresion regular de Abrir info
def t_OPINFO(t):
    r'<info>'
    print(colored('Se encontro el token <info>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar info
def t_CLINFO(t):
    r'</info>'
    print(colored('Se encontro el token </info>' ,'green'))
    return t 

#Definicion de la expresion regular de Abrir abstract
def t_OPABST(t):
    r'<abstract>'
    print(colored('Se encontro el token <abstract>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar abstract
def t_CLABST(t):
    r'</abstract>'
    print(colored('Se encontro el token </abstract>' ,'green'))
    return t 

#Definicion de la expresion regular de Abrir address
def t_OPADD(t):
    r'<address>'
    print(colored('Se encontro el token <address>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar address
def t_CLADD(t):
    r'</address>'
    print(colored('Se encontro el token </address>' ,'green'))
    return t 

#Definicion de la expresion regular de Abrir author
def t_OPAUTHOR(t):
    r'<author>'
    print(colored('Se encontro el token <author>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar author
def t_CLAUTHOR(t):
    r'</author>'
    print(colored('Se encontro el token </author>' ,'green'))
    return t 

#Definicion de la expresion regular de Abrir copyright
def t_OPCOPY(t):
    r'<copyright>'
    print(colored('Se encontro el token <copyright>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar copyright
def t_CLCOPY(t):
    r'</copyright>'
    print(colored('Se encontro el token </copyright>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir title
def t_OPTIT(t):
    r'<title>'
    print(colored('Se encontro el token <title>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar title
def t_CLTIT(t):
    r'</title>'
    print(colored('Se encontro el token </title>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir simpara
def t_OPSPARA(t):
    r'<simpara>'
    print(colored('Se encontro el token <simpara>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar simpara
def t_CLSPARA(t):
    r'</simpara>'
    print(colored('Se encontro el token </simpara>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir emphasis
def t_OPEMPH(t):
    r'<emphasis>'
    print(colored('Se encontro el token <emphasis>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar emphasis
def t_CLEMPH(t):
    r'</emphasis>'
    print(colored('Se encontro el token </emphasis>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir comment
def t_OPCOM(t):
    r'<comment>'
    print(colored('Se encontro el token <comment>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar comment
def t_CLCOM(t):
    r'</comment>'
    print(colored('Se encontro el token </comment>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir para
def t_OPPARA(t):
    r'<para>'
    print(colored('Se encontro el token <para>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar para
def t_CLPARA(t):
    r'</para>'
    print(colored('Se encontro el token </para>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir firstname
def t_OPFNAME(t):
    r'<firstname>'
    print(colored('Se encontro el token <firstname>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar firstname
def t_CLFNAME(t):
    r'</firstname>'
    print(colored('Se encontro el token </firstname>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir surname
def t_OPSNAME(t):
    r'<surname>'
    print(colored('Se encontro el token <surname>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar surname
def t_CLSMANE(t):
    r'</surname>'
    print(colored('Se encontro el token </surname>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir street
def t_OPSTREET(t):
    r'<street>'
    print(colored('Se encontro el token <street>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar street
def t_CLSTREET(t):
    r'</street>'
    print(colored('Se encontro el token </street>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir city
def t_OPCITY(t):
    r'<city>'
    print(colored('Se encontro el token <city>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar city
def t_CLCITY(t):
    r'</city>'
    print(colored('Se encontro el token </city>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir state
def t_OPSTATE(t):
    r'<state>'
    print(colored('Se encontro el token <state>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar state
def t_CLSTATE(t):
    r'</state>'
    print(colored('Se encontro el token </state>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir phone
def t_OPPHONE(t):
    r'<phone>'
    print(colored('Se encontro el token <phone>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar phone
def t_CLPHONE(t):
    r'</phone>'
    print(colored('Se encontro el token </phone>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir email
def t_OPEMAIL(t):
    r'<email>'
    print(colored('Se encontro el token <emails>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar email
def t_CLEMAIL(t):
    r'</email>'
    print(colored('Se encontro el token </emails>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir date
def t_OPDATE(t):
    r'<date>'
    print(colored('Se encontro el token <date>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar date
def t_CLDATE(t):
    r'</date>'
    print(colored('Se encontro el token </date>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir year
def t_OPYEAR(t):
    r'<year>'
    print(colored('Se encontro el token <year>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar year
def t_CLYEAR(t):
    r'</year>'
    print(colored('Se encontro el token </year>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir holder
def t_OPHOLDER(t):
    r'<holder>'
    print(colored('Se encontro el token <holder>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar holder
def t_CLHOLDER(t):
    r'</holder>'
    print(colored('Se encontro el token </holder>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir mediaobject
def t_OPMOBJ(t):
    r'<mediaobject>'
    print(colored('Se encontro el token <mediaobject>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar mediaobject
def t_CLMOBJ(t):
    r'</mediaobject>'
    print(colored('Se encontro el token </mediaobject>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir videoobject
def t_OPVOBJ(t):
    r'<videoobject>'
    print(colored('Se encontro el token <videoobject>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar videoobject
def t_CLVOBJ(t):
    r'</videoobject>'
    print(colored('Se encontro el token </videoobject>' ,'green'))
    return t

#Definición de 'VIDAT', 'VFORM' PENDIENTE

def t_VIDAT(t):
    r'<videodata\s+fileref="(?:[^"]+)"\s*/>'
    print(colored('Se encontro el token <videodata>' ,'green'))
    return t


#Definicion de la expresion regular de Abrir imageobject
def t_OPIMOBJ(t):
    r'<imageobject>'
    print(colored('Se encontro el token <imagenobject>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar imageobject
def t_CLIMOBJ(t):
    r'</imageobject>'
    print(colored('Se encontro el token </imagenobject>' ,'green'))
    return t

#Definición de 'IMDATA', 'IMFORM' PENDIENTE

def t_IMDATA(t):
    r'<imagedata\s+fileref="(?:[^"]+)"\s*/>'
    print(colored('Se encontro el token <imagendata>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir itemizedlist
def t_OPILIST(t):
    r'<itemizedlist>'
    print(colored('Se encontro el token <itemizedlist>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar itemizedlist
def t_CLILIST(t):
    r'</itemizedlist>'
    print(colored('Se encontro el token </itemizedlist>' ,'green'))
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
    return t 

#Definicion de la expresion regular de Cerrar informaltable
def t_CLINTAB(t):
    r'</informaltable>'
    print(colored('Se encontro el token </informaltable>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir tgroup
def t_OPTGROUP(t):
    r'<tgroup>'
    print(colored('Se encontro el token <tgroup>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar tgroup
def t_CLGROUP(t):
    r'</tgroup>'
    print(colored('Se encontro el token </tgroup>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir thead
def t_OPHEAD(t):
    r'<thead>'
    print(colored('Se encontro el token <thead>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar thead
def t_CLHEAD(t):
    r'</thead>'
    print(colored('Se encontro el token </thead>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir tfoot
def t_OPFOOT(t):
    r'<tfoot>'
    print(colored('Se encontro el token <tfoot>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar tfoot
def t_CLFOOT(t):
    r'</tfoot>'
    print(colored('Se encontro el token </tfoot>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir tbody
def t_OPBODY(t):
    r'<tbody>'
    print(colored('Se encontro el token <tbody>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar tbody
def t_CLBODY(t):
    r'</tbody>'
    print(colored('Se encontro el token </tbody>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir row
def t_OPROW(t):
    r'<row>'
    print(colored('Se encontro el token <row>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar row
def t_CLROW(t):
    r'</row>'
    print(colored('Se encontro el token </row>' ,'green'))
    return t

#Definicion de la expresion regular de Abrir entry
def t_OPENTRY(t):
    r'<entry>'
    print(colored('Se encontro el token <entry>' ,'green'))
    return t 

#Definicion de la expresion regular de Cerrar entry
def t_CLENTRY(t):
    r'</entry>'
    print(colored('Se encontro el token </entry>' ,'green'))
    return t

#Definicion de la expresion regular de link PENDIENTE
def t_OPLINK(t):
    r'<(link)(\s+xlink:href=")((https?|ftps?)://[\w\-]+(\.[\w\-]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?)"'
    print(colored('Se encontro el token LINK' ,'green'))
    return(t)


def t_CLLINK(t):
    r'</link>'
    print(colored('Se encontro el token </link>' ,'green'))
    return(t)

#Definicion de la expresion regular de un texto
def t_TEXTO(t):
    r'([0-9]*[a-zA-Z ,.;#:&?+/()_-][0-9]*[a-zA-Z ,.;#:&?+/()_-]*[0-9]*)'
    if t.value.upper() in tokens:
        t.value = t.value.upper()
        t.type= t.value
    print(colored('Se encontro el token TEXTO' ,'green'))
    return t

#Definicion de la expresion regular de un numero
def t_NUMERO(t):
    r'[0-9][0-9]*'
    print(colored('Se encontro el token NUMERO' ,'green'))
    return t

def t_error(t):
    print(colored("Error lexico en la linea", "red"), str(t.lineno))
    t.lexer.skip(1)


print ("Hola este es el analizador Lexico")
 # Crear una ventana de Tkinter oculta
ventana = Tk()
ventana.withdraw()

def opcion1():
    print("Has seleccionado elegir un archivo desde el equipo.")
    # Abrir el explorador de archivos y obtener la ruta del archivo seleccionado
    ruta_archivo = askopenfilename()
    fp=codecs.open(ruta_archivo,"r","UTF-8")
    cad=fp.read()
    fp.close
    analizador = lex.lex(reflags=re.IGNORECASE)
    analizador.input(cad)  
    print("\nLista de tokens\n")
    while True:
        tok = analizador.token()
        if not tok : break
        print(colored('Con el lexema: \n', 'green'),tok) 


def opcion2():
    print("Has seleccionado ingresarlo por teclado.")
    while True:
        linea = input("Ingresa una línea (presiona Enter para continuar, o escribe 'salir' para terminar): ")
        if linea == "salir":
            break
        cad=''
        cad=cad+linea
        analizador = lex.lex(reflags=re.IGNORECASE)
        analizador.input(cad)  
        print("\nLista de tokens\n")
        while True:
            tok = analizador.token()
            if not tok : break
            print(colored('Con el lexema: \n', 'green'),tok) 
        

while True:
    print('MENU')
    print('1. Elegir un archivo')
    print("2. Ingresarlo por teclado")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")


