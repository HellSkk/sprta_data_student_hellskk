scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}    
]

# ex1
for s in scores:
    name =s["name"]
    score = str(s['score'])
    print(name, score)
    
# ex2
for s in scores:
    name = s["name"]
    score = str(s['score'])
    print(name+'는 ' +score+'점 입니다.')

# ex3
for s in scores:
    name = s['name']
    score = str(s['score'])
    print(f'{name}은 {score}점입니다.')
        