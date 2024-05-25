"""
1. 수학에서의 함수 형태 
y = 2x + 3 

2. 일반적인 함수 형태
def 함수_이름(매개 변수):
    수행할_문장1 
    수행할_문장2
    ...
    return result -> 보통 다 리턴함

함수 호출(사용) => 리턴값을 받을 변수 = 함수이름(입력인수1, 입력인수2)

def add(a, b):
    result = a + b 
    return result

함수 호출(사용) => 리턴값을 받을 변수 = 함수이름(입력인수1, 입력인수2)

3. 입력값이 없는 함수 

def say():
    return "Hi"

a = say()
리턴값을 받을 변수 = 함수 이름()

4. 리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))


add(3,4)

5. 입력값이 몇 개가 될지 모를 때(*이 포인트!)
def 함수_이름(*매개 변수):
    수행할_문장
    ...

<여러 개의 입력값을 받는 함수>
def add_many(*args):
    result = 0 
    for i in args:
        result += i
    return result

result = add_many(1, 2, 3)
print(result)

<여러 개의 입력값을 모두 더하는 함수>
def add_many(choice, *args):
    if choice == "add":
        result = 0 
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

# 더하기 
result = add_many("add", 1, 2, 3)
print(result)
# 곱하기 
result = add_many("mul", 1, 2, 3, 4, 5, 6, 7)
print(result)


# 함수 이름 add, 입력으로 2개의 값을 방아서 입력값의 합을 출력

# a, b는 매개변수(파라미터) -> 함수에 입력으로 전달된 값을 받는 변수
def add(a, b):
    return a + b 

a = 3 
b = 4 
# add(3, 4)의 리턴값을 c에 대입 
# a, b는 인수 -> 함수를 호출할때 전달하는 입력값
c = add(a, b)
print(c)

a = ass(3, 4)
print(a) > none이라는 값이 출력 
4번을 보면 리턴값을 쓰지 않은 함수인데 즉, 변수에 아무것도 저장이 되지 않고 그냥 출력만 되었기 때문

"""

n = 50
"""
()()* i =1 
()*** i = 2
***** i = 3
"""
# 위쪽 피라미드 
for i in range(1, n+1):
  print(" " * (n-i) + "*"*(i*2-1))
for j in range(n-1, 0, -1): # 맨끝의 -1로 역순으로 
  print(" "*(n-j) + "*"*(j*2-1))