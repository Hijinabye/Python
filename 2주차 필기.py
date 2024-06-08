# swap: 두 값을 바꾸는것 
a = 3
b = 5

tmp = b # tmp -> 5 / 이 과정없이 
b = a # a = b라고만 쓰면 b값이 없어지고 3이된다. 즉, a, b = 3 
a = tmp 

print(a)
print(b)

# 파이썬에서는 걍  a, b = b, a 로 해줘도 됨.

# 튜플
a = [2, 4, 6, 8] #리스트: 안에서 리스트 다시 못만듦
b = (2, 4, 6, 8) #튜플: 안에서 다시 튜플 생성 가능
c = (1, 2, 4, (1, 2))

print(b[0])
print(b[1:])
print(b + c)
print(b * 2)

# 리스트와의 가장 큰 차이점 : 리스트는 요소 값을 바굴 수 있지만, 튜플은 불가
#b[0] = 0 #2를 0으로 바꿔주세요. -> 오류뜸.

# 조건문: if else문 
"""
    기본 틀
    if 조건문:
        수행할 문장1
        수행할 문장2
        ...
    else:
        수행할 문장1
        수행할 문장2
        ...
"""

'돈이 있으면 택시를 타고 가고, 돈이 없으면 걸어간다.'
money = True
if money: #돈이 있다
    print("택시타기")
else: #돈이 없다
    print("걸어가기")

# 비교 연산자(보통 if의 조건문에 많이 들어감)
x = 3
y = 2 
print(x < y) # False
print(x > y) # True
print(x == y) # False
print(x != y) # True

#만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라.
"""
money = 5000
if money >= 3000:
     print("택시를 타라")
else money < 3000: #else에는 조건문 쓰면 안됨!
     print("걸어가라")
"""

money = 5000
if money >= 3000:
     print("택시를 타라")
else :
     print("걸어가라")

# 논리 연산자
x = True 
y = False 
# and, or, not
# and -> x랑 y가 모두 참이여야 참이다.
# or -> x랑 y가 거짓이면 참이다.
# not -> x가 거짓이면 참이다. 

print(x and y) # False
print(x or y) # True
print(not x) # False 

#만약 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 5000
card = 0 #card = False
if money >= 3000 or card >= 1: #card = Flase라고 쓰면 card라고만 써도 됨(보기보다 똑똑한 상운이)
    print("택시를 타라")
else: 
    print("걸어가라")\
    
#만약 5000원 있으면서 카드가 없으면 택시를 가고, 그렇지 않으면 걸어가라.
money = 5000
card = True #card = 1 
if money >= 3000 and not card:
    print("택시를 타라")
else: 
    print("걸어가라")

# in, not in
# x in 리스트, 튜플 
# x not in 리스트, 튜플 

print(1 in [1, 2, 3]) # True 
print(1 in [1, 2, 3 ]) #True 
print(1 not in {1, 2, 3}) #False 

print('a' in ('a', 'b', 'c')) # True
print('j' not in 'python') # True

# 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.
# pocket이라는 리스트를 만들어서 paper, cellphone, money

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시 타라")
else:
    print("걸어가라")


# 만약 주머니에 돈이 있으면 가만히 있고, 없으면 카드를 꺼내라.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass # 조건문에서 아무것일도 안하게 만들고 싶을때 사용.
else:
    print('카드를 꺼내세요')

# 주머니에 돈이 있으면 택시를 타고 가고, 
# 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 
# 돈은 없고 카드도 없으면 걸어가라. 

pocket = ['paper', 'cellphone', 'money']
card = True 

# elif -> 다중 조건 판단 (else + if) : else와 다르게 이건 조건을 붙일 수 있음
if 'money' in pocket:
    print ("택시 타기")
else: # 주머니에 돈이 없는 상황
    if card: # 주머니에 돈은 없지만 카드는 있음
        print("택시 타기")
    else: # 주머니에 돈도 카드도 없음
        print("걸어 가기")


if 'money' in pocket:
    print("택시 타기")
elif card:
    print("택시 타기")
else:
    print("걸어가기")

# 조건문이 하나일 경우에는 이렇게 이어붙여도 된다. 
if 'money' in pocket:print("택시 타기")
elif card: print("택시 타기")
else:print("걸어가기")

# 성적 프로그램 
# 성적이 90점 이상이면 A등급 
# 80점 이상 90점 미만이면 B등급 
# 70점 이상 80점 미만이면 C등급 
# 70점 미만이면 F등급 

# 성적은 사용자로부터 입력 
grade = int(input(("성적을 입력:"))) #input으로 받는건 무조건 다 문자열로 출력이 된다. 
                             # 그러므로 형변환해야함.
if grade >= 90 : print("A")
elif 90 > grade >= 80 : print("B")
elif 80 > grade >= 70 : print("c")
else : print("F")

# 자료형 중 하나인 딕셔너리(사전) : 다양한 정보를 저장해야할때 
# baseball => 야구 
# {key, value}
# {Key1: Value, Key2: Value, Key3: Value, ...}
dic = {'name': 'Jina', 'phone': '010-3352--8830', 'birth':'2003.02.24'}
print(dic['name'])
print(dic['phone'])

d = {1: 'd'}
#a[key] = value
d[2] = 'b'
print(a) #{1: 'j', 2: 'b'}
d[3] = [1, 2, 3]

d = {1: 'd', 1: 'b'} #이건 안됨 출력이 그냥 무시됨 
print(d)