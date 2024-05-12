
d = {} # 딕셔너리

d['left'] = '왼쪽'
d['3'] = 5
d['555'] = 1243

# 숫자 범위는 크지만, 자료 갯수는 많지 않을 때
# 1000 : 10000

# 문자열에 이것저것 대응될 때
d = {1:'a', 2:'b', 3:'c'}
print(d)
# {1: 'a', 2: 'b', 3: 'c'}

for k, v in d.items():
    print(k, v)
# 1 a
# 2 b
# 3 c

# 딕셔너리 안에 key값이 존재하는 지 찾기
print('a' in d.values())
# True

# key값 찾기
if 3 in d:
    print(d[3])
# c