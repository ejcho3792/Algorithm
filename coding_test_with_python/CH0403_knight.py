knight=input()
row,col=int(knight[1]),int(ord(knight[0])-96)
rts=[(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]
res=0
for rt in rts:
    n_row=row+rt[1]
    n_col=col+rt[0]
    if 0<n_row<9 and 0<n_col<9:
        res+=1
print(res)