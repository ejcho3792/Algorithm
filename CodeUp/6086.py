#[220104:total 10] first commit
n=int(input())
i=1
nsum=0
while True:
    nsum+=i
    i+=1
    if nsum>=n:
        break
print(nsum)