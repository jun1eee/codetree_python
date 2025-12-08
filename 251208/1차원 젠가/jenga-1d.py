n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# 첫 번째 제거
for i in range(s1 - 1, e1):
    blocks[i] = -1

# 남은 블록만 추출
remain = [b for b in blocks if b != -1]

# 두 번째 제거 (remain 리스트 기준)
remain = remain[:s2 - 1] + remain[e2:]

# 출력
print(len(remain))
for v in remain:
    print(v)

# import sys

# input = sys.stdin.readline

# # 처음 블록 개수
# N = int(input().strip())

# # 위에서부터 아래까지 블록에 적힌 숫자
# blocks = [int(input().strip()) for _ in range(N)]

# # 첫 번째로 제거할 구간 (1-indexed)
# s1, e1 = map(int, input().split())
# # 두 번째로 제거할 구간 (첫 번째 제거 이후 상태 기준, 1-indexed)
# s2, e2 = map(int, input().split())

# # 첫 번째 제거: 0-indexed로 바꿔서 슬라이싱 삭제
# del blocks[s1 - 1:e1]

# # 두 번째 제거: 첫 제거 이후의 리스트 기준으로 다시 삭제
# del blocks[s2 - 1:e2]

# # 결과 출력
# print(len(blocks))
# for x in blocks:
#     print(x)
