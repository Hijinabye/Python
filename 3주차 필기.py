# 반복문(2)
"""
while 조건문:
    수행할 문장1 
    수행할 문장2
    수행할 문장3 
    ...
"""
# 조건문이 참인 동안 계속 반복! 

# "10번 찍어 안넘어가는 나무 없다."

# treeHit = 0

# while treeHit < 10:
#     treeHit = treeHit + 1 # treeHit이 9번일 경우: 9 + 1 
#     print("나무를 %d번 찍었습니다." %treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")
# while문 안에 if문을 넣어서 많이 씀! 


# while문 안에서 숫자 입력 
# 입력받은 숫자가 3이면 while문 중지

# num = 0

# while num != 3:
#     print("숫자 입력")
#     num = int(input())

# while문 강제로 빠져나가기
# 커피 자판기 

# 남은 커피 양 
coffee = 10
# money = 300



# # 이건 계속 반복 : 조건문을 걸어줘야함 ! 
# while money:

# while True:
#     money = int(input("돈을 넣어주세요.: "))

#     if money == 300:
#         print("커피를 준다.")
#         coffee = coffee - 1 
#         print("남은 커피의 양은 %d개" %coffee) 
#     elif money > 300:
#         coffee = coffee - 1 
#         print("카스름돈 %d를 주고 커피를 줍니다." % (money - 300))
#         print("남은 커피의 양은 %d개" %coffee) 
#     else: 
#         print("돈을 다시 돌려주고 커피를 주지 않는다.")
#         print("남은 커피의 양은 %d개" %coffee) 

#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매 중지")
#         break



    # coffee = coffee - 1
    # print("남은 커피의 양은 %d개 입니다." % coffee)

    # if coffee == 0:
    #     print("커피가 다 떨어졌습니다. 판매 중지")
    #     break # <- while문을 빠져나가겠다는 의미





    # while문 처음으로 돌아가기 
    # 1 ~ 10까지 수 중에 홀수만 출력하기 

a = 0 
while a < 10:
    a = a + 1 # for문은 a를 증가시킬 필요가 없지만 while은 이런 식을 작성해줘야 함. 
    if a % 2 == 0: continue #아무것도 출력되지 않고 그냥 while문으로 돌아간다.
    print(a)