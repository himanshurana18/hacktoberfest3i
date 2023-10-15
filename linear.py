def linear_search(arr, x):
    """
    Perform linear search to find the index of x in arr.

    :param arr: List of elements.
    :param x: Element to search for.
    :return: Index of x in arr, or -1 if x is not present.
    """

    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110

index = linear_search(arr, x)
if index != -1:
    print(f"Element {x} is present at index {index}.")
else:
    print(f"Element {x} is not present in the array.")
