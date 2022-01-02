#[220101:logical 05] first commit
c,d=input().split()
c = bool(int(c))
d = bool(int(d))
print((c and (not d)) or ((not c) and d))