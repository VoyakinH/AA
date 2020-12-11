import levenshtein_distance as alg
from time import process_time_ns
from random import sample
from string import ascii_letters
from sys import getsizeof as gso


def cpu_time(func, s_1, s_2):
    start = process_time_ns()
    func(s_1, s_2)
    end = process_time_ns()
    return end - start


memory = 0


def lr(s_1, s_2):
    global memory
    memory += gso(s_1) + gso(s_2)
    if not s_1 or not s_2:
        res = max(len(s_1), len(s_2))
        memory += gso(res)
        return res
    res = min(lr(s_1, s_2[:-1]) + 1, lr(s_1[:-1], s_2) + 1, lr(s_1[:-1], s_2[:-1]) + int(s_1[-1] != s_2[-1]))
    memory += gso(res)
    return res


def lm(s_1, s_2, return_matrix=False):
    global memory
    memory += gso(s_1) + gso(s_2)
    if not s_1 or not s_2:
        res = max(len(s_1), len(s_2))
        memory += gso(res)
        return res
    ls_1 = len(s_1) + 1
    ls_2 = len(s_2) + 1
    mt = [[i + j for j in range(ls_2)] for i in range(ls_1)]
    memory += gso(ls_1) + gso(ls_2) + gso(mt)
    for i in range(1, ls_1):
        for j in range(1, ls_2):
            mt[i][j] = min(mt[i - 1][j] + 1, mt[i][j - 1] + 1, mt[i - 1][j - 1] + int(s_1[i - 1] != s_2[j - 1]))
    if return_matrix:
        return mt
    return mt[-1][-1]


def ldr(s_1, s_2):
    global memory
    memory += gso(s_1) + gso(s_2)
    if not s_1 or not s_2:
        res = max(len(s_1), len(s_2))
        memory += gso(res)
        return res
    res = min(ldr(s_1, s_2[:-1]) + 1, ldr(s_1[:-1], s_2) + 1, ldr(s_1[:-1], s_2[:-1]) + int(s_1[-1] != s_2[-1]))
    memory += 2 * gso(res)
    if len(s_1) >= 2 and len(s_2) >= 2 and s_1[-1] == s_2[-2] and s_1[-2] == s_2[-1]:
        res = min(res, ldr(s_1[:-2], s_2[:-2]) + 1)
    return res


def ldm(s_1, s_2, return_matrix=False):
    global memory
    memory += gso(s_1) + gso(s_2)
    if not s_1 or not s_2:
        res = max(len(s_1), len(s_2))
        memory += gso(res)
        return res
    ls_1 = len(s_1) + 1
    ls_2 = len(s_2) + 1
    mt = [[i + j for j in range(ls_2)] for i in range(ls_1)]
    memory += gso(ls_1) + gso(ls_2) + gso(mt)
    for i in range(1, ls_1):
        for j in range(1, ls_2):
            mt[i][j] = min(mt[i - 1][j] + 1, mt[i][j - 1] + 1, mt[i - 1][j - 1] + int(s_1[i - 1] != s_2[j - 1]))
            if i > 1 and j > 1 and s_1[i - 1] == s_2[j - 2] and s_1[i - 2] == s_2[j - 1]:
                mt[i][j] = min(mt[i][j], mt[i - 2][j - 2] + 1)
    if return_matrix:
        return mt
    return mt[-1][-1]


def main():
    global memory
    print("              -> Время работы алгоритмов в м.с. <-")
    print("| len |   LevRec   |   LevMat   |   LevDamRec   |   LevDamMat   |")
    for i in range(1, 8):
        # Генерация строк
        s_1 = ''.join(sample(ascii_letters, i))
        s_2 = ''.join(sample(ascii_letters, i))
        lr_time_arr = []
        lm_time_arr = []
        ldr_time_arr = []
        ldm_time_arr = []
        for _ in range(1000):
            lr_time_arr.append(cpu_time(alg.lr, s_1, s_2))
            lm_time_arr.append(cpu_time(alg.lm, s_1, s_2))
            ldr_time_arr.append(cpu_time(alg.ldr, s_1, s_2))
            ldm_time_arr.append(cpu_time(alg.ldm, s_1, s_2))
        print("%5d" % i, "%12d" % int(sum(lr_time_arr) / len(lr_time_arr)),
              "%12d" % int(sum(lm_time_arr) / len(lm_time_arr)),
              "%15d" % int(sum(ldr_time_arr) / len(ldr_time_arr)),
              "%15d" % int(sum(ldm_time_arr) / len(ldm_time_arr)))

    print("\n        -> Затрачиваемая алгоритмами память в байтах <-")
    print("| len |   LevRec   |   LevMat   |   LevDamRec   |   LevDamMat   |")
    for i in range(1, 8):
        # Генерация строк
        s_1 = ''.join(sample(ascii_letters, i))
        s_2 = ''.join(sample(ascii_letters, i))
        memory = 0
        lr(s_1, s_2)
        lr_mem = memory
        memory = 0
        lm(s_1, s_2)
        lm_mem = memory
        memory = 0
        ldr(s_1, s_2)
        ldr_mem = memory
        memory = 0
        ldm(s_1, s_2)
        ldm_mem = memory
        print("%5d" % i, "%12d" % lr_mem, "%12d" % lm_mem, "%15d" % ldr_mem, "%15d" % ldm_mem)

if __name__ == "__main__":
    main()
