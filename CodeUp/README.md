# CodeUp Python 기초 100제   [(Link)](https://codeup.kr/problemsetsol.php?psid=33)
---
### * 해당 문제 번호로 .py 파일 생성할 것
### * 기억해둬야 할 부분은 문제 번호와 함께 적어 놓기

# 1. File input, output   
### input() : str 형식으로 입력받음   
### input().split() : 공백으로 구분된 여러 값 입력 받음   
### split() : 괄호에 다양한 구분자 입력 가능 (ex. ':', '.','-')   

# 2. dtype   
### int(num, 16) : num을 16진수로 변환   
### print( '%o' % int(num) ) : num에 대한 8진수 출력   

# 3. bit shift
### print( num << 1 ) : num의 2배 수 출력
### print( num << 2 ) : num의 4배 수 출력
### print( num >> 1 ) : num의 1/2배 수 출력
### print( num >> 2 ) : num의 1/4배 수 출력

# 4. Comparison 비교연산자 
### print( 10 < 20 ) : True 출력
### print( 10 > 20 ) : False 출력
### print( 10 != 20 ) : True 출력

# 5. logical
### not bool( num ) : num의 bool 값이 False이면 True 출력 
### bool(A and B) : A와 B가 모두 True여야만 True로 계산
### bool(A or B) : A와 B 중 하나만 True이면 True로 계산

# 6. bitwise (비트단위 연산)
### ~ (tilde : bitwise not) : 참/거짓을 바꿔줌 (정수 n일때, ~n= -n-1)
### & (ampersand : bitwise and) : n & m 두 비트열 모두 1인 부분의 자리만 1로 변경
### | (vertical bar : bitwise or) : n | m 비트열에서 하나라도 1인 자리는 1로 변경
### ^ (circumflex : bitwise xor) : 배타적 논리합. 서로 다른 부분만 1로 변경

# 7. Ternary operator
### 'x if C else y' 형태. 
##### C : conditional expression(조건식) 혹은 값
##### x : C의 결과가 True일 때 사용할 값
##### y : C의 결과가 True가 아닐 때 사용할 값