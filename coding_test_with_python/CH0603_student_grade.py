n=int(input())
arr=[]

for i in range(n):
    d=input().split()
    arr.append((d[0],int(d[1])))

arr=sorted(arr,key=lambda student:student[1])

for s in arr:
    print(s[0],end=' ')