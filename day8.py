"""
📝 QUESTION:

Given a list of integers, remove all duplicate occurrences of elements 
while preserving only their LAST occurrence in the list.

Return the new list.

---

✅ Example 1:
Input:  [4, 5, 9, 4, 9, 5, 7]
Output: [4, 9, 5, 7]

✅ Example 2:
Input:  [1, 2, 3, 2, 4, 1, 5]
Output: [3, 2, 4, 1, 5]

---

🔹 Additional Test Cases:
⚪ Input:  []
   Output: []

🟢 Input:  [10]
   Output: [10]

🔁 Input:  [5, 5, 5, 5, 5]
   Output: [5]

🎲 Input:  [8, 2, 7, 3, 1]
   Output: [8, 2, 7, 3, 1]

🔀 Input:  [1, 1, 2, 3, 3, 4, 2, 5, 1]
   Output: [3, 4, 2, 5, 1]

⬆️ Input:  [1, 2, 3, 4, 5]
   Output: [1, 2, 3, 4, 5]

⬇️ Input:  [5, 4, 3, 3, 4, 5]
   Output: [3, 4, 5]

"""

# ----------------------
# 🧑‍💻 SOLUTION CODE:
# ----------------------

inp = list(map(int, input("Enter numbers separated by space: ").split()))
lst = []
n = len(inp)

for ele in reversed(inp):
    if ele in lst:
        continue
    else:
        lst.append(ele)

print("Output:", lst[::-1])
