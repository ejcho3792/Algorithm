# coding test with python
---
## INDEX
[Chapter 03. Greedy](#chapter-03-greedy)   
[Chapter 04. Implementation](#chapter-04-implementation)   
[Chapter 05. DFS/BFS](#chapter-05-dfsbfs)   
[Chapter 06. Sorting](#chapter-06-sorting)   
[]()   
[]()   



---
#### Chapter 03. Greedy   
##### * 그리디 알고리즘 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법   
[ex01) 거스름돈 출력](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0301_change.py)   
잔돈 500원, 100원, 50원, 10원이 무한히 있다.   
손님에게 거슬러 줘야 할 돈이 N원일때, 거슬러 줄 동전의 최소 개수 구하기   
[ex02) 큰 수의 법칙](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0302_sum_number.py)   
N의 크기로 입력받은 배열의 수들을 M번 더하여 가장 큰 수를 만든다.   
특정 인덱스의 수가 연속 K번을 초과할 수 없다.   
[ex03) 숫자 카드 게임](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0303_card_game.py)   
카드가 N*M 형태로 있을 때 뽑고자 하는 카드 행을 선택하고, 해당 행의 카드 중 가장 낮은 숫자를 뽑아야 한다.   
즉 각 행마다 가장 작은 수를 찾은 뒤, 작은 수들 중 최대값을 찾는다.
[ex04) 숫자 나누기](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0304_div_one.py)   
숫자 n이 1이 될때까지   
1 n에서 1을 뺀다   
2 n을 k로 나눈다(나누어 떨어질 때만)   
두 과정중 하나를 최소 횟수로 수행하여 1을 만든다.   

#### Chapter 04. Implementation   
[ex01) 상하좌우](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0401_coordinate.py)   
n*n 공간에서 왼쪽 위의 좌표는 1,1이다.   
1,1에서 시작하여 상, 하, 좌, 우가 입력되며, 공간을 벗어나는 방향은 무시된다. 도착 지점의 좌표를 출력한다.   
[ex02) 시간](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0402_time.py)   
정수 n이 입력되면 0:0:0~n:59:59의 시간 중 3이 포함되는 모든 경우의 수를 구한다.   
[ex03) 체스](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0403_knight.py)   
8*8 체스판의 나이트는 L자 형태로만 이동 가능(수직으로 두칸, 수평으로 한칸 또는 수평으로 두칸, 수직으로 한칸)   
나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력한다.   
[ex04) 게임](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0404_game.py)   
n*m 크기로 구성된 맵이며, 각각의 칸은 육지(0) 또는 바다(1)이다.   
캐릭터는 바다는 갈 수 없다.   
1) 현재 위치에서 바라보고 있는 방향을 기준으로 왼쪽방향부터 시작한다.   
2) 해당 방향에 아직 가지 않은 칸이 있다면 전진한다. 없다면 회전만 하고 다시 1로 돌아간다.   
3) 네 방향 모두 가본 칸 혹은 바다라면, 방향전환 없이 뒤로 한칸 가고 1로 돌아간다.   
이때 뒤쪽 방향이 바다라서 못간다면 움직임을 멈추고 방문한 칸의 수를 출력한다.

#### Chapter 05. DFS/BFS   
[ex01) 스택, 큐, 재귀함수](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0501_stack_queue.py)   
[ex02) DFS/BFS](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0502_dfs_bfs.py)   
[ex03) Ice](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0503_ice.py)   
n*m크기의 얼음틀에 구멍이 뚫려 있는 부분끼리 상하좌우로 붙어있는 경우 연결되어 있는 것으로 간주한다.   
주어진 얼음틀에 생성되는 총 아이스크림의 개수를 구하기   
[ex04) Maze](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0504_maze.py)   
n*m 미로에서 내 위치는 1,1이고, 출구는 n*m이다.   
지나갈 수 있는 칸은 1로 표시되어 있을 때 탈출을 위해 움직여야 하는 최소 칸의 개수를 구하기   

#### Chapter 06. Sorting   
[ex01) 정렬 알고리즘](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0601_sort.py)   
[ex02) 수열 내림차순 정렬](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0602_ascending.py)   
입력될 수의 갯수 n개가 주어지고, n개의 수열이 차례로 입력될 때 내림차순으로 정렬하여 정렬된 결과를 공백으로 구분하여 출력하기   
[ex03) 성적순으로 학생 출력](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0603_student_grade.py)   
n명의 학생이 있고, 학생의 이름과 성적이 입력될 때 성적이 낮은 순서대로 학생의 이름을 출력하기   
[ex04) 두 배열의 원소 교체](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0604_change_ele.py)   
n개의 원소로 구성된 a, b 배열에서 각 배열에서 원소를 하나씩 선택하여 서로 최대 k번 바꿔치기를 수행할 한다. a의 모든 원소의 합이 최대가 되도록 하고 최대값을 출력하기   



