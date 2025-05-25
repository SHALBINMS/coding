# Function to check if the given string is a pangram
def is_pangram(input: str) -> bool:
    # Define a set containing all 26 lowercase letters of the English alphabet
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    
    # Convert the input string to lowercase and create a set of its characters
    input_set = set(input.lower())
    
    # Check if all letters in alphabet_set are present in input_set
    return alphabet_set.issubset(input_set)


# Take user input
str = input("Enter a sentence: ")

# Check if the input is a pangram and print the result
if is_pangram(str):
    print(f"{str} is a pangram")
else:
    print(f"{str} is not a pangram")
