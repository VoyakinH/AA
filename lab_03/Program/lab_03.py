from copy import deepcopy as dc
from random import choice


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def insert_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    key = choice(arr)
    l = list(filter(lambda x: x < key, arr))
    m = list(filter(lambda x: x == key, arr))
    r = list(filter(lambda x: x > key, arr))
    return quick_sort(l) + m + quick_sort(r)


def main():
    base_arr = list(map(int, input("Введите массив целых чисел через пробел: ").split()))
    print("Исходный массив целых чисел:", *base_arr)
    print("Сортировка пузырьком:       ", *bubble_sort(dc(base_arr)))
    print("Сортировка вставками:       ", *insert_sort(dc(base_arr)))
    print("Быстрая сортировка:         ", *quick_sort(dc(base_arr)))


if __name__ == "__main__":
    main()
