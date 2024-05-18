#1 
i = int(input("숫자를 입력하세요.:"))

if i % 2 == 0: 
    print("짝수")
else:
    print("홀수")

#2
score = int(input("점수를 입력하세요.: "))

if score > 80 and score <= 100:
    grade = "A"
elif 60 < score <= 80:
    grade = "B"
elif 40 < score <=60:
    grade = "C"
elif 20 < score <= 40:
    grade = "D"
else:
    grade = "E"

print("grade is {}".format(grade)) # 피라미터 넣을 곳 즉 , 중괄호를 안했음.

#3 
i = int(input("숫자를 입력하세요.: "))

if i <= 255:
    print(i + 20)
else:
    print(255)


#4 
phone_number = int(input("휴대폰 번호를 입력하세요.: ")) #sep ="-"
front_phone_number = phone_number.spit(-)

if front_phone_number[0:2] == 011:
    print("skt사용자 입니다.")
elif front_phone_number[0:2] == 016:
    print("kt 사용자 입니다.")
elif front_phone_number[0:2] == 019:
    print("lgu 사용자 입니다.")
else: print("알 수 없음")

#5
 print ((3 == 3) and (4 != 3)) = true
