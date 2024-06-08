
# 가위바위보 게임 만들기
# 컴퓨터 랜덤
import random
win = 0 
lose = 0 
same = 0 

list = ["가위", "바위", "보"]

while True: 
    user = input("가위, 바위, 보 중 하나를 입력하세요: ")
    # 가위, 바위, 보 맞는지 확인 
    if user not in list: 
        print("다시 입력하세요.")
        continue

    # 리스트의 요소를 추출하는 함수는 chice와 sample이 있음.
    # chice는 한가지 요소만 추출하는 것.
    computer = random.choice(list)
    print(computer)

    if user == computer: 
        print("비김")
        same += 1
    # 이겼을때 
    # user: 가위, 상대: 보 / user: 바위, 상태: 가위 / 나: 보, 상대: 바위
    elif (user == "가위" and computer == "보")or \
        (user == "바위" and computer == "가위")or \
        (user == "보" and computer == "바위"): 
        print("이김")
        win += 1
    else: 
        print("짐")
        lose += 1


    while True: 
        # 게임을 계속하시겠습니까? (Y/N): Y
        restart =input("게임을 계속 하시겠습니까?")

        if restart == "Y": 
            break
        elif restart == "N":
            print("가위바위보 게임을 종료합니다.")
            print(f"승{win}번, 패{lose}번, 무승부{same}번")
            exit()
        else:
            print("잘못된 입력입니다. Y 또는 N을 입력해주세요.")

            
"""   

# 2 

N = int(input("정수를 입력하세요.: ")) # 개수 

# function -> 각 요소에 적용할 함수
# iterable -> 함수를 적용할 데이터 집합 
# map(function, iterable)
N_list = list(map(int,input().split())) # 그 안에 있는 숫자들 # 공백을 기준으로 입력받는 것을 int정수 형태로 저장하겠다. 
V = int(input()) # 
count = 0 

for i in range(0, N):
    if N_list[i] == V:
        count += 1 
print(f"{count}개 입니다.")

# while문으로 풀어보기 숙제 !!





# """
# map(a, b)
# a -> 각 요소에 적용할 함수 
# b -> 함수를 적용할 데이터 집합

# map(int, input().split()) -> 다 정수형으로 바꿈 
# int를 input().split()에 다 적용 
# """