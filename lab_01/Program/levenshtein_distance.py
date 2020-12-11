def lr(s_1, s_2):
    if not s_1 or not s_2:
        return max(len(s_1), len(s_2))
    return min(lr(s_1, s_2[:-1]) + 1, lr(s_1[:-1], s_2) + 1, lr(s_1[:-1], s_2[:-1]) + int(s_1[-1] != s_2[-1]))


def lm(s_1, s_2, return_matrix=False):
    if not s_1 or not s_2:
        return max(len(s_1), len(s_2))
    ls_1 = len(s_1) + 1
    ls_2 = len(s_2) + 1
    mt = [[i + j for j in range(ls_2)] for i in range(ls_1)]
    for i in range(1, ls_1):
        for j in range(1, ls_2):
            mt[i][j] = min(mt[i - 1][j] + 1, mt[i][j - 1] + 1, mt[i - 1][j - 1] + int(s_1[i - 1] != s_2[j - 1]))
    if return_matrix:
        return mt
    return mt[-1][-1]


def ldr(s_1, s_2):
    if not s_1 or not s_2:
        return max(len(s_1), len(s_2))
    res = min(ldr(s_1, s_2[:-1]) + 1, ldr(s_1[:-1], s_2) + 1, ldr(s_1[:-1], s_2[:-1]) + int(s_1[-1] != s_2[-1]))
    if len(s_1) >= 2 and len(s_2) >= 2 and s_1[-1] == s_2[-2] and s_1[-2] == s_2[-1]:
        res = min(res, ldr(s_1[:-2], s_2[:-2]) + 1)
    return res


def ldm(s_1, s_2, return_matrix=False):
    if not s_1 or not s_2:
        return max(len(s_1), len(s_2))
    ls_1 = len(s_1) + 1
    ls_2 = len(s_2) + 1
    mt = [[i + j for j in range(ls_2)] for i in range(ls_1)]
    for i in range(1, ls_1):
        for j in range(1, ls_2):
            mt[i][j] = min(mt[i - 1][j] + 1, mt[i][j - 1] + 1, mt[i - 1][j - 1] + int(s_1[i - 1] != s_2[j - 1]))
            if i > 1 and j > 1 and s_1[i - 1] == s_2[j - 2] and s_1[i - 2] == s_2[j - 1]:
                mt[i][j] = min(mt[i][j], mt[i - 2][j - 2] + 1)
    if return_matrix:
        return mt
    return mt[-1][-1]


def mt_print(mt):
    if type(mt) == list:
        for row in mt:
            print(' '.join(map(str, row)))
    else:
        print("Матрица не использовалась.")


def main():
    s_1 = input("Введите первую строку: ")
    s_2 = input("Введите вторую строку: ")

    print("\n-> Расстояние Левенштейна <-")
    print("Рекурсивный алгоритм:", lr(s_1, s_2))
    print("Матричный алгоритм:  ", lm(s_1, s_2))
    mt_print(lm(s_1, s_2, return_matrix=True))

    print("\n-> Расстояние Дамерау-Левенштейна <-")
    print("Рекурсивный алгоритм:", ldr(s_1, s_2))
    print("Матричный алгоритм:  ", ldm(s_1, s_2))
    mt_print(ldm(s_1, s_2, return_matrix=True))


if __name__ == "__main__":
    main()
