import ply.yacc as yacc
import os
import codecs
import re
import lexer
from lexer import tokens

def p_sigma(p):
    '''sigma    :   DOCTYPE docbook'''

def p_docbook(p):
    '''docbook  :   OPART   articulo   CLART'''

def p_articulo(p):
    '''articulo :   genArt | info genArt | title genArt | info title genArt 
    | genArt genS | info genArt genS | title genArt genS | info title genArt genS 
    | genArt genSS | info genArt genSS | title genArt genSS | info title genArt genSS'''

def p_genArt(p):
    '''genArt   :   itemizedList genArt | important genArt | para genArt | simPara genArt 
    | address genArt | mediaObject genArt | informalTable genArt | comment genArt 
    | abstract genArt | itemizedList | important | para | simPara | address | mediaObject 
    | informalTable | comment | abstarct'''

def p_genS(p):
    '''genS :   section | section genS'''

def p_genSS(p):
    '''genSS    :   simpleSec | simpleSec genSS'''

def p_texto(p):
    '''texto    :   TEXTO'''

def p_numero(p):
    '''numero   :   NUMERO'''

def p_section(p):
    '''section  :   OPSECT  genArt  CLSECT | OPSECT info title genArt   CLSECT 
    | OPSECT    info    genArt  CLSECT | OPSECT title   genArt  CLSECT 
    | OPSECT    genArt  genS    CLSECT | OPSECT info    genArt  genS CLSECT 
    | OPSECT    title   genArt  genS    CLSECT | OPSECT info    title   genArt  genS    CLSECT 
    | OPSECT    genArt genSS    CLSECT | OPSECT info genArt genSS   CLSECT 
    | OPSECT    title   genArt  genSS   CLSECT | OPSECT info    title   genArt  genSS   CLSECT'''

def p_simpleSec(p):
    '''simpleSec : OPSSECT info title genArt CLSSECT | OPSSECT info genArt CLSSECT 
    | OPSSECT title genArt CLSSECT | OPSSECT genArt CLSSECT'''
    
def p_genInfo(p):
    '''genInfo : mediaObject | abstract | address | author | date | copyright | title | mediaObject genInfo 
    | abstract genInfo | address genInfo | author genInfo | date genInfo | copyright genInfo | title genInfo'''

def p_info(p):
    '''info : OPINFO genInfo CLINFO'''

def p_genAbstr(p):
    '''genAbstr : para genAbstr | simPara genAbstr | para | simPara'''

def p_abstract(p):
    '''abstract : OPABST title genAbstr CLABST | OPABST genAbstr CLABST'''

def p_genAddress(p):
    '''genAddress : texto | street | city | state | phone | email | texto genAddress 
| street genAddress | city genAddress | state genAddress | phone genAddress | email genAddress'''

def p_address(p):
    '''address : OPADD genAddress CLADD'''

def p_genAuthor(p):
    '''genAuthor :  firstName | surName | firstName genAuthor | surName genAuthor'''

def p_author(p):
    '''author : OPAUTHOR genAuthor CLAUTHOR'''

def p_genCopy(p):
    '''genCopy : year | year genCopy'''

def p_genHolder(p):
    '''genHolder : holder | holder genHolder'''

def p_copyright(p):
    '''copyright : OPCOPY genCopy CLCOPY | OPCOPY genCopy genHolder CLCOPY'''

def p_genTitle(p):
    '''genTitle : texto | emphasis | link | email | texto genTitle | emphasis genTitle | link genTitle | email genTitle'''



