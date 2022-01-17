############################
# 스택                      #
############################
## 선입후출 구조
# in(5) - in(2) - in(3) - in(7) - out() - in(1) - in(4) - out()

stack=[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()     # 7이 제거
stack.append(1)
stack.append(4)
stack.pop()    # 4가 제거

print(stack)
print(stack[::-1])

############################
# 큐                       #
############################
# 선입선출 구조
# in(5) - in(2) - in(3) - in(7) - out() - in(1) - in(4) - out()

from collections import deque

queue=deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  #5 제거
queue.append(1)
queue.append(4)
queue.popleft()  #2 제거

print(queue)
queue.reverse()
print(queue)

############################
# 재귀 함수                  #
############################
# 자기 자신을 다시 호출하는 함수

def recursive_function(i):
    if i==50:
        return
    print('recursive', i)
    recursive_function(i+1)

recursive_function(1)

# ex. 팩토리얼
def factorial_iterative(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

def factorial_reculsive(n):
    if n<=1:
        return 1
    return n * factorial_iterative(n-1)
print('iterative ', factorial_iterative(5))
print('reculsive ', factorial_reculsive(5))