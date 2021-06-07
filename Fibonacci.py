# 100 까지의 리스트 초기화
d = [0] * 100

def pibo(x):
    print('f('+ str(x) + ')', end=" ")
    if x== 1 or x== 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)

    return d[x]

pibo(6)

# 출력결과
# f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)