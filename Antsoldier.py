n = int(input())

array = list(map(int,input().split()))

# DP 테이블
d = [0] * 100

# 다이나믹 프로그램 진행 ( bottom up)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n) :
    d[i] = max(d[i-1], d[i-2]+array[i])

# 계산 결과 출력
print(d[n-1])