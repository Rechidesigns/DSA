# ===============================
# FULL SOLUTIONS + EDGE CASES + COMMON HASHMAP VARIANTS
# ===============================

# ---------- 1. TWO SUM ----------
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # No match found

# Edge Cases:
# - Negative numbers
# - Duplicates
# - Large arrays
print(twoSum([2, 7, 11, 15], 9))          # [0, 1]
print(twoSum([3, 2, 4], 6))               # [1, 2]
print(twoSum([3, 3], 6))                  # [0, 1]
print(twoSum([-1, -2, -3, -4, -5], -8))   # [2, 4]

# Variants:
# --- Find Duplicates ---
def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

# --- Count Occurrences ---
def countOccurrences(nums):
    from collections import defaultdict
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    return dict(freq)

# --- Track First/Last Index ---
def firstLastIndex(nums):
    pos = {}
    for i, num in enumerate(nums):
        if num not in pos:
            pos[num] = [i, i]
        else:
            pos[num][1] = i
    return pos

# --- Check Frequency Match (e.g. Anagrams) ---
def isAnagram(s, t):
    from collections import Counter
    return Counter(s) == Counter(t)

# --- Detect Triplets with Given Sum ---
def hasTripletWithSum(nums, target):
    nums.sort()
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                return True
            elif total < target:
                left += 1
            else:
                right -= 1
    return False


# ---------- 2. LONGEST SUBSTRING WITHOUT REPEATING ----------
def lengthOfLongestSubstring(s):
    char_index = {}
    start = max_len = 0
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len

# Edge Cases:
# - All characters same
# - Empty string
# - Spaces and special chars
print(lengthOfLongestSubstring("abcabcbb"))     # 3
print(lengthOfLongestSubstring("bbbbb"))        # 1
print(lengthOfLongestSubstring(""))             # 0
print(lengthOfLongestSubstring("a!@#a!@#"))      # 4 (a!@#)


# ---------- 3. IS PALINDROME ----------
def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Edge Cases:
# - Empty string
# - Only symbols/spaces
# - Mixed case
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                      # False
print(isPalindrome(""))                                # True
print(isPalindrome("   "))                             # True


# ---------- 4. BINARY SEARCH ----------
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Edge Cases:
# - Target not present
# - Duplicates
# - Empty list
# - Single element
print(binarySearch([1, 3, 5, 7, 9], 7))    # 3
print(binarySearch([1, 3, 5, 7, 9], 2))    # -1
print(binarySearch([], 5))                # -1
print(binarySearch([5], 5))               # 0
print(binarySearch([5], 3))               # -1


# ---------- 5. VALID PARENTHESES ----------
def isValid(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

# Edge Cases:
# - Empty string
# - Extra closing or opening brackets
# - Nested and mixed brackets
print(isValid("()[]{}"))     # True
print(isValid("(]"))         # False
print(isValid("({[]})"))     # True
print(isValid("((()))"))     # True
print(isValid("((())"))      # False
print(isValid("") )          # True






# ---------- BONUS: COMMON SORTING METHODS ----------

# --- Bubble Sort ---
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# --- Selection Sort ---
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# --- Insertion Sort ---
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- Merge Sort ---
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Quick Sort ---
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

# Sample Tests:
print("\nSORTING DEMO")
arr = [64, 34, 25, 12, 22, 11, 90]
print("Bubble:", bubbleSort(arr[:]))
print("Selection:", selectionSort(arr[:]))
print("Insertion:", insertionSort(arr[:]))
print("Merge:", mergeSort(arr[:]))
print("Quick:", quickSort(arr[:]))