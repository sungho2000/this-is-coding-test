# 나의 풀이
'''
N = int(input())
T = 0
cnt = 0

for i in range(N*10000 + 6000):
    T += 1
    if "3" in str(T) :
        cnt += 1
    if 2 <= len(str(T)) < 4 and str(T)[-2] > "5" and "3" in str(T):
        cnt -= 1
    if len(str(T)) >= 4 and ((str(T)[-2] > "5") or (str(T)[-4] > "5")) and "3" in str(T):
        cnt -= 1
        
print(cnt)
'''

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
