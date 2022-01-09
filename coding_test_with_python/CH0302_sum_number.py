n,m,k=map(int, input().split())
lst=list(map(int,input().split()))
lst.sort()
res=0
for i in range(m):
    if i%(k+1)==3:
        res+=lst[-2]
    else:
        res+=lst[-1]
print(res)
