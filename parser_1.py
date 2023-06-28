import ply.yacc as yacc
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import re
import codecs
import lexer
from lexer import tokens
from termcolor import colored




contadorErrores = 0

def p_sigma(p):
    '''sigma    :   DOCTYPE docbook '''

def p_docbook(p):
    '''docbook  :   OPART articulo  CLART'''

def p_articulo(p):
    '''articulo :   genArt 
                | info genArt 
                | title genArt 
                | info title genArt 
                | genArt genS 
                | info genArt genS 
                | title genArt genS 
                | info title genArt genS 
                | genArt genSS 
                | info genArt genSS 
                | title genArt genSS 
                | info title genArt genSS'''

def p_genArt(p):
    '''genArt   : itemizedList genArt 
                | important genArt 
                | para genArt 
                | simPara genArt 
                | address genArt 
                | mediaObject genArt 
                | InformalTable genArt 
                | comment genArt 
                | abstract genArt 
                | itemizedList 
                | important 
                | para 
                | simPara 
                | address 
                | mediaObject 
                | InformalTable 
                | comment 
                | abstract'''

def p_genS(p):
    '''genS : section 
            | section genS'''

def p_genSS(p):
    '''genSS    : simpleSec 
                | simpleSec genSS'''

def p_texto(p):
    '''texto    :   TEXTO'''  

def p_numero(p):
    '''numero   :   NUMERO'''

def p_section(p):
    '''section  :   OPSECT  genArt  CLSECT 
                | OPSECT info title genArt   CLSECT 
                | OPSECT    info    genArt  CLSECT 
                | OPSECT title   genArt  CLSECT 
                | OPSECT    genArt  genS    CLSECT 
                | OPSECT info    genArt  genS CLSECT 
                | OPSECT    title   genArt  genS    CLSECT 
                | OPSECT info    title   genArt  genS    CLSECT 
                | OPSECT    genArt genSS    CLSECT 
                | OPSECT info genArt genSS   CLSECT 
                | OPSECT    title   genArt  genSS   CLSECT 
                | OPSECT info    title   genArt  genSS   CLSECT'''

def p_simpleSec(p):
    '''simpleSec : OPSSECT info title genArt CLSSECT 
                 | OPSSECT info genArt CLSSECT 
                 | OPSSECT title genArt CLSSECT 
                 | OPSSECT genArt CLSSECT'''
    
def p_genInfo(p):
    '''genInfo : mediaObject 
               | abstract 
               | address 
               | author 
               | date 
               | copyright 
               | title 
               | mediaObject genInfo 
               | abstract genInfo 
               | address genInfo 
               | author genInfo 
               | date genInfo 
               | copyright genInfo 
               | title genInfo'''

def p_info(p):
    '''info : OPINFO genInfo CLINFO'''

def p_genAbstr(p):
    '''genAbstr : para genAbstr 
                | simPara genAbstr 
                | para 
                | simPara'''

def p_abstract(p):
    '''abstract : OPABST title genAbstr CLABST 
                | OPABST genAbstr CLABST'''

def p_genAddress(p):
    '''genAddress : texto 
                  | street 
                  | city 
                  | state 
                  | phone 
                  | email 
                  | texto genAddress 
                  | street genAddress 
                  | city genAddress 
                  | state genAddress 
                  | phone genAddress 
                  | email genAddress'''

def p_address(p):
    '''address : OPADD genAddress CLADD'''

def p_genAuthor(p):
    '''genAuthor : firstName 
                 | surname 
                 | firstName genAuthor 
                 | surname genAuthor'''

def p_author(p):
    '''author : OPAUTHOR genAuthor CLAUTHOR'''

def p_genCopy(p):
    '''genCopy : year 
               | year genCopy'''

def p_genHolder(p):
    '''genHolder : holder 
                 | holder genHolder'''

def p_copyright(p):
    '''copyright : OPCOPY genCopy CLCOPY 
                 | OPCOPY genCopy genHolder CLCOPY'''

