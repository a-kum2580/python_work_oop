def bubbleSort(arr):

    """

    Implement the Bubble Sort algorithm for sorting a list of elements in ascending order.


    :param arr: A list of elements to be sorted.

    :return: None.

    """

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if not swapped:

            break


# Example usage

arr = [64, 34, 25, 12, 2, 11, 90]

bubbleSort(arr)

print("Sorted array:", arr)