import sys

# sys.stdin = open('./bj_s1-1991__tree-traversal__input.txt', 'r')

input = sys.stdin.readline
print = sys.stdout.write

NODE = 0
LEFT = 1
RIGHT = 2


def in_order(root=1):
    # if root <= 2 ** N - 1:
    #     if tree[root * 2]:
    #         in_order(root * 2)
    #     print(f'{tree[root]}')
    #     if tree[root * 2 + 1]:
    #         in_order(root * 2 + 1)

    if root <= N:
        if sub_trees[root][LEFT] != '.':
            left_idx = dic[sub_trees[root][LEFT]]
            in_order(left_idx)
        print(f'{sub_trees[root][NODE]}')
        if sub_trees[root][RIGHT] != '.':
            right_idx = dic[sub_trees[root][RIGHT]]
            in_order(right_idx)


def pre_order(root=1, idx=1):
    if root <= N:
        print(f'{sub_trees[root][NODE]}')
        if sub_trees[root][LEFT] != '.':
            left_idx = dic[sub_trees[root][LEFT]]
            pre_order(left_idx)
        if sub_trees[root][RIGHT] != '.':
            right_idx = dic[sub_trees[root][RIGHT]]
            pre_order(right_idx)

    # if root <= 2 ** N - 1:
    #     tree[root] = sub_trees[idx][NODE]
    #     print(f'{tree[root]}')
    #     if sub_trees[idx][LEFT] != '.':
    #         left_idx = dic[sub_trees[idx][LEFT]]
    #         pre_order(root * 2, left_idx)
    #     if root * 2 + 1 <= 2 ** N - 1 and sub_trees[idx][RIGHT] != '.':
    #         right_idx = dic[sub_trees[idx][RIGHT]]
    #         pre_order(root * 2 + 1, right_idx)


def post_order(root=1):
    # if root <= 2 ** N - 1:
    #     if tree[root * 2]:
    #         post_order(root * 2)
    #     if tree[root * 2 + 1]:
    #         post_order(root * 2 + 1)
    #     print(f'{tree[root]}')

    if root <= N:
        if sub_trees[root][LEFT] != '.':
            left_idx = dic[sub_trees[root][LEFT]]
            post_order(left_idx)
        if sub_trees[root][RIGHT] != '.':
            right_idx = dic[sub_trees[root][RIGHT]]
            post_order(right_idx)
        print(f'{sub_trees[root][NODE]}')


N = int(input())
sub_trees = [None] + [input().split() for _ in range(N)]
# tree = [None] * (2 ** N)

dic = {}

for i in range(1, N+1):
    dic.setdefault(sub_trees[i][NODE], i)

pre_order()
print(f'\n')
in_order()
print(f'\n')
post_order()

# print(f'sub_trees: {sub_trees}\n')
# print(f'dic: {dic}\n')
# print(f'tree: {tree}')


sys.stdin.close()