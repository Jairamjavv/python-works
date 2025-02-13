"""
Source : Techgig Januaury Code Challenge
Qns : The New Year Party is on and people are coming up with new and innovative ideas for party and games. 
    Mr. Alphabet has organised such a theme party. He has invited N people for the party and all have come wearing a t-shirt with a single lowercase alphabet printed on it. 
    The alphabet may be their starting name or their favorite of all 26. The alphabet on the t-shirt provides individuals with their party number. 
Example:
    Suppose if the t-shirt has 'a' printed on it, then the party number of the person wearing that is equal to 1 
    and so on with the alphabet 'z' having the party number 26. Mr. Alphabet has organised a game for the guests. 
    In this game, N people will arrange themselves in a linear manner randomly. Mr. Alphabet will provide a party number P 
    and people have to tell the count of all those, the sum of whose will be equal to P. The limitation is that only the 
    continuous ones can be together in forming the party number P.
Example:
Suppose there are 3 people, N =3.
The alphabets on their t-shirt are 'a', 'b', and 'c' respectively. The limitation is that only continuous ones can be together.
Mr. Alphabet will provide gifts for the correct answers. No one wants to lose out on the gifts but they are finding it difficult to answer. 
Can you help them and provide correct answers to Mr. Alphabet?

Input Format
The first line of input consists of the number of test cases, T
The first line of each test case consists of the number of people, N and the Party number, P
The second line of each test case consists of the alphabets of the N people arranged in a line.
Constraints :
1<= T<= 10
1<= N <=1000000
1<= P <=26000000
Output Format :
Print the required output in a separate line. If no answer exists, print 0.
"""


def main():
    # Number of test cases
    t = int(input())
    results = []

    for _ in range(t):
        # Input: number of people (N) and party number (P)
        n, p = map(int, input().split())
        # Input: string of alphabets on t-shirts
        st = input()

        # Convert alphabets to their corresponding party numbers
        nums = [ord(ch) - 96 for ch in st]

        # Efficient subarray sum calculation using a hashmap
        current_sum = 0
        sum_count = {0: 1}  # Initialize with 0 sum having one occurrence
        count = 0

        for num in nums:
            current_sum += num
            # Check if (current_sum - P) exists in the hashmap
            if current_sum - p in sum_count:
                count += sum_count[current_sum - p]
            # Update hashmap with current_sum
            sum_count[current_sum] = sum_count.get(current_sum, 0) + 1

        # Append the result for the current test case
        results.append(count)

    # Print all results
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
