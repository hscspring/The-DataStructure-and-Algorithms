class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        groupn = numRows + numRows - 2
        news = s + (len(s)%groupn)* " "
        res = ""
        for i in range(numRows):
            for j in range(int(len(news)/groupn) + 1):
                if i > 0 and i < numRows - 1 and j > 0:
                    pcol = news[j*groupn-i]
                    if pcol == " ":
                        continue
                    res += pcol
                try:
                    col = news[groupn*j+i]
                except IndexError as e:
                    continue
                if col == " ":
                    continue
                res += col
        return res