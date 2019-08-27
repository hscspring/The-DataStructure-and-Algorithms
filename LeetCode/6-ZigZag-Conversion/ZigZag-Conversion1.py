class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        groupn = numRows + (numRows - 2)
        arr = []
        for i in range(int(len(s)/groupn)+1):
            group = s[i*groupn: (i+1)*groupn]
            arr.append(group[:numRows])
            for j,w in enumerate(group[numRows:]):
                nexts = ' '*(numRows-2-j) + w + ' '*(j+1)
                arr.append(nexts)
        res = ""
        for i in range(numRows):
            for item in arr:
                try:
                    res += item[i]
                except IndexError as e:
                    continue
        converted = res.replace(" ", "")
        return converted
