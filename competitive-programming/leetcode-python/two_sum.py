import random as r

class TwoSum:
    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target

    def brute_force_method(self):
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if i != j:
                    if self.nums[i] + self.nums[j] == self.target:
                        return [i,j]
        return [0,0]
    
    def dict_method(self):
        seen_dict = {}
        for i in range(len(self.nums)):
            to_find = self.target - self.nums[i]
            if to_find in seen_dict.keys():
                return [seen_dict.get(to_find), i]
            else:
                seen_dict[self.nums[i]] = i

        return [0,0]

target = r.randint(0,20)
series = [r.randint(0,9) for i in range(50)]
ts = TwoSum(series, target)
a1, b1 = ts.brute_force_method()
a2, b2 = ts.dict_method()
print("Using Brute force:", f"{a1}:{series[a1]}+{b1}:{series[b1]}={target}")
print("Using Dict method:", f"{a2}:{series[a2]}+{b2}:{series[b2]}={target}")
