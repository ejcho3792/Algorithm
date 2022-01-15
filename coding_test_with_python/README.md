# coding test with python
---
## INDEX
[Chapter 03. Greedy](#chapter-03-greedy)   
[Chapter 04. Implementation](#chapter-04-implementation)   
[]
[]
[]
[]

---
#### Chapter 03. Greedy   
##### * 그리디 알고리즘 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법   
[ex01) 거스름돈 출력](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0301_change.py)   
잔돈 500원, 100원, 50원, 10원이 무한히 있다. 손님에게 거슬러 줘야 할 돈이 N원일때 거슬러 줄 동전의 최소 개수 구하기   
[ex02) 큰 수의 법칙](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0302_sum_number.py)   
N의 크기로 입력받은 배열의 수들을 M번 더하여 가장 큰 수를 만든다. 특정 인덱스의 수가 연속 K번을 초과할 수 없다.   
[ex03) 숫자 카드 게임](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0303_card_game.py)   
카드가 N*M 형태로 있을 때 뽑고자 하는 카드 행을 선택하고, 해당 행의 카드 중 가장 낮은 숫자를 뽑아야 한다. 즉 각 행마다 가장 작은 수를 찾은 뒤, 작은 수들 중 최대값을 찾는다.
[ex04) 숫자 나누기](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0304_div_one.py)   
숫자 n이 1이 될때까지 1. n에서 1을 뺀다 2. n을 k로 나눈다(나누어 떨어질 때만) 두 과정중 하나를 최소 횟수로 수행하여 1을 만든다.   

#### Chapter 04. Implementation   
[ex01) 상하좌우](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0401_coordinate.py)   
n*n 공간에서 왼쪽 위의 좌표는 1,1이다. 1,1에서 시작하여 상, 하, 좌, 우가 입력되며, 공간을 벗어나는 방향은 무시된다. 도착 지점의 좌표를 출력한다.   
[ex02) 시간](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0402_time.py)   
정수 n이 입력되면 0:0:0~n:59:59의 시간 중 3이 포함되는 모든 경우의 수를 구한다.   
[ex03) 체스](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0403_knight.py)   
8*8 체스판의 나이트는 L자 형태로만 이동 가능(수직으로 두칸, 수평으로 한칸 또는 수평으로 두칸, 수직으로 한칸) 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력한다.   
[ex04) 게임](https://github.com/ejcho3792/Algorithm/blob/master/coding_test_with_python/CH0404_game.py)   
n*m 크기로 구성된 맵이며, 각각의 칸은 육지(0) 또는 바다(1)이다. 캐릭터는 바다는 갈 수 없다. 1) 현재 위치에서 바라보고 있는 방향을 기준으로 왼쪽방향부터 시작한다. 2) 해당 방향에 아직 가지 않은 칸이 있다면 전진한다. 없다면 회전만 하고 다시 1로 돌아간다. 3) 네 방향 모두 가본 칸 혹은 바다라면, 방향전환 없이 뒤로 한칸 가고 1로 돌아간다. 이때 뒤쪽 방향이 바다라서 못간다면 움직임을 멈추고 방문한 칸의 수를 출력한다.




