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

# map(함수, 반복가능한 객체)

def check_adult(person):
    if person['age'] > 20:
        return '성인'
    else:
        return '청소년'

result = map(check_adult, people)
print(list(result))

# 2차 조작!

def check_adult(person):
    return "성인" if person['age']>20 else '청소년'
result = map(check_adult, people)
print(list(result))

# 3차 조작!

result = map(lambda x: ("성인" if x['age'] >20 else "청소년"), people)
print(list(result))

result = filter(lambda x: x['age'] > 20, people)
print(list(result))