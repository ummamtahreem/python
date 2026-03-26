rno=[]
mks=[]
for a in range(4):
    r,m=eval(input("Enter Roll no:, marks:"))
    rno.append(r)
    mks.append(m)
    
d={rno[0]:mks[0],rno[1]:mks[1],rno[2]:mks[2],rno[3]:mks[3]}
if d[2]>75 :
    print("roll no. 2 scored",d[2],"(>75)")
else:
    print("roll no 2 scored",d[2],"(<75)")
    print("created dictionary")
print(d)