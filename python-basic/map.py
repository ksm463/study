# 백준 입력시 자주 사용
# map(int, input().split())

a = [1,2,3,4,5]
b = [1,4,9,16,25]

c = list(map(lambda x:x*x, a))
print(c)
print([x*x for x in a])