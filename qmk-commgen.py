import QMK_KC
lines=input("How many lines? ")
lines=int(lines)
comb=[]
for num in range(1,(lines+1)):
    kmap=input("Line "+str(num)+"? ")
    kmap=" *,"+kmap
    kmap=kmap.replace(" ","")
    colm=""
    fixed=QMK_KC.repl(kmap)
    comb.append(fixed)
print(comb)
print (len(comb))
