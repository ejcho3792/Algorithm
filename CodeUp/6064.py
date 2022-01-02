#[220102:ternary operator 02] first commit
a,b,c=map(int,input().split())
print(int((a if a<b else b) if ((a if a<b else b)<c) else c))