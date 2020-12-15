from lab_03 import *
from random import randint
from copy import deepcopy as dc
from time import process_time_ns

rep_cnt = 50


def count_time(func, arr):
    start = process_time_ns()
    func(arr)
    end = process_time_ns()
    return end - start


def output_result(arr):
    print("Случайный массив.")
    for i in range(len(arr)):
        print((i + 1) * 100, int(arr[i][0] / rep_cnt))
    print("\nОтсортированный массив.")
    for i in range(len(arr)):
        print((i + 1) * 100, int(arr[i][1] / rep_cnt))
    print("\nОтсортированный в обратном порядке массив.")
    for i in range(len(arr)):
        print((i + 1) * 100, int(arr[i][2] / rep_cnt))


def time_test():
    bubble_time = []
    insert_time = []
    quick_time = []
    for length in range(100, 1001, 100):
        rand_arr = list(randint(-10000, 10000) for _ in range(length))
        sorted_up_arr = sorted(rand_arr)
        sorted_down_arr = sorted(rand_arr, reverse=True)

        bubble = [0, 0, 0]
        insert = [0, 0, 0]
        quick = [0, 0, 0]

        for _ in range(rep_cnt):
            bubble[0] += count_time(bubble_sort, dc(rand_arr))
            bubble[1] += count_time(bubble_sort, dc(sorted_up_arr))
            bubble[2] += count_time(bubble_sort, dc(sorted_down_arr))

            insert[0] += count_time(insert_sort, dc(rand_arr))
            insert[1] += count_time(insert_sort, dc(sorted_up_arr))
            insert[2] += count_time(insert_sort, dc(sorted_down_arr))

            quick[0] += count_time(quick_sort, dc(rand_arr))
            quick[1] += count_time(quick_sort, dc(sorted_up_arr))
            quick[2] += count_time(quick_sort, dc(sorted_down_arr))

        bubble_time.append(bubble)
        insert_time.append(insert)
        quick_time.append(quick)

    print("\nСортировка пузырьком.")
    output_result(bubble_time)
    print("\nСортировка вставками.")
    output_result(insert_time)
    print("\nСортировка быстрая.")
    output_result(quick_time)


def main():
    time_test()


if __name__ == "__main__":
    main()
