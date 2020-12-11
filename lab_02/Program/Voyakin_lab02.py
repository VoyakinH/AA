from random import randint
from time import process_time_ns


def standard_alg(mt_1, mt_2):
    if len(mt_2) != len(mt_1[0]):
        print("Неправильные размерности матриц.")
        return

    res = [[0 for _ in range(len(mt_2[0]))] for _ in range(len(mt_1))]
    for i in range(len(mt_1)):
        for j in range(len(mt_2[0])):
            for k in range(len(mt_1[0])):
                res[i][j] += mt_1[i][k] * mt_2[k][j]
    return res


def Winograd_alg(mt_1, mt_2):
    n1 = len(mt_1)
    n2 = len(mt_2)
    m2 = len(mt_2[0])

    if n2 != len(mt_1[0]):
        print("Неправильные размерности матриц.")
        return

    mulH = [0 for _ in range(n1)]
    mulV = [0 for _ in range(m2)]

    for i in range(n1):
        for j in range(n2 // 2):
            mulH[i] += mt_1[i][2 * j] * mt_1[i][2 * j + 1]

    for i in range(m2):
        for j in range(n2 // 2):
            mulV[i] += mt_2[2 * j][i] * mt_2[2 * j + 1][i]

    res = [[0 for _ in range(m2)] for _ in range(n1)]
    for i in range(n1):
        for j in range(m2):
            res[i][j] = - mulH[i] - mulV[j]
            for k in range(n2 // 2):
                res[i][j] += ((mt_1[i][2 * k] + mt_2[2 * k + 1][j]) * (mt_1[i][2 * k + 1] + mt_2[2 * k][j]))

    if n2 % 2:
        for i in range(n1):
            for j in range(m2):
                res[i][j] += mt_1[i][n2 - 1] * mt_2[n2 - 1][j]

    return res


def Winograd_alg_improved(mt_1, mt_2):
    n1 = len(mt_1)
    n2 = len(mt_2)
    m2 = len(mt_2[0])

    if n2 != len(mt_1[0]):
        print("Неправильные размерности матриц.")
        return

    d = n2 // 2

    mulH = [0 for _ in range(n1)]
    mulV = [0 for _ in range(m2)]

    for i in range(n1):
        mulH[i] = sum(mt_1[i][2 * j] * mt_1[i][2 * j + 1] for j in range(d))

    for i in range(m2):
        mulV[i] = sum(mt_2[2 * j][i] * mt_2[2 * j + 1][i] for j in range(d))

    res = [[0 for _ in range(m2)] for _ in range(n1)]
    for i in range(n1):
        for j in range(m2):
            res[i][j] = sum(
                (mt_1[i][2 * k] + mt_2[2 * k + 1][j]) * (mt_1[i][2 * k + 1] + mt_2[2 * k][j]) for k in range(d)) \
                           - mulH[i] - mulV[j]

    return res


def cpu_time(func, mt_1, mt_2):
    start = process_time_ns()
    func(mt_1, mt_2)
    end = process_time_ns()
    return end - start


def get_mt(n):
    return [[randint(-100, 100) for _ in range(n)] for _ in range(n)]


def count_time():
    for i in range(100, 501, 100):
        mt_1 = get_mt(i)
        mt_2 = get_mt(i)
        mt_1_bad = get_mt(i + 1)
        mt_2_bad = get_mt(i + 1)
        res_standard_alg = 0
        res_winograd_alg = 0
        res_winograd_alg_improved = 0
        res_standard_alg_bad = 0
        res_winograd_alg_bad = 0
        res_winograd_alg_improved_bad = 0
        for _ in range(0, 10):
            res_standard_alg += cpu_time(standard_alg, mt_1, mt_2)
            res_winograd_alg += cpu_time(Winograd_alg, mt_1, mt_2)
            res_winograd_alg_improved += cpu_time(Winograd_alg_improved, mt_1, mt_2)
            res_standard_alg_bad += cpu_time(standard_alg, mt_1_bad, mt_2_bad)
            res_winograd_alg_bad += cpu_time(Winograd_alg, mt_1_bad, mt_2_bad)
            res_winograd_alg_improved_bad += cpu_time(Winograd_alg_improved, mt_1_bad, mt_2_bad)
        res_standard_alg /= 10
        res_winograd_alg /= 10
        res_winograd_alg_improved /= 10
        res_standard_alg_bad /= 10
        res_winograd_alg_bad /= 10
        res_winograd_alg_improved_bad /= 10
        print("\nРазмерность матриц ", i, " * ", i, ':')
        print("Стандартный алгоритм: ", int(res_standard_alg), "нс")
        print("Алгоритм Винограда: ", int(res_winograd_alg), "нс")
        print("Алгоритм Винограда улучшенный: ", int(res_winograd_alg_improved), "нс")
        print("\nРазмерность матриц", i + 1, "*", i + 1, ':')
        print("Стандартный алгоритм: ", int(res_standard_alg_bad), "нс")
        print("Алгоритм Винограда: ", int(res_winograd_alg_bad), "нс")
        print("Алгоритм Винограда улучшенный: ", int(res_winograd_alg_improved_bad), "нс")


def m_output(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print()


def main():
    # mt_1 = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    # mt_2 = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
    #
    # print("\nМатрица №1:")
    # m_output(mt_1)
    # print("\nМатрица №2:")
    # m_output(mt_2)
    #
    # print("\nСтандартный алгоритм умножения матриц:")
    # m_output(standard_alg(mt_1, mt_2))
    #
    # print("\nАлгоритм Винограда:")
    # m_output(Winograd_alg(mt_1, mt_2))
    #
    # print("\nОптимизированный алгоритм Винограда:")
    # m_output(Winograd_alg_improved(mt_1, mt_2))

    count_time()


if __name__ == '__main__':
    main()
