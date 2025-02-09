class PalindromeNumber:
    def __init__(self, num: int):
        self.num = num

    def brute_force(self):
        str_num = str(self.num)
        if str_num == str_num[::-1]:
            return (f"{self.num} is Palindrome")
        return (f"{self.num} is not Palindrome")
    
    # revork please
    def another_method(self):
        if self.num < 0:
            return (f"{self.num} is not Palindrome")
        if self.num%10 == self.num:
            return (f"{self.num} is Palindrome")
        x = self.num
        palindrome_n = 0
        while x > 0:
            digit = self.num % 10
            palindrome_n = palindrome_n * 10 + digit
            x = x // 10
        print(palindrome_n)
        if palindrome_n == self.num:
            return (f"{self.num} is Palindrome")

        return (f"{self.num} is not Palindrome")

pn = PalindromeNumber(12321)
print(pn.brute_force())
print(pn.another_method())