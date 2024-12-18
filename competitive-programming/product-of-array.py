# This problem was asked by Uber. Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
## For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
def prod(numbers, exclude):
    result = 1
    for num in numbers:
        if num != exclude:
            result *= num
    return result


def main():
    x = [100, 50, 25, 5]
    y = [prod(x, num) for num in x]

    for val in y:
        print(val)


if __name__ == "__main__":
    main()
