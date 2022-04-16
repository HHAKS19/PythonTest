class Solve():
    def twoSum(self, num, target):
        required = {}
        for i in range(len(num)):
            space = target - num[i]

            if space in required:
                return [required[space],i]
            required[num[i]]=i

input_list = [2,8,12,15]
sol1 = Solve()
print(sol1.twoSum(input_list, 14))
