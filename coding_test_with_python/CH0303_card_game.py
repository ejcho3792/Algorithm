n,m=map(int, input().split())
res=0
for i in range(n):
    lst=map(int,input().split())
    min_v=min(lst)
    res=max(res,min_v)
print(res)