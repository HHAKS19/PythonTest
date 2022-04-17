# num = input('Type Roman')
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class solution:
    def romanint(self,s: str) -> int:
        Sum  = 0
        for i in s[::-1]: #range(len(s)-1,-1,-1)
            num = roman[s[i]]
            if num*3 < Sum:
                Sum = Sum - num
            else:
                Sum = Sum + num
        return Sum

sol = solution()
print(sol.romanint('II'))
