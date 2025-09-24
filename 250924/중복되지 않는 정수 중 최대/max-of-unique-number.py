# 입력 받기
N = int(input())
arr = list(map(int, input().split()))

# 각 숫자의 등장 횟수 세기
from collections import Counter
count = Counter(arr)

# 등장 횟수가 1인 숫자들만 필터링
unique_numbers = [num for num, cnt in count.items() if cnt == 1]

# 결과 출력
if unique_numbers:
    print(max(unique_numbers))
else:
    print(-1)
