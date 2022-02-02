############################
# 정렬                      #
############################
# 데이터를 특정한 기준에 따라 나열하는 것
# 선택정렬
# 가장 작은 것을 선택하여 맨 앞의 데이터와 바꾸는 과정을 반복
arr=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(arr)):
    min_i=i
    for j in range(i+1,len(arr)):
        if arr[min_i]>arr[j]:
            min_i=j
    arr[i],arr[min_i]=arr[min_i],arr[i]
print(arr)
# 삽입정렬
# 데이터를 확인하여 필요한 경우에만 위치를 바꿈
arr=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
print(arr)
# 퀵 정렬
# 기준 데이터(pivot)를 설정하여 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def qu(arr, start, end):
    if start >= end:
        return
    pivot = start
    l = start + 1
    r = end
    while (l <= r):
        while (l <= end and arr[l] < arr[pivot]):
            l += 1
        while (r > end and arr[r] >= arr[pivot]):
            r -= 1
        if (l > r):
            arr[r], arr[pivot] = arr[pivot], arr[r]
        else:
            arr[l], arr[pivot] = arr[pivot], arr[l]
    qu(arr, start, r - 1)
    qu(arr, r + 1, end)
qu(arr, 0, len(arr) - 1)
print(arr)
# 계수정렬
# 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을때 사용. 매우 빠르게 동작
arr=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
cnt=[0]*(max(arr)+1)
for i in range(len(arr)):
    cnt[arr[i]]+=1
for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i,end=' ')