#1 슬라이싱을 이용해 nums 리스트에서 홀수만 출력(while반복문)
i = 1 
#슬라이싱을 이용한 풀이
print(nums[::2])


while i <= 10:
    if i % 2 != 0:
        print(i)

    i = i + 1 

#2 
# string = "삼성전자/LG전자/Naver"
# print("삼성전자","LG전자", "Naver", sep = ",")

interest = string.split('/')
print(interest)

#3
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)


#4
print(int("2020")) #year = int("2020") 이렇게 변수로 정장해도 됨. 
print(int("2020")-1)
print(int("2020")-2)

#5 띄어쓰기
string = "국어 영어 수학 과학 경제 지리 물리 화학 생물"
print(string[0:2]) #국어
print(string[3:5]) #영어
print(string[6:8]) #수학

print(string.replace("", "\n"))
print("국어\n 영어\n 수학\n 과학\n 경제\n 지리\n 물리\n 화학\n 생물")

#6 문자열의 길이
string = "pneumonoultramicroscopicsilicovolcanoconiosis"
print(len(string))

#7 리스트의 평균 
nums = [1, 2, 3, 4, 5]
average = sum(nums)/len(nums)
print(average)

#8 뒤에 4자리만 출력 
license_plate = "24가 2210"
print(license_plate[4:])

#9
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest = string.split(',')
print(interest)