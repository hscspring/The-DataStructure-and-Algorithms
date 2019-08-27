Given two strings `A` and `B` of lowercase letters, return `true` if and only if we can swap two letters in `A` so that the result equals `B`.

 

**Example 1:**

```python
Input: A = "ab", B = "ba"
Output: true
```

**Example 2:**

```python
Input: A = "ab", B = "ab"
Output: false
```

**Example 3:**

```python
Input: A = "aa", B = "aa"
Output: true
```

**Example 4:**

```python
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
```

**Example 5:**

```python
Input: A = "", B = "aa"
Output: false
```

 

**Note:**

1. `0 <= A.length <= 20000`
2. `0 <= B.length <= 20000`
3. `A` and `B` consist only of lowercase letters.