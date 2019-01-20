import QMK_KC
comb=[]
fill="-------"
fill2="------+"
counter=0
yes=0
ndnl=[]
nl="\n"
inpt=open("keymap.c","r")
allin=inpt.readlines()
inpt.close()
for line in allin:
    counter+=1
    line=line.replace(" ","")
    line=line.replace("\n","")
    if line.count(")")>=1:
        yes=0
    elif yes>0:
        ndnl.append(counter-1)
    elif line.count("LAYOUT")==1:
        yes=counter
for num in ndnl:
    allin[num]=allin[num].replace(" ","")
    allin[num]=allin[num].replace("\n","")
    if allin[num].endswith(",")==False:
        allin[num]=allin[num]+","
    colm=allin[num].count(',')
    colm=colm-1
    allin[num]=" * ,"+allin[num]
    fixed=QMK_KC.repl(allin[num])
    fixed=fixed.replace(",","|")
    fixed=fixed.replace("*,","*|")
    fixed=fixed.replace("REPLACE|",",")
    comb.append(fixed)
lines=len(comb)
file=open("comment.txt","w+")
file.write("/*"+nl)
file.write(" * ,------"+(fill*colm)+"."+nl)
for index in range(0,lines):
    col2=colm-1
    file.write(comb[index]+nl)
    if index>=0 and index<(lines-1) and lines>1:
        file.write(" * |"+(fill2*colm)+"------|"+nl)
file.write(" * `------"+(fill*colm)+"'"+nl)
file.write(" */")
print("DONE")
file.close()
