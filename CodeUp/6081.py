#[220104:total 05] first commit
n = int(input(), 16)
for i in range(1, 16):
    print("%X*%X=%X" % (n, i, n * i))