# 내 코드(틀림)
'''
# 입력받기
N, M = map(int, input().split())
A, B, d = map(int, input().split())
earth = [list(map(int, input().split())) for i in range(N)]

move = [(-1,0), (0, 1), (1, 0), (0, -1)]
cnt = 1
direction = 1


while direction != 5:
    earth[A][B] = 1
    # 반시계 방향으로 90도 회전
    d -= 1
    if d < 0:
        d = 3
    # 이동했을 때 0(가보지 않은 칸)이라면
    if earth[A + move[d][0]][B + move[d][1]] == 0:
        earth[A + move[d][0]][B + move[d][1]] = 2
        A += move[d][0]
        B += move[d][1]
        cnt += 1
        direction = 1
    # 1이라면
    else:
        direction += 1
        
if earth[A - move[d][0]][B - move[d][1]] != 1:
    A -= move[d][0]
    B -= move[d][1]
    
print(cnt)

'''

#GPT로 수정(종료조건 수정)
# 입력받기
N, M = map(int, input().split())
A, B, d = map(int, input().split())
earth = [list(map(int, input().split())) for _ in range(N)]

# 방향 (북, 동, 남, 서)
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 시작 위치 방문 처리
cnt = 1
earth[A][B] = 2  # 방문 표시
direction = 0  # 회전 횟수

while True:
    # 반시계 방향으로 회전
    d = (d - 1) % 4
    nx, ny = A + move[d][0], B + move[d][1]

    # 이동할 수 있는 경우 (미방문 지역)
    if 0 <= nx < N and 0 <= ny < M and earth[nx][ny] == 0:
        earth[nx][ny] = 2  # 방문 처리
        A, B = nx, ny
        cnt += 1
        direction = 0  # 다시 회전 횟수 초기화
        continue

    # 이동할 수 없다면 회전 횟수 증가
    direction += 1

    # 네 방향 모두 갈 수 없는 경우 → 후진
    if direction == 4:
        nx, ny = A - move[d][0], B - move[d][1]
        
        # 뒤가 바다(1)라면 종료
        if nx < 0 or nx >= N or ny < 0 or ny >= M or earth[nx][ny] == 1:
            break
        
        A, B = nx, ny  # 후진 수행
        direction = 0  # 회전 횟수 초기화

print(cnt)
