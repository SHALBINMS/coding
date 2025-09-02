"""
PROBLEM: Run-Length Encoding

Write a program that performs run-length encoding on a given string.
Run-length encoding compresses consecutive identical characters by 
representing them as the character followed by the count of repetitions.

INPUT:
- A single string containing any characters (letters, numbers, symbols)

OUTPUT:
- The run-length encoded string where each character is followed by its count

EXAMPLES:
Input: "a"          → Output: "a1"
Input: "aa"         → Output: "a2"  
Input: "aaa"        → Output: "a3"
Input: "aab"        → Output: "a2b1"
Input: "abb"        → Output: "a1b2"
Input: "abc"        → Output: "a1b1c1"
Input: "aaabbc"     → Output: "a3b2c1"
Input: "aaabbbbcc"  → Output: "a3b4c2"
Input: "abcdef"     → Output: "a1b1c1d1e1f1"
Input: "aaaaaa"     → Output: "a6"
Input: "aabbcc"     → Output: "a2b2c2"
Input: ""           → Output: ""
Input: "a1b2c3"     → Output: "a111b112c113"
Input: "!!@@##"     → Output: "!2@2#2"

TEST CASES TO VERIFY:
1. Single character: "x" → "x1"
2. All same: "zzzzz" → "z5"
3. All different: "abcd" → "a1b1c1d1"
4. Mixed groups: "wwwxxyyz" → "w3x2y2z1"
5. With numbers: "11223" → "1222313"
6. With symbols: "$$%%^^" → "$2%2^2"
7. Empty string: "" → ""
8. One group at end: "aabbbcd" → "a2b3c1d1"

CONSTRAINTS:
- String length can be 0 to 1000 characters
- String can contain any printable ASCII characters
- Output should have no spaces or extra characters
"""

def run_length_encode(s):
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

# Usage
print(run_length_encode(input()), end="")