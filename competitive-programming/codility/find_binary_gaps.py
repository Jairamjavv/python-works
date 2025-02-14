"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is 
surrounded by ones at both ends in the binary representation of N. For example, number 9 has 
binary representation 1001 and contains a binary gap of length 2. The number 529 has binary 
representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. 
The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 
15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 
100000 and has no binary gaps.

Write a function: def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function 
should return 0 if N doesn't contain a binary gap. For example, given N = 1041 the function 
should return 5, because N has binary representation 10000010001 and so its longest binary gap 
is of length 5. Given N = 32 the function should return 0, because N has binary representation 
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

N = 1041


def get_binary(N: int) -> str:
    # create binary string
    bs = ""
    while N >= 1:
        bs += str(N % 2)
        N = N // 2

    return bs


# O(N^2)
def solution1(N: int) -> int:
    # Implement your solution here
    # find gaps
    bs = get_binary(N)
    current_gap = 0
    max_gap = 0
    track_1 = []
    for i in bs:
        if int(i) in track_1:
            track_1.remove(1)
            max_gap = current_gap
            current_gap = 0
        if int(i) == 1:
            track_1.append(1)
        else:
            current_gap += 1

    return max_gap


print(f"Running Solution 1 for N:{N} return:{solution1(N)}")


# O(N)
def solution2(N: int) -> int:
    # Implement your solution here
    # find gaps
    bs = get_binary(N)
    current_gap = 0
    max_gap = 0

    for i in bs:
        if i == "1":
            if current_gap > max_gap:
                max_gap = current_gap
            # Reset the current_gap counter
            current_gap = 0
        else:
            current_gap += 1

    return max_gap


print(f"Running Solution 1 for N:{N} return:{solution2(N)}")
