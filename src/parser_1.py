from imp import reload
from tkinter import filedialog
import ply.yacc as yacc
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import re
import codecs
from AnalizadorL import tokens, inicioTraduccion, finTraduccion 
from termcolor import colored
from sys import stdin

contadorErrores = 0

def p_sigma(p):
    '''sigma    :   DOCTYPE docBook '''


def p_docBook(p):
    '''docBook  :   OPART articulo CLART'''



def p_articulo(p):
    '''articulo :  info genArt
                | title genArt
                | info title genArt
                | genArt
                | info genArt simpleSec
                | title genArt simpleSec
                | info title genArt simpleSec
                | genArt simpleSec
                | info genArt section
                | info section
                | title genArt section
                | info title genArt section
                | genArt section'''





def p_genArt(p):
    '''genArt   : itemizedList  
                | important 
                | para 
                | simpara 
                | address 
                | informalTable 
                | comment 
                | abstract
                | itemizedList genArt
                | important genArt
                | para genArt
                | simpara genArt
                | address genArt
                | informalTable genArt
                | comment genArt
                | abstract genArt'''

def p_section(p):
    '''section  : OPSECT info genSect1 CLSECT
                | OPSECT title genSect1 CLSECT
                | OPSECT info title genSect1 CLSECT
                | OPSECT genSect1 CLSECT
                | OPSECT info genSect1 genSect2 CLSECT
                | OPSECT title genSect1 genSect2 CLSECT
                | OPSECT info title genSect1 genSect2 CLSECT
                | OPSECT genSect1 genSect2 CLSECT
                | OPSECT info genSect1 genSect3 CLSECT
                | OPSECT title genSect1 genSect3 CLSECT
                | OPSECT info title genSect1 genSect3 CLSECT
                | OPSECT genSect1 genSect3 CLSECT'''
                
def p_genSect1(p):
    '''genSect1 : itemizedList  
                | important 
                | para
                | simpara
                | address
                | mediaObject
                | informalTable
                | comment
                | abstract
                | itemizedList genSect1  
                | important genSect1
                | para genSect1
                | simpara genSect1
                | address genSect1
                | mediaObject genSect1
                | informalTable genSect1
                | comment genSect1
                | abstract genSect1'''
            
def p_genSect2(p):
    '''genSect2 : simpleSec
                | simpleSec genSect2'''
            
def p_genSect3(p):
    '''genSect3 : section
                | section genSect3'''

def p_simpleSec(p):
    '''simpleSec : OPSSECT info genSSect CLSSECT
                | OPSSECT title genSSect CLSSECT
                | OPSSECT info title genSSect CLSSECT
                | OPSSECT genSSect CLSSECT'''

def p_genSSect(p):
    '''genSSect    : itemizedList  
                | important 
                | para 
                | simpara 
                | address 
                | mediaObject 
                | informalTable 
                | comment 
                | abstract
                | itemizedList genSSect
                | important genSSect
                | para genSSect
                | simpara genSSect
                | address genSSect
                | mediaObject genSSect
                | informalTable genSSect
                | comment genSSect
                | abstract genSSect'''

def p_geninfo(p):
    '''geninfo : title  
                | abstract 
                | address 
                | author 
                | date 
                | copyright 
                | mediaObject 
                | mediaObject geninfo
                | abstract geninfo
                | address geninfo
                | author geninfo
                | date geninfo
                | copyright geninfo
                | title geninfo'''

def p_info(p):
    '''info : OPINFO geninfo CLINFO'''

def p_abstract(p):
    '''abstract : OPABST title genAbstr CLABST
                | OPABST genAbstr CLABST'''
                
def p_genAbstr(p):
    '''genAbstr : para
                | simpara
                | para genAbstr
                | simpara genAbstr'''

def p_address(p):
    '''address : OPADD CLADD
                | OPADD genAdd CLADD'''

def p_genAdd(p):
    '''genAdd : TEXTO
            | street 
            | city 
            | state 
            | phone 
            | email 
            | TEXTO genAdd
            | street genAdd
            | city genAdd
            | state genAdd
            | phone genAdd
            | email genAdd'''

