n,m=map(int, input().split())
a,b,direction=map(int,input().split())

d=[[0]*m for _ in range(n)]
d[a][b]=1

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

# 북, 동, 남, 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

count=1
turn_time=0

while True:
    turn_left()
    nx=a+dx[direction]
    ny=b+dy[direction]
    if d[nx][ny]==0 and arr[nx][ny]==0:
        d[nx][ny]=1
        a=nx
        b=ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1

    if turn_time==4:
        nx=a-dx[direction]
        ny=b-dy[direction]
        if arr[nx][ny]==0:
            a=nx
            b=ny
        else:
            break
        turn_time=0

print(count)
