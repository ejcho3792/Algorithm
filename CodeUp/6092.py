#[220104:list 01] first commit
n=int(input())
a=list(map(int,input().split()))
cnt=[]
for i in range(23):
    cnt.append(0)
for i in range(n):
    cnt[a[i]-1]+=1
for i in range(23):
    print(cnt[i],end=' ')