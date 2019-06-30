import qmk_kc
import re, json
from tkinter import Tk
r=Tk()
r.withdraw()
#END OF IMPORT
comb=[]             #combined layer ready for output
fill1='──────┬'      #top fill lines 
fill2='──────┼'     #middle row fill lines
fill3='──────┴'     #bottom fill lines
fill4th='──'
laystart=False      #has the program found a layer start
layers=0            #how many layers
KClayers=[]         #array of all KClines
KClines=[]          #list if all KC on line
nl='\n'
width=[]
names=[]
layname=""
notdef=[]
ends=['','}']
path=''
mapstart1=False
mapstart2=False
layout=''
jsonmap=[]
jsonrep=['w','x','y',':','"','{','}',']']
#END OF VARS
try:
    inpt=open('keymap.c','r')
except FileNotFoundError:
    print("+- File Not Found Error -+")
    exit()
inpList=inpt.readlines()
inpt.close()
file=open('comment.txt','w+',encoding='utf-8')
#OPEN AND CONVERT TO CORRECT FORMAT
for line in inpList:
    line=line.replace('\n','')
    line=line.replace('\\','')
    for possible in ends:
        if line==possible:
            end=True
        else:
            end=False
    if line.count('#define '):
        notdef.append(line)
    line=line.replace(' ','')
    if line.count(')')==1 and line.count('(')==0 and laystart==True or end==True and laystart==True:
        laystart=False
        KClayers.append(KClines)
        KClines=[]
        layers+=1
    elif laystart==True:
        KClines.append(line)
    if re.search('LAYOUT',line):
        laystart=True
        layout=line
        fnd = re.search('\[(.+?)\]',line)
        if fnd:
            layname=fnd.group(1).replace("_","")
            names.append(layname)
assert len(KClayers)>0,'+- No keymap Found -+'
assert layers==len(KClayers),'+- Layer Error -+'
print('Successfully imported layers')
lyrcount=layers
widthlist=[]
Xlist=[]
Ylist=[]
widtharray=[[]]
#READ CONFIG.JSON FOR KEY SIZES
if qmk_kc.yesno('Search for info.json')==True:
    #TRIM DOWN 'layout' VAR
    layout = re.sub('\[(.+?)\]','',layout)
    layout = layout.replace('(','')
    layout = layout.replace('=','')
    with open('info.json') as json_file:
        data = json.load(json_file)
        jsonrange = data['layouts'][layout]['layout']
#PRINT TO FILE
for layer in range(0,len(KClayers)):
    lyrcount-=1
    for num in range(0,len(KClayers[layer])):
        crtln=(KClayers[layer][num])
        if crtln.endswith(',')==False:
            crtln=crtln+','
        colm=crtln.count(',')
        colm2=colm-1
        width.append(colm2)
        crtln=' * ,'+crtln
        fixed=qmk_kc.replkc(crtln,notdef)
        comb.append(fixed)
        lines=len(comb)
    file.write(nl)
    print(f'/* {names[layer]}',file=file)
    print(f' * ┌{fill1*width[0]}──────┐', file=file)
    for num in range(0,lines):
        file.write(comb[num]+nl)
        if lines>1 and num<(lines-1):
            print(f' * ├{fill2*width[num]}──────┤', file=file)
    print(f' * └{fill3*width[len(width)-1]}──────┘',file=file)
    print(' */',file=file)
    print('Layer '+str(layer+1)+' Done')
    comb=[]
file.close()
#ASK IF CLIPBOARD
if qmk_kc.yesno('Enable paste to Clipboard')==True:
    opclp=open('comment.txt','r',encoding='utf-8')
    clip=opclp.read()    
    r.clipboard_clear()
    r.clipboard_append(clip)
    r.update()
    r.destroy()
    print('Added to Clipboard')
print('Done printing Keymap')
