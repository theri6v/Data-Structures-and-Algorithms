def shell_sort(collection):
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        for i in range(gap, len(collection)):
            j = i
            while j >= gap and collection[j] < collection[j - gap]:
                collection[j], collection[j - gap] = collection[j - gap], collection[j]
                j -= gap
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(shell_sort(unsorted))
