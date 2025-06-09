# for 문
fruits = ["사과", "배", "감", "귤"]

for fruit in fruits:
    print(fruit)

# Q. 사람의 나이 출력하기

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    if person["age"] > 20:
        print(person["name"]) # 정답!
        
# enumerate, break
fruits = ['사과', '배', '감', '귤','귤','수박','참외','감자','배','홍시','참외','오렌지']

for i, fruit in enumerate(fruits):
    print(i, fruit)
    
# for index, value in enumerate(리스트):
    # index: 현재 인덱스
    # value: 해당 인덱스의 값

# 앞에 5개만 출력해보고 싶다면?
for i, fruit in enumerate(fruits):
    print(i, fruit)
    if i == 4:
        break;
    
    
# Q. 리스트에서 짝수만 출력하는 함수 만들기
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

for num in num_list:
    if (num % 2) == 0:
        print(num)
# 정답!
      
# Q. 리스트에서 짝수의 개수를 출력하기
result = 0
for num in num_list:
    if (num % 2) == 0:
        result += 1

print( result , "개")
# 정답!

# Q. 리스트 안에 있는 모든 숫자 더하기
result = 0
for num in num_list:
    result += num
print("정답:",result)

# Q. 리스트 안에 있는 자연수 중 가장 큰 숫자 구하기

max = 0;
for num in num_list:
    if max < num:
        max = num
print(max)