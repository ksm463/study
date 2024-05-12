import bisect
import random

# 이분 탐색
# 정렬된 배열에서 X찾기. logN개반을 탐색해서 찾을 수 있음.

a = [random.randint(0, 100) for _ in range(10)]

print(a)
print(bisect.bisect_left(a, 10) == 10)
# [86, 79, 4, 51, 83, 65, 45, 24, 5, 21]
# False