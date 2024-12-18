# This problem was recently asked by Google. Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def check(numbers, k):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                return True
    return False

# Example usage:
x = [10, 0, 10, 17]
k = 17

if check(x, k):
    print("Worked")
else:
    print("Not worked")