def p_author(p):
    '''author : OPAUTHOR genauthor  CLAUTHOR'''

def p_genauthor (p):
    '''genauthor  : firstName 
                | surName 
                | firstName genauthor 
                | surName genauthor'''

def p_copyright(p):
    '''copyright : OPCOPY genCopy1 CLCOPY
                | OPCOPY genCopy1 genCopy2 CLCOPY'''

def p_genCopy1(p):
    '''genCopy1 : year
                | year genCopy1'''

def p_genCopy2(p):
    '''genCopy2 : holder 
                | holder genCopy2'''

def p_title(p):
    '''title : OPTIT gentitle CLTIT'''
    
def p_gentitle(p):
    '''gentitle : TEXTO 
                | emphasis 
                | link 
                | email
                | TEXTO gentitle
                | emphasis gentitle
                | link gentitle
                | email gentitle'''

def p_simpara(p):
    '''simpara : OPSPARA genSpara CLSPARA'''

def p_genSpara(p):
    '''genSpara : TEXTO 
                | emphasis 
                | link 
                | email
                | author
                | comment
                | TEXTO genSpara
                | emphasis genSpara
                | link genSpara
                | email genSpara
                | author genSpara
                | comment genSpara'''

def p_emphasis(p):
    '''emphasis : OPEMPH genEmp CLEMPH'''

def p_genEmp(p):
    '''genEmp : TEXTO 
            | emphasis 
            | link 
            | email
            | author
            | comment
            | TEXTO genEmp
            | emphasis genEmp
            | link genEmp
            | email genEmp
            | author genEmp
            | comment genEmp'''

def p_comment(p):
    '''comment : OPCOM genCom CLCOM'''

def p_genCom(p):
    '''genCom : TEXTO 
            | emphasis 
            | link 
            | email
            | author
            | comment
            | TEXTO genCom
            | emphasis genCom
            | link genCom
            | email genCom
            | author genCom
            | comment genCom'''

def p_link(p):
    '''link :  OPLINK genlink CLLINK'''

def p_genlink(p):
    '''genlink : TEXTO 
            | emphasis 
            | link 
            | email
            | author
            | comment
            | TEXTO genlink
            | emphasis genlink
            | link genlink
            | email genlink
            | author genlink
            | comment genlink'''

def p_para(p):
    '''para : OPPARA genpara CLPARA'''

def p_genpara(p):
    '''genpara : TEXTO 
            | emphasis 
            | link 
            | email
            | author
            | comment
            | itemizedList 
            | important 
            | address 
            | mediaObject 
            | informalTable
            | TEXTO genpara
            | emphasis genpara
            | link genpara
            | email genpara
            | author genpara
            | comment genpara
            | itemizedList genpara
            | important genpara
            | address genpara
            | mediaObject genpara
            | informalTable genpara'''

def p_important(p):
    '''important : OPIMPORT title genImport CLIMPORT
                | OPIMPORT genImport CLIMPORT'''

def p_genImport(p):
    '''genImport : itemizedList
                | important
                | para
                | simpara
                | address
                | mediaObject 
                | informalTable
                | comment
                | abstract
                | itemizedList genImport
                | important genImport
                | para genImport
                | simpara genImport
                | address genImport
                | mediaObject genImport
                | informalTable genImport
                | comment genImport
                | abstract genImport'''

def p_firstName(p):
    '''firstName : OPFNAME genFN CLFNAME'''
    
def p_genFN(p):
    '''genFN : TEXTO
            | link 
            | emphasis 
            | comment
            | TEXTO genFN
            | link genFN
            | emphasis genFN 
            | comment genFN'''

def p_surName(p):
    '''surName : OPSNAME genSN CLSMANE'''
    
def p_genSN(p):
    '''genSN : TEXTO
            | link 
            | emphasis 
            | comment
            | TEXTO genSN
            | link genSN
            | emphasis genSN
            | comment genSN'''

def p_street(p):
    '''street : OPSTREET genstreet CLSTREET'''

def p_genstreet(p):
    '''genstreet : TEXTO
                | link 
                | emphasis 
                | comment
                | TEXTO genstreet
                | link genstreet
                | emphasis genstreet
                | comment genstreet'''

