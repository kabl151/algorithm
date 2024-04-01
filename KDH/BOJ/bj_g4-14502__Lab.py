import sys
from collections import deque
# sys.stdin = open('./bj_g4-14502__Lab__input.txt', 'r')

input = sys.stdin.readline
print = sys.stdout.write

FORBID = -1
VIRUS = 2
WALL = 1
PATH = 0


def bfs():
    new_table = [table[i][:] for i in range(N+2)]
    q = deque(virus_pos)
    cnt = 0

    while q:
        cur_x, cur_y = q.popleft()
        for move_x, move_y in moves:
            next_x, next_y = cur_x + move_x, cur_y + move_y
            if new_table[next_x][next_y] == PATH:
                new_table[next_x][next_y] = VIRUS
                q.append((next_x, next_y))

    for i in range(1, N+1):
        for j in range(1, M+1):
            if new_table[i][j] == PATH:
                cnt += 1

    return cnt


def set_wall(cnt=0, start=0):
    global max_v
    if cnt == 3:
        max_v = max(max_v, bfs())
        return

    for k in range(start, len(path_pos)):
        i, j = path_pos[k]
        table[i][j] = 1
        set_wall(cnt + 1, k + 1)
        table[i][j] = 0


N, M = map(int, input().split())
table = [[-1] * (M + 2)]
table += [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)]
table += [[-1] * (M + 2)]

path_pos = []
virus_pos = []
for r in range(1, N+1):
    for c in range(1, M+1):
        if table[r][c] == VIRUS:
            virus_pos.append((r, c))
        elif table[r][c] == PATH:
            path_pos.append((r, c))


moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
max_v = 0

set_wall()

print(f'{max_v}')

# sys.stdin.close()