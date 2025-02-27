# 나의 풀이
night = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # alpha 리스트를 사용하지 말고 117p 정답처럼 하면 빠르게 연산 가능(ord함수사용)
location = [alpha.index(night[0])+1 ,int(night[1])]
cnt = 0

cases = [[-2, 1], [-2, -1], [1, 2], [-1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]

for i in range(8):
    if 1 <= location[0] + cases[i][0] <= 8 and 1 <= location[1] + cases[i][1] <= 8:
        cnt += 1

print(cnt)
