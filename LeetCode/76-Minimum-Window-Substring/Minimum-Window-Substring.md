Given two strings `s` and `t`, return *the minimum window in `s` which will contain all the characters in `t`*. If there is no such window in `s` that covers all characters in `t`, return *the empty string `""`*.

**Note** that If there is such a window, it is guaranteed that there will always be only one unique minimum window in `s`.

 

**Example 1:**

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Example 2:**

```
Input: s = "a", t = "a"
Output: "a"
```

 

**Constraints:**

- `1 <= s.length, t.length <= 105`
- `s` and `t` consist of English letters.

 

**Follow up:** Could you find an algorithm that runs in `O(n)` time?