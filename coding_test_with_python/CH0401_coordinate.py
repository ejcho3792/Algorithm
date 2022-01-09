n=int(input())
moves=input().split()
x,y=1,1
# 상, 하, 좌, 우
di=['U','D','L','R']
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for move in moves:
    for i in range(len(di)):
        if move==di[i] and 0<(x+dx[i])<=n and 0<(x+dy[i])<=n:
            x+=dx[i]
            y+=dy[i]
print(x,y)
