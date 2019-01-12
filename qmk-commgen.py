rows=int(input("ROWS? "))
colm=int(input("COLM? "))
odd="------"*(colm-1)
odd2="-----+"*(colm-1)

even="|     "*(colm-1)
fh=open("comment.txt","w+")
fh.write("/*"+"\n")
fh.write(" * ,"+odd+"-----."+"\n")
fh.write(" * "+even+"|     |"+"\n")
rows=rows-1
while rows>0:
    fh.write(" * |"+odd2+"-----|"+"\n")
    fh.write(" * "+even+"|     |"+"\n")
    rows=rows-1
fh.write(" * `"+odd+"-----'"+"\n")
fh.write("*/")
fh.close()
print("Done!")
