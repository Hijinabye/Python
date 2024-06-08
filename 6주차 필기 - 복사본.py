"""
y = 2x + 3 

def 함수_이름(매개 변수):
    수행할_문장1 
    수행할_문장2
    ...
"""

# 함수 이름 add, 입력으로 2개의 값을 방아서 입력값의 합을 출력
def add(a, b):
    return a + b 

a = 3 
b = 4 
# add(3, 4)의 리턴값을 c에 대입 
c = add(a, b)
print(c)