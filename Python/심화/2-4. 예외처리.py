people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

# Ex1
# for person in people:
#     if person['age'] > 20:
#         print (person['name'])
        
# 만약 bobby가 age를 갖고 있지 않다면 데이터가 잘못 들어간 것!!
# 그 때 try except 구문을 이용하여 에러를 넘길 수 있다.

# Ex2
for person in people:
    try:
        if person['age'] > 20:
            print(person['name'])
    except:
        name = person['name']
        print(f'{name} - age 값 null 에러입니다.')