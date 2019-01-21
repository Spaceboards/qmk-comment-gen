import QMK_KC
comb=[]
fill="-------"
fill2="------+"
yes=0
layers=0
kclay=[]
kclns=[]
nl="\n"
inpt=open("keymap.c","r")
allin=inpt.readlines()
#add all lines of keymap to allin var
inpt.close()
file=open("comment.txt","w+")

for line in allin:
    line=line.replace(" ","")
    line=line.replace("\n","")
    if line.count(")")==1 and yes>0:
        #if it is the end of a Map
        yes=0
        kclay.append(kclns)
        kclns=[]
        layers+=1
    elif yes>0:
        #if it part of keymap add it to KC lines
        kclns.append(line)
    elif line.count("LAYOUT")==1:
        yes=1
lyrcount=layers
for layer in range(0,len(kclay)):
    lyrcount-=1
    for num in range(0,len(kclay[layer])):
        crtln=(kclay[layer][num])
        if crtln.endswith(",")==False:
            crtln=crtln+","
        colm=crtln.count(',')
        crtln=" * ,"+crtln
        fixed=QMK_KC.repl(crtln)
        comb.append(fixed)
        lines=len(comb)
    file.write(nl)
    file.write("/*"+nl)
    colm2=colm-1
    file.write(" * ,------"+(fill*colm2)+"."+nl)
    for num in range(0,lines):
        file.write(comb[num]+nl)
        if lines>1 and num<(lines-1):
            file.write(" * |"+(fill2*colm2)+"------|"+nl)
    file.write(" * `------"+(fill*colm2)+"'"+nl)
    file.write(" */"+nl)
    print("Layer "+str(layer+1)+" done!")
    comb=[]

file.close()
