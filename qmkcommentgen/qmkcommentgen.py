import re
from pathlib import Path

try:
    from tkinter import Tk
except ImportError:
    Tk = None

from . import keymap


def replkc(line,others):
    for rfrom, rto in keymap.keycodes.items():
        line=line.replace(rfrom, rto)
    if not others==[]:
        for defin in others:
            defin=defin.replace("#define ","")
            newdef=defin.split()
            line=line.replace(newdef[0],newdef[1])
    return line 


def paste_to_clipboard(output_file_path: Path):
    """
    Paste to Clipboard
    :param output_file_path: Output file that contains comments text
    """
    if Tk is None:
        print("Dependency tkinter is not installed and is required to paste to clipboard.")
        exit(1)
    with output_file_path.open('r') as opclp:
        clip=opclp.read()   
    r=Tk()
    r.withdraw() 
    r.clipboard_clear()
    r.clipboard_append(clip)
    r.update()
    r.destroy()


def gen_comment(keymap_path: Path, output_file_path: Path):
    """
    Generate Keymap Comments
    :param keymap_path: Path to keymap.c
    :param output_file_path: Output file to write comments text
    """
    comb=[]             #combined layer ready for output
    fill='──────┬'      #top fill lines 
    fill2='──────┼'     #middle row fill lines
    fill3='──────┴'     #bottom fill lines
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

    #open keymap file
    with keymap_path.open('r') as inpt:
        # add all lines of keymap to inpList var
        inpList=inpt.readlines()

    with output_file_path.open('w+',encoding='utf-8') as output_file:
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
            #remove whitespace and new lines
            line=line.replace(' ','')
            if line.count(')')==1 and line.count('(')==0 and laystart==True or end==True and laystart==True:
                #if it is the end of a layer
                laystart=False
                #add layer to KClayers
                KClayers.append(KClines)
                KClines=[]
                layers+=1
            elif laystart==True:
                #if it part of keymap add it to KC lines
                KClines.append(line)
            if re.search('LAYOUT',line):
                laystart=True
                fnd = re.search('\[(.+?)\]',line)
                if fnd:
                    layname=fnd.group(1).replace("_","")
                    names.append(layname)
        assert len(KClayers)>0,'+- No keymap Found -+'
        assert layers==len(KClayers),'+- Layer Error -+'
        print('Successfully imported layers')
        lyrcount=layers
        for layer in range(0,len(KClayers)):
            lyrcount-=1
            for num in range(0,len(KClayers[layer])):
                #define current layer
                crtln=(KClayers[layer][num])
                if crtln.endswith(',')==False:
                    crtln=crtln+','
                colm=crtln.count(',')
                colm2=colm-1
                width.append(colm2)
                crtln=' * ,'+crtln
                #run it through my module see qmk_kc.py
                fixed=replkc(crtln,notdef)
                comb.append(fixed)
                lines=len(comb)
            output_file.write(nl)
            #Output to comment.txt
            print(f'/* {names[layer]}',file=output_file)
            print(f' * ┌{fill*width[0]}──────┐', file=output_file)
            for num in range(0,lines):
                output_file.write(comb[num]+nl)
                if lines>1 and num<(lines-1):
                    print(f' * ├{fill2*width[num]}──────┤', file=output_file)
            print(f' * └{fill3*width[len(width)-1]}──────┘',file=output_file)
            print(' */',file=output_file)
            print('Layer '+str(layer+1)+' done')
            #empty the combined list
            comb=[]
