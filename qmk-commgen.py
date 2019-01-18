import QMK_KC
lines=input("How many lines? ")
lines=int(lines)
comb=[]
fill="-------"
fill2="------+"

nl="\n"
for num in range(1,(lines+1)):
    kmap=input("Line "+str(num)+"? ")
    colm=kmap.count(',')
    colm=colm-1
    kmap=kmap.replace(" ","")
    kmap=" * ,"+kmap
    if kmap.endswith(",")==False:
        kmap=kmap+","
    fixed=QMK_KC.repl(kmap)
    comb.append(fixed)
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
file.close()
