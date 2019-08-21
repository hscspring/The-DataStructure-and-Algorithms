class Solution:
    def get_revsersed_num(self, x):
        a = -x if x < 0 else x
        length = len(str(a))
        num = 0
        for i in range(1, length+1):
            m = int(a%(10**i)/(10**(i-1)))
            num += m*(10**(length-i))
        return -num if x < 0 else num
    def reverse(self, x: int) -> int:
        num = self.get_revsersed_num(x)
        if num > (2**31) -1 or num < -(2**31):
            num = 0
        return num
        

def get_revsersed_num2(self, x):
    s = str(x)
    if x < 0:
        s = s[1:]
        res = "-"
    else:
        res = ""
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    num = int(res)
    return num