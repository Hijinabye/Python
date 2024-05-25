#1 
i = 1 
while i <= 9:
    result = 2 * i 
    print(f"2 * {i} = {result}")
    i += 1 

# 이중 while문
i = 1 

while i <= 9:
    num = 1  #  변수를 안에 선언해함 
    while num <= 9: 
        print(f"{i} * {num}= {i * num}")
        num += 1 
    i += 1


# 2 (i, j, k, t ...)

i = 0
while i < 3:
    j = 0 
    while j < 3:
        if j <= i: 
            print("*", end=" ")
        j += 1
    i += 1 
    print() 



# 추가 문제 1
list= [100, 200, 300]
# 리스트의 길이만큼
i =0
while i < len(list): #i가 list 하나하나를 지나간다. 
    print(list[i] + 10) #이렇게만 쓰면 상운이꼴 남
    i += 1 



# 추가 문제 2  
list = ['dog', 'cat', 'parrot']
i = 0 # for문과 다르게 while문은 간격을 주기 않기 때문에 무조건 간격 써줘야함 !
while i < len(list): # len함수는 리스트 안의 요소 뿐 아니라 문자열 안의 개수도 알 수 있음
    print(list[i], len(list[i]))
    i += 1 # 이걸 위에 쓰면 i가 1부터 시작하는 거니까 오류난다. 

# 추가 문제 3
# 코딩에서 =는 변수를 대입하는 거고(대입 연산자), ==는 비교연산자로서 비교하는거
i = 1
# 조건: 1 ~ 30까지 탐색 
while i <= 30:
    if i % 3 == 0:
        print(i)
    # else: pass #else는 굳이 안써도 됨 
    i += 1
