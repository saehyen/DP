# 화폐 구성
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행(bottom up)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001 :
            d[j]= min(d[j],d[j- array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])