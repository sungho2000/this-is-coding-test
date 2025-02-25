N, M = map(int, input().split())
li = []
max1 = 0

for i in range(N):
    li.append(list(map(int, input().split())))

for i in li:
    i.sort()
    #if i[0] > max1:
    #    max1 = i[0]
    # 아래 코드도 가능
    max1 = max(max1, i[0])

print(max1)

