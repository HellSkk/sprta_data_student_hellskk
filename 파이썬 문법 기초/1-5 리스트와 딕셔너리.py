# 리스트 순서가 있는, 다른 자료형들의 모임!
# 리스트의 길이도 len() 함수를 통해 알 수 다
# 순서가 있어서 인덱싱과 슬라이싱을 사용할 수 있다
# 리스트의 요소가 리스트라면 중첩해서 불러온다
a = [1, 2,[2, 3], 0]
print(a[2])
print(a[2][0])

# 덧붙이기
a = [1, 2, 3]
a.append(5)
print(a)

a.append([1, 2])
print(a)

# 더하기 연산으로 추가하기
a += [2, 7]
print(a)

# 정렬하기
a = [2, 5, 3]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 요소가 리스트 안에 있는지 알아보기
a = [2, 1, 4, "2", 6]
print(1 in a)       # True
print("1" in a)     # False
print(0 not in a)   # True


####################### 딕셔너리
# 키와 밸류의 쌍으로 이루어진 자료의 모임
person = {"name":"Bob", "age": 21}
print(person["name"])

# 딕셔너리를 만드는 방법
a = {"one":1, "two":2}

# 빈 딕셔너리 만들기
a = {}
a = dict()

# 딕셔너리의 요소에는 순서가 없어 인덱싱을 사용할 수 없다.
# 딕셔너리의 값을 업데이트하거나 새로운 쌍의 자료를 넣을 수 있다
person = {"name":"Bob", "age": 21}

person["name"] = "Robert"
print(person)

person["height"] = 174.8
print(person)

# 딕셔너리의 밸류로는 아무 자료형이나 쓸 수 있다. 다른 딕셔너리도 넣을 수 있다!
# 딕셔너리 안에 해당 키가 존재하는지 알고 싶을 때 in 을 사용
person = {"name":"Bob", "age": 21}
print("name" in person)     # True
print("email" in person)    # False
print("phone" in person)    # False

# 리스트와 딕셔너리의 조합
people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}]

# people[0]['name']의 값은? 'bob'
# people[1]['name']의 값은? 'carry'

person = {'name': 'john', 'age': 7}
people.append(person)

# people의 값은? [{'name':'bob','age':20}, {'name':'carry','age':38}, {'name':'john','age':7}]
# people[2]['name']의 값은? 'john'


# Q 딕셔너리 퀴즈
people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]
print(people[2]["score"]["science"])