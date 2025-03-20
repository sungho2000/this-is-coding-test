N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

while A[0] < B[-1] and K > 0:
    A[0], B[-1] = B[-1], A[0]
    A.sort()
    B.sort()
    K -= 1

sum = 0
for i in A:
    sum += i

print(sum)

# 정답
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
