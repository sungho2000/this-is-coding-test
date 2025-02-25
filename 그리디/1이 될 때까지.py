'''
N, K = map(int, input().split())
cnt = 0

while N != 1:
    if N % K == 0:
        N //= K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)
'''

#정답 102p
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
    
result += (n - 1)
print(result)
