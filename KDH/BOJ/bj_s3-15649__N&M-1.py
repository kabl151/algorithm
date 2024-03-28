import sys

sys.stdin = open('./bj_s3-15649__N&M-1__input.txt', 'r')


def subsequence(idx=0, cnt=0):
    if idx > N:
        return

    if cnt == M:
        print(*lst)
        return

    for i in range(N):
        if sequence[i] not in lst:
            lst.append(sequence[i])
            subsequence(i+1, cnt+1)
            lst.pop()


N, M = map(int, input().split())
sequence = [i for i in range(1, N + 1)]
lst = []
# print(N,M)

subsequence()



sys.stdin.close()