def p_city(p):
    '''city : OPCITY gencity CLCITY'''
    
def p_gencity(p):
    '''gencity : TEXTO
            | link 
            | emphasis 
            | comment
            | TEXTO gencity
            | link gencity
            | emphasis gencity
            | comment gencity'''

def p_state(p):
    '''state : OPSTATE genSate CLSTATE'''

def p_genSate(p):
    '''genSate : TEXTO
            | link 
            | emphasis 
            | comment
            | TEXTO genSate
            | link genSate
            | emphasis genSate
            | comment genSate'''
            
def p_phone(p):
    '''phone : OPPHONE genphone CLPHONE'''
    
def p_genphone(p):
    '''genphone : TEXTO
                | link 
                | emphasis 
                | comment
                | TEXTO genphone
                | link genphone
                | emphasis genphone
                | comment genphone'''
            
def p_email(p):
    '''email : OPEMAIL  genemail CLEMAIL'''

def p_genemail(p):
    '''genemail : TEXTO
                | link 
                | emphasis 
                | comment
                | TEXTO genemail
                | link genemail
                | emphasis genemail
                | comment genemail'''

def p_date(p):
    '''date : OPDATE  gendate CLDATE'''

def p_gendate(p):
    '''gendate : TEXTO
            | link 
            | emphasis 
            | comment
            | TEXTO gendate
            | link gendate
            | emphasis gendate
            | comment gendate'''

def p_year(p):
    '''year : OPYEAR  genyear CLYEAR'''

def p_genyear(p):
    '''genyear : TEXTO
            | link 
            | emphasis 
            | comment
            | TEXTO genyear
            | link genyear
            | emphasis genyear
            | comment genyear'''

def p_holder(p):
    '''holder : OPHOLDER  genholder CLHOLDER'''

def p_genholder(p):
    '''genholder : TEXTO
                | link 
                | emphasis 
                | comment
                | TEXTO genholder
                | link genholder
                | emphasis genholder
                | comment genholder'''

def p_mediaObject(p):
    '''mediaObject : OPMOBJ info videoObject CLMOBJ
                | OPMOBJ info imageObject CLMOBJ
                | OPMOBJ videoObject CLMOBJ
                | OPMOBJ imageObject CLMOBJ
                | OPMOBJ info videoObject genMO CLMOBJ
                | OPMOBJ info imageObject genMO CLMOBJ
                | OPMOBJ videoObject genMO CLMOBJ
                | OPMOBJ imageObject genMO CLMOBJ'''

def p_genMO(p):
    '''genMO : videoObject
                    | imageObject
                    | videoObject genMO
                    | imageObject genMO'''


def p_itemizedList(p):
    '''itemizedList :  OPILIST genIList CLILIST'''

def p_genIList(p):
    '''genIList : listItem
                | listItem genIList'''


def p_videoObject(p):
    '''videoObject :  OPVOBJ VIDAT CLVOBJ
                    | OPVOBJ info VIDAT CLVOBJ'''

def p_imageObject (p):
    '''imageObject  : OPIMOBJ IMDATA CLIMOBJ
                    | OPIMOBJ info IMDATA CLIMOBJ'''


def p_listItem(p):
    '''listItem : OPLITEM genlistItem CLLITEM'''
    
def p_genlistItem(p):
    '''genlistItem : itemizedList
                | important
                | para
                | simpara
                | address
                | mediaObject
                | informalTable
                | comment
                | abstract
                | itemizedList genlistItem
                | important genlistItem
                | para genlistItem
                | simpara genlistItem
                | address genlistItem
                | mediaObject genlistItem
                | informalTable genlistItem
                | comment genlistItem
                | abstract genlistItem'''

def p_informalTable(p):
    '''informalTable : OPINTAB genIT1 CLINTAB
                    | OPINTAB genIT2 CLINTAB'''

def p_genIT1 (p):
    '''genIT1  : address
                | address genIT1'''
                
def p_genIT2 (p):
    '''genIT2  : tGroup
            | tGroup genIT2'''

