# 가위바위보 게임 with computer 
# mission 1. 판이 끝나면 "계속 하시겠습니까?" > Y/N 사용자가 선택해서 게임 이어갈지 말지 정하기 
# mission 2. 승, 무, 패 

print("👧🧑 === 가위바위보 게임 with computer === ✌✊✋")

list = ["가위", "바위", "보"]
win = 0 
lose = 0 
same = 0 
count = 0

# 사용자에게 입력받기 

while True:
    user = input("가위, 바위, 보 중 하나만 입력하세요.")
    if user not in list: 
        print(" 아니 가위, 바위, 보 중 하나만 입력하시라구요 ^_^")
        continue
    else: break

# 컴퓨터 랜덤 뽑기 
import random
cpmouter = random.choice(list)
print(f"computer은 {computer}를 냈네요 👨")

# 승부 가리기 
# + 승부 세기 

if user == computer: 
    print("비겼습니다.")
    same += 1 
elif (user == "주먹" and computer == "가위") or\
    (user == "가위" and computer == "보") or\
    (user == "보" and computer == "주먹"): 
    print("이겼습니다 !!")
    win += 1 
else: 
    print("졌습니다 ㅠㅠ")
    lose += 1 

# 게임을 계속 하시겠습니까?

answer = ["Y", "y", "N", "n"]
while True: 
    keep_going = input("게임을 계속 하시겠습니까? (Y/N)")
    if keep_going == Y or keep_going == y:
        count += 1 
        print(f"{count}회차, 게임을 다시 시작합니다.")
        continue
    elif ckeep_going not in answer: 
        print("입력값을 잘못입력하셨습니다.")
        continue
    else:
        print("게임을 종료합니다.")
        exit()