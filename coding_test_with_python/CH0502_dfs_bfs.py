
# 1. 인접행렬 : 각 노드가 연결된 형태를 기록
INF=999999999
graph=[[0,7,5],
       [7,0,INF],
       [5,INF,0]]

# 2. 인접리스트 : 모든 노드에 연결된 노드에 대한 정보를 연결하여 저장
graph=[[] for _ in range(3)]
# 노드 0에 연결된 노드정보 저장 (노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))
print(graph)

############################
# DFS                      #
############################
# 깊이 우선 탐색
def dfs(graph,v,visited):
       visited[v]=True
       print(v,end=' ')
       for i in graph[v]:
              if not visited[i]:
                     dfs(graph,i,visited)
graph=[[],
       [2,3,8],
       [1,7],
       [1,4,5],
       [3,5],
       [3,4],
       [7],
       [2,6,8],
       [1,7]]
visited=[False]*9
dfs(graph,1,visited)

############################
# BFS                      #
############################
# 너비 우선 탐색

from collections import deque

def bfs(graph,start,visited):
       queue=deque([start])
       visited[start]=True
       while queue:
              v=queue.popleft()
              print(v,end=' ')
              for i in graph[v]:
                     if not visited[i]:
                            queue.append(i)
                            visited[i]=True
graph=[[],
       [2,3,8],
       [1,7],
       [1,4,5],
       [3,5],
       [3,4],
       [7],
       [2,6,8],
       [1,7]]
visited=[False]*9
bfs(graph,1,visited)