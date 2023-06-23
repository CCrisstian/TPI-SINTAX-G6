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

def p_title(p):
    '''title : OPTIT genTitle CLTIT'''

def p_genSECL(p):
    '''genSECL : texto | emphasis | link | email | author | comment | texto genSECL | emphasis genSECL | link genSECL 
    | email  genSECL| author genSECL| comment genSECL'''

def p_simPara(p):
    '''simPara : OPSPARA genSECL CLSPARA'''

def p_emphasis(p):
    '''emphasis : OPEMPH genSECL CLEMPH'''

def p_comment(p):
    '''comment : OPCOM genSECL CLCOM'''

def p_link(p):
    '''link :  genSECL link | genSECL'''
 
def p_genPara(p):
    '''genPara : texto | emphasis | link | email | author | comment | itemizedList | important | address | mediaObject 
    | informalTable | texto genPara | emphasis genPara | link genPara | email genPara | author genPara | comment genPara 
    | itemizedList genPara | important genPara | address genPara | mediaObject genPara | informalTable genPara'''

def p_para(p):
    '''para : OPPARA genPara CLPARA'''

def p_important(p):
    '''important : title genArt | genArt'''

def p_genFC(p):
    '''genFC : texto | link | emphasis | comment | texto genFC | link genFC | emphasis genFC | comment genFC '''

def p_firstName(p):
    '''firstName : OPFNAME genFC CLFNAME'''

def p_surname(p):
    '''surname : OPSNAME genFC CLSMANE'''

def p_street(p):
    '''street : OPSTREET genFC CLSTREET'''

def p_city(p):
    '''city : OPCITY genFC CLCITY'''

def p_state(p):
    '''state → OPSTATE genFC CLSTATE'''

def p_phone(p):
    '''Phone → OPPHONE genFC CLPHONE'''

def p_email(p):
    '''email : OPEMAIL genFC CLEMAIL'''

def p_date(p):
    '''date : OPDATE genFC CLDATE'''

def p_year(p):
    '''year : OPYEAR genFC CLYEAR'''

def p_holder(p):
    '''holder : OPHOLDER genFC CLHOLDER'''

def p_genMediaObj(p):
    '''genMediaObj : videoObject | imageObject | videoObject genMediaObj | imageObject genMediaObj'''

def p_mediaobject(p):
    '''mediaobject : OPMOBJ info videoObject CLMOBJ | OPMOBJ info imageObject CLMOBJ 
| OPMOBJ videoObject CLMOBJ | OPMOBJ imageObject CLMOBJ 
| OPMOBJ info videoObject genMediaObj CLMOBJ | OPMOBJ info imageObject genMediaObj CLMOBJ 
| OPMOBJ videoObject genMediaObj CLMOBJ | OPMOBJ imageObject genMediaObj CLMOBJ'''

def p_videoobject(p):
    '''videoObject : OPVOBJ info videoData CLVOBJ | OPVOBJ videoData CLVOBJ'''

VideoData → <videodata fileref='texto.VideoFormat' />

VideoFormat → MP4 | Ogg | WebM | AVI | MOV

def p_imageobject(p):
    '''imageobject : OPIMOBJ info imageData CLIMOBJ | OPIMOBJ imageData CLIMOBJ'''

ImageData → <imagedata fileref='texto.ImageFormat' />

ImageFormat → PNG | JPEG | GIF | SVG

def p_genItemizedList(p):
    '''genItemizedList : listItem | listItem genItemizedList'''

def p_itemizedlist(p):
    '''itemizedList :  OPILIST genItemizedList CLILIST'''

def p_genListItem(p):
    '''genListItem : itemizedList | genArt | itemizedList genListItem | genArt genListItem '''

def p_listitem(p):
    '''listItem : OPLITEM genListItem CLLITEM'''

def p_genTGroup(p):
    '''genTGroup : tGroup | tGroup genTGroup'''

def p_genInformalTable(p):
    '''genInformalTable : genMediaObj | genTGroup'''

def p_informaltable(p):
    '''InformalTable : OPINTAB genInformalTable CLINTAB'''

def p_tgroup(p):
    '''TGroup : OPTGROUP thead tfoot tbody CLTGROUP | OPTGROUP tfoot tbody CLTGROUP | OPTGROUP thead tbody CLTGROUP | OPTGROUP tbody CLTGROUP'''

def p_genHFB(p):
    '''genHFB : row | row genHFB'''

def p_thead(p):
    '''thead : OPHEAD genHFB CLHEAD'''

def p_tfoot(p):
    '''tfoot : OPFOOT genHFB CLFOOT'''

def p_tbody(p):
    '''tbody : OPBODY genHFB CLBODY'''

def p_genrow(p):
    '''genrow : entry | entrytbl | entry genrow | entrytbl genrow'''

def p_row(p):
    '''row : OPROW genrow CLROW'''

def p_entrytbl(p):
    '''entrytbl : thead tbody | tbody'''

def p_genEntry(p):
    '''genEntry : texto | itemizedList | important | para | simPara | mediaObject | comment | abstract 
    | texto genEntry | itemizedList genEntry | important genEntry | para genEntry | simPara genEntry 
    | mediaObject genEntry | comment genEntry | abstract genEntry'''

def p_entry(p):
    '''entry : OPENTRY genEntry CLENTRY'''

LINK →<link xlink:href= PROTOCOLO://DOMINIO_GRAL FINAL_URL </link>

FINAL_URL → /RUTA#LOCALIZADOR | /RUTA

PROTOCOLO → http | https | ftp | ftps

DOMINIO_GRAL → DOMINIO:PUERTO | DOMINIO

LOCALIZADOR → texto
DOMINIO → texto
RUTA →texto