def p_tGroup(p):
    '''tGroup : OPTGROUP thead CLTGROUP
            | OPTGROUP tfoot CLTGROUP
            | OPTGROUP tbody CLTGROUP'''
            
def p_thead(p):
    '''thead : OPHEAD genHFB CLHEAD'''

def p_tfoot(p):
    '''tfoot : OPFOOT genHFB CLFOOT'''
            
def p_tbody(p):
    '''tbody : OPBODY genHFB CLBODY'''

def p_genHFB(p):
    '''genHFB : row
            | row genHFB'''
            
def p_row(p):
    '''row : OPROW genrow CLROW'''
    
def p_genrow(p):
    '''genrow : entry
            | entry genrow'''

def p_entry(p):
    '''entry : OPENTRY genentry CLENTRY'''
    
def p_genentry(p):
    '''genentry : TEXTO 
                | itemizedList 
                | important 
                | para 
                | simpara 
                | address 
                | comment 
                | abstract 
                | TEXTO genentry
                | itemizedList genentry
                | important genentry
                | para genentry
                | simpara genentry
                | address genentry
                | comment genentry
                | abstract genentry'''

def p_error(p):
    # p regresa como un objeto del Lexer.
    # p.__dict__ -> ver propiedades del objeto.
    global contadorErrores
    if (p):
        print(f'Error parser --> Tipo: {p.type} | Valor: {p.value}')
        print('Error sintáctico en LINEA:', p.lineno)
    contadorErrores += 1


parser=yacc.yacc(start='sigma')
# Crear una ventana de Tkinter oculta
ventana = Tk()
ventana.withdraw()
print ("Hola este es el analizador Sintactico")

def opcion1():
    print("Has seleccionado elegir un archivo desde el equipo.")
    # Abrir el explorador de archivos y obtener la ruta del archivo seleccionado
    ruta_archivo = askopenfilename()
    directorio_archivo = os.path.dirname(ruta_archivo)
    fp=codecs.open(ruta_archivo,"r","UTF-8")
    cad=fp.read()
    inicioTraduccion(directorio_archivo + "\\File.html")
    result=parser.parse(cad)
    print(result)
    finTraduccion()
    global contadorErrores
    if contadorErrores > 0:
        print('(⨉) Ocurrió un error sintáctico.')
        # Resetear contador
        contadorErrores = 0
    else:
        print('✅ El archivo es sintacticamente correcto!')
        # Ejecutar exportacion de html
        print('(✅) Sintácticamente correcto. Se exportó un .html con los comentarios.')
        print('(!) Se exportó un .txt con las producciones analizadas.')

    fp.close()

    


def opcion2():
    print("Has seleccionado ingresarlo por teclado.")
    while True:
        linea = input("Ingresa una línea (presiona Enter para continuar, o escribe 'salir' para terminar): ")
        if linea == "salir":
            finTraduccion()
            break
        cad=''
        cad=cad+linea
        inicioTraduccion(os.getcwd() + "\\File.html") #getcwd devuelve la ruta actual

            # Mostrar el cuadro de diálogo para guardar archivo
    file_path = filedialog.asksaveasfilename(
    initialdir="/",  # Carpeta inicial mostrada en el cuadro de diálogo
    title="Guardar archivo",  # Título del cuadro de diálogo
    filetypes=(("Archivos de texto", "*.html"), ("Todos los archivos", "*.*")))  # Filtros de archivo

    inicioTraduccion(file_path)
    
    if file_path:
    # Realizar las operaciones necesarias con el archivo
    # En este ejemplo, simplemente imprimimos la ruta del archivo seleccionado
        print("Archivo guardado en:", file_path)
    else:
        print("No se seleccionó ningún archivo.")

    result=parser.parse(cad)
    print(result)
    global contadorErrores
    if contadorErrores > 0:
        print('(⨉) Ocurrió un error sintáctico.')
        # Resetear contador
        contadorErrores = 0
    else:
        print('✅ El archivo es sintacticamente correcto!')
        # Ejecutar exportacion de html
        print('(✅) Sintácticamente correcto. Se exportó un .html con los comentarios.')
        print('(!) Se exportó un .txt con las producciones analizadas.')
    
    finTraduccion()
        
        

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
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")