#[220104:list 02] first commit
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    print(a[n-i-1],end=' ')