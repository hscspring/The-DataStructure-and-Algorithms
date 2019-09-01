
"""
All exceeded time limit.
"""

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    res = 0
    lenh = len(height)
    for i in range(lenh):
        for j in range(i, len(height)-1):
            le = j - i + 1
            he = min(height[j+1], height[i])
            area = le * he
            if area > res:
                res = area
    return res

def maxArea(height):
    lenh = len(height)
    res = 0
    for i in range(int(lenh/2)):
        for j in range(i+1, lenh-i):
            area = max((j - i) * min(height[i], height[j]), (lenh-i-1-j) * min(height[j], height[lenh-i-1]))
            if area > res:
                res = area
    return res