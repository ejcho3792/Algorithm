#[220104:total 07] first commit
r,g,b=map(int,input().split())
num=0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            num+=1
print(num)