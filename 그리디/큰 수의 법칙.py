N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
max = 0
max2 = 0
jungbok = 0
sum = 0

for i in arr:
    if i > max:
        max = i

arr.remove(max)

for j in arr:
    if j > max2:
        max2 = j

for i in range(M):
    if jungbok < K:
        sum += max
        jungbok += 1
    else:
        sum += max2
        jungbok = 0

print(sum)

# 정렬을 사용하자!(sort())

# 정답
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k + m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
