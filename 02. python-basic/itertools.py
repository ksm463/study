import itertools

a = [1, 3, 5]

# 조합
print([*itertools.combinations(a, 2)])
# 중복 조합
print([*itertools.combinations_with_replacement(a, 2)])
# 순열
print([*itertools.permutations(a, 2)])
# 모든 순서쌍
print([*itertools.product(a, a)])
# 원소가 n개인 모든 순서쌍
print([*itertools.product(a, repeat=3)])
