for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    origianl_oselo = [[0] * (N) for _ in range(N)]

    dr_l = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    #        왼쪽위      위      오른위     오른    오른아래   아래   왼쪽아래    왼쪽
    origianl_oselo[N // 2][N // 2] = 2
    origianl_oselo[N // 2 - 1][N // 2] = 1
    origianl_oselo[N // 2][N // 2 - 1] = 1
    origianl_oselo[N // 2 - 1][N // 2 - 1] = 2

    for i in range(M):
        origianl_oselo[data[i][1]-1][data[i][0]-1] = data[i][2]
        if data[i][2] == 1:
            for j in range(1, N):
                for k in range(8):
                    if 0 <= data[i][1] - 1 + (dr_l[k][0] * j) < N and 0 <= data[i][0] - 1 + (dr_l[k][1] * j) < N:
                        if origianl_oselo[data[i][1] - 1 + (dr_l[k][0] * j)][data[i][0] - 1 + (dr_l[k][1] * j)] == 1:
                            for l in range(1, j):
                                if origianl_oselo[data[i][1] - 1 + (dr_l[k][0] * l)][data[i][0] - 1 + (dr_l[k][1] * l)] == 2:
                                    pass
                                else:
                                    break
                                for m in range(1, j):
                                    origianl_oselo[data[i][1] - 1 + (dr_l[k][0] * l)][data[i][0] - 1 + (dr_l[k][1] * l)] = 1

        elif data[i][2] == 2:
            for j in range(1, N):
                for k in range(8):
                    if 0 <= data[i][1] - 1 + (dr_l[k][0] * j) < N and 0 <= data[i][0] - 1 + (dr_l[k][1] * j) < N:
                        if origianl_oselo[data[i][1] - 1 + (dr_l[k][0] * j)][data[i][0] - 1 + (dr_l[k][1] * j)] == 2:
                            for l in range(1, j):
                                if origianl_oselo[data[i][1] - 1 + (dr_l[k][0] * l)][data[i][0] - 1 + (dr_l[k][1] * l)] == 1:
                                    pass
                                else:
                                    break
                                for l in range(1, j):
                                    origianl_oselo[data[i][1] - 1 + (dr_l[k][0] * l)][data[i][0] - 1 + (dr_l[k][1] * l)] = 2

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if origianl_oselo[i][j] == 1:
                black += 1
            elif origianl_oselo[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')
