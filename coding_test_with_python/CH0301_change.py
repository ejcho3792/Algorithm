n=int(input())
c=[500,100,50,10]
count=0
for i in c:
    count+=n//i
    n%=i
print(count)