def p_genTitle(p):
    '''genTitle : texto 
                | emphasis 
                | link 
                | email 
                | texto genTitle 
                | emphasis genTitle 
                | link genTitle 
                | email genTitle'''

def p_title(p):
    '''title : OPTIT genTitle CLTIT'''

def p_genSECL(p):
    '''genSECL : texto 
                | emphasis 
                | link 
                | email 
                | author 
                | comment 
                | texto genSECL 
                | emphasis genSECL 
                | link genSECL 
                | email  genSECL
                | author genSECL
                | comment genSECL'''

def p_simPara(p):
    '''simPara : OPSPARA genSECL CLSPARA'''

def p_emphasis(p):
    '''emphasis : OPEMPH genSECL CLEMPH'''

def p_comment(p):
    '''comment : OPCOM genSECL CLCOM'''

def p_link(p):
    '''link :  genSECL link 
            | genSECL'''
 
def p_genPara(p):
    '''genPara : texto 
                | emphasis 
                | link 
                | email 
                | author 
                | comment 
                | itemizedList 
                | important 
                | address 
                | mediaObject 
                | InformalTable 
                | texto genPara 
                | emphasis genPara 
                | link genPara 
                | email genPara 
                | author genPara 
                | comment genPara 
                | itemizedList genPara 
                | important genPara 
                | address genPara 
                | mediaObject genPara 
                | InformalTable genPara'''

def p_para(p):
    '''para : OPPARA genPara CLPARA'''

def p_important(p):
    '''important : title genArt 
                 | genArt'''

def p_genFC(p):
    '''genFC : texto 
             | link 
             | emphasis 
             | comment 
             | texto genFC 
             | link genFC 
             | emphasis genFC 
             | comment genFC '''

def p_firstName(p):
    '''firstName : OPFNAME genFC CLFNAME'''

def p_surname(p):
    '''surname : OPSNAME genFC CLSMANE'''

def p_street(p):
    '''street : OPSTREET genFC CLSTREET'''

def p_city(p):
    '''city : OPCITY genFC CLCITY'''

def p_state(p):
    '''state : OPSTATE genFC CLSTATE'''

def p_phone(p):
    '''phone : OPPHONE genFC CLPHONE'''

def p_email(p):
    '''email : OPEMAIL genFC CLEMAIL'''

def p_date(p):
    '''date : OPDATE genFC CLDATE'''

def p_year(p):
    '''year : OPYEAR genFC CLYEAR'''

def p_holder(p):
    '''holder : OPHOLDER genFC CLHOLDER'''

def p_genMediaObj(p):
    '''genMediaObj : videoObject 
                    | imageObject 
                    | videoObject genMediaObj 
                    | imageObject genMediaObj'''

def p_mediaObject(p):
    '''mediaObject : OPMOBJ info videoObject CLMOBJ 
                    | OPMOBJ info imageObject CLMOBJ 
                    | OPMOBJ videoObject CLMOBJ 
                    | OPMOBJ imageObject CLMOBJ 
                    | OPMOBJ info videoObject genMediaObj CLMOBJ 
                    | OPMOBJ info imageObject genMediaObj CLMOBJ 
                    | OPMOBJ videoObject genMediaObj CLMOBJ 
                    | OPMOBJ imageObject genMediaObj CLMOBJ'''

def p_videoObject(p):
    '''videoObject : OPVOBJ info videoData CLVOBJ 
                    | OPVOBJ videoData CLVOBJ'''

def p_videoData(p):
    '''videoData : VIDAT'''

def p_imageObject(p):
    '''imageObject : OPIMOBJ info imageData CLIMOBJ 
                    | OPIMOBJ imageData CLIMOBJ'''

def p_imageData(p):
    '''imageData : IMDATA'''

def p_genItemizedList(p):
    '''genItemizedList : listItem 
                        | listItem genItemizedList'''

def p_itemizedlist(p):
    '''itemizedList :  OPILIST genItemizedList CLILIST'''

def p_genListItem(p):
    '''genListItem : itemizedList  
                    | genArt   
                    | itemizedList genListItem 
                    | genArt genListItem '''

def p_listitem(p):
    '''listItem : OPLITEM genListItem CLLITEM'''

def p_genTGroup(p):
    '''genTGroup : TGroup 
                 | TGroup genTGroup'''

def p_genInformalTable(p):
    '''genInformalTable : genMediaObj 
                        | genTGroup'''

def p_InformalTable(p):
    '''InformalTable : OPINTAB genInformalTable CLINTAB'''

def p_Tgroup(p):
    '''TGroup : OPTGROUP thead tfoot tbody CLTGROUP 
                | OPTGROUP tfoot tbody CLTGROUP 
                | OPTGROUP thead tbody CLTGROUP 
                | OPTGROUP tbody CLTGROUP'''

def p_genHFB(p):
    '''genHFB : row 
            | row genHFB'''

def p_thead(p):
    '''thead : OPHEAD genHFB CLHEAD'''

def p_tfoot(p):
    '''tfoot : OPFOOT genHFB CLFOOT'''

def p_tbody(p):
    '''tbody : OPBODY genHFB CLBODY'''

def p_genrow(p):
    '''genrow : entry 
                | entrytbl 
                | entry genrow 
                | entrytbl genrow'''

def p_row(p):
    '''row : OPROW genrow CLROW'''

def p_entrytbl(p):
    '''entrytbl : thead tbody 
                | tbody'''

def p_genEntry(p):
    '''genEntry : texto 
                | itemizedList 
                | important 
                | para 
                | simPara 
                | mediaObject 
                | comment 
                | abstract 
                | texto genEntry 
                | itemizedList genEntry 
                | important genEntry 
                | para genEntry 
                | simPara genEntry 
                | mediaObject genEntry 
                | comment genEntry 
                | abstract genEntry'''

def p_entry(p):
    '''entry : OPENTRY genEntry CLENTRY'''


def p_error(p):
    # p regresa como un objeto del Lexer.
    # p.__dict__ -> ver propiedades del objeto.
    global contadorErrores
    if (p):
        print(f'Error parser --> Tipo: {p.type} | Valor: {p.value}')
        print('Error sintáctico en LINEA:', p.lineno)

    contadorErrores += 1



# Crear una ventana de Tkinter oculta
ventana = Tk()
ventana.withdraw()
print ("Hola este es el analizador Lexico")

def opcion1():
    print("Has seleccionado elegir un archivo desde el equipo.")
    # Abrir el explorador de archivos y obtener la ruta del archivo seleccionado
    ruta_archivo = askopenfilename()
    directorio_archivo = os.path.dirname(ruta_archivo)
    fp=codecs.open(ruta_archivo,"r","UTF-8")
    global file_HTML
    file_HTML=open(directorio_archivo + "\\File.html","w")
    cad=fp.read()
    analizador = yacc.yacc()
    resultado=analizador.parse(cad)
    print('El resultado es ',resultado)
    print("\nLista de tokens\n")
    while True:
        tok = analizador.token()
        if not tok : break
        print(colored('Con el lexema: \n', 'green'),tok)
    
    #if contadorErrores > 0:
    #        print('(⨉) Ocurrió un error sintáctico.')
    #        # Resetear contador
    #        contadorErrores = 0
    #        reload(lexer)
    #else:
    #        print('✅ El archivo es sintacticamente correcto!')
    #        # Ejecutar exportacion de html
    #        print('(✅) Sintácticamente correcto. Se exportó un .html con los comentarios.')
    #        print('(!) Se exportó un .txt con las producciones analizadas.')
    
    file_HTML.close()
    fp.close()

    


def opcion2():
    print("Has seleccionado ingresarlo por teclado.")
    while True:
        linea = input("Ingresa una línea (presiona Enter para continuar, o escribe 'salir' para terminar): ")
        if linea == "salir":
            break
        cad=''
        cad=cad+linea
        analizador = yacc.yacc()
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
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")