import sys

def siftUp(tree):
    i = len(tree) - 1
    while i > 0 and (tree[i // 2]) < tree[i]:
        tree[i], tree[i// 2] = tree[i// 2], tree[i]
        i = i // 2
    return tree


def siftDown(i, n, tree):
    while 2 * i <= n:     
        j = i
        if tree[2 * i] > tree[j] and tree[2*i] > tree[2*i + 1]:
            j = 2 * i
        if 2 * i + 1 <= n and tree[2 * i + 1] > tree[j]:
            j = 2 * i + 1
        tree[i], tree[j] = tree[j], tree[i]
        if i == j:
          break
        i = j
    return tree


def insertArr(element, tree):
    tree.append(element)
    if len(tree) == 1:
        return tree
    else:
        return siftUp(tree)


def extractMax(tree):
    res = tree[0]
    tree[0] = tree[-1]
    siftDown(0, len(tree)-1, tree)
    del tree[-1]
    return res


n = int(sys.stdin.readline())
tree = []
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'Insert':
        insertArr(int(cmd[1]), tree)
    elif cmd[0] == 'ExtractMax':
        print(extractMax(tree))

# ### Раскомментировать при чтении из файла
# with open('1.txt', 'r') as file:    
#     n = int(file.readline())
#     tree = []
#     for i in range(n):
#         cmd = file.readline().split()
#         if cmd[0] == 'Insert':
#             insertArr(int(cmd[1]), tree)
#         elif cmd[0] == 'ExtractMax':
#             print(tree)
#             print(extractMax(tree))
# ###



# Тестовый тривиальный алгоритм
# T = []
# tst = []
# def t_insert(x):
#     T.append(x)
# def t_extract_max():
#     m = 0
#     for i in range(1, len(T)):
#         if T[i] > T[m]:
#             m = i
#     result = T[m]
#     del T[m]
#     return result

# n = 100
# for i in range(n):
#     tst = insertArr(i, tst)
#     t_insert(i)
# for i in range(n):
#     print(T, tst, sep='\n')
#     a = extractMax(tst)
#     b = t_extract_max()
#     if a == b:
#         print(i, a)
#     else:
#         print(i, 'got:',a,',','expected:',b, " | ERROR")
#         break