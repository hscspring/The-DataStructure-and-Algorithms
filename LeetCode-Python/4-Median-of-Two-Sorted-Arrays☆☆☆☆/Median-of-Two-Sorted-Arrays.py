def median(A, B):
    m, n = len(A), len(B)
    # 第一种特殊情况
    if m == 0 or n == 0:
        mid = int((m+n)/2)
        if (m+n)%2 == 1:
            return (A+B)[mid]*1.0
        else:
            return sum((A+B)[mid-1:mid+1])/2.0
    # 第二种特殊情况
    if m > n:
        A, B, m, n = B, A, n, m
    
    half = int((m+n+1)/2)
    pib, pie = 0, m
    # 线性 O(min(n,m))
    # for pi in range(m+1):
    #     pi = pi
    while pib <= pie:
        # 二分 O(log(min(m,n)))
        pi = int((pib+pie)/2)
        pj = half - pi
        # 因为 m>n 时 AB 互换，所以这里其实不需要判断 pj 
        if pi > 0 and pj < n and A[pi-1] > B[pj]:
            pie = pi - 1
        elif pi < m and pj > 0 and B[pj-1] > A[pi]:
            pib = pi + 1
        else:
            break
    
    if pi == 0:
        max_left = B[pj-1]
    elif pj == 0:
        max_left = A[pi-1]
    else:
        max_left = max(A[pi-1], B[pj-1])
    if pi == m:
        min_right = B[pj]
    elif pj == n:
        min_right = A[pi]
    else:
        min_right = min(A[pi], B[pj])

    if (m+n)%2 == 0:
        ans = (max_left + min_right) / 2.0
    else:
        ans = max_left * 1.0
            
    return ans

class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        arr = []
        i, j = 0, 0
        n = len(nums1) + len(nums2)

        index = int(n/2)

        if len(nums1) == 0:
            arr = nums2
        elif len(nums2) == 0:
            arr = nums1
        else:
            while (i < len(nums1) and j < len(nums2)):
                if nums1[i] <= nums2[j]:
                    item = nums1[i]
                    i = i + 1
                else:
                    item = nums2[j]
                    j = j + 1
                arr.append(item)

                if len(arr) == index + 1:
                    break
            if len(arr) < index + 1:
                if i == len(nums1):
                    arr.extend(nums2[j:])
                elif j == len(nums2):
                    arr.extend(nums1[i:])

        if n == 0:
            res = 0
        elif n % 2 == 0:
            res = (arr[index] + arr[index-1])/2
        else:
            res = arr[index]/1
        return res


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.0
    assert median(nums1, nums2) == 2.0

    nums1 = [1, 2]
    nums2 = [3, 4]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.5
    assert median(nums1, nums2) == 2.5

    nums1 = [1]
    nums2 = [2, 4]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.0
    assert median(nums1, nums2) == 2.0

    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    assert solution.findMedianSortedArrays(nums1, nums2) == 3.5
    assert median(nums1, nums2) == 3.5

    nums1 = [1, 7]
    nums2 = [2, 4, 6]
    assert solution.findMedianSortedArrays(nums1, nums2) == 4.0
    assert median(nums1, nums2) == 4.0

    nums1 = [1, 3, 5, 7]
    nums2 = [2, 10]
    assert solution.findMedianSortedArrays(nums1, nums2) == 4.0
    assert median(nums1, nums2) == 4.0

    nums1 = [1]
    nums2 = []
    assert solution.findMedianSortedArrays(nums1, nums2) == 1.0
    assert median(nums1, nums2) == 1.0

    nums1 = []
    nums2 = [1]
    assert solution.findMedianSortedArrays(nums1, nums2) == 1.0
    assert median(nums1, nums2) == 1.0

    nums1 = []
    nums2 = []
    assert solution.findMedianSortedArrays(nums1, nums2) == 0.0
    assert median(nums1, nums2) == 0.0

    nums1 = [1,2]
    nums2 = [1,2,3]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.0
    assert median(nums1, nums2) == 2.0

    nums1 = [2]
    nums2 = [1, 3]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.0
    assert median(nums1, nums2) == 2.0

    nums1 = []
    nums2 = [1, 3]
    assert solution.findMedianSortedArrays(nums1, nums2) == 2.0
    assert median(nums1, nums2) == 2.0

