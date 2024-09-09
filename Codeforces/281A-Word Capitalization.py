# A. Word Capitalization
# time limit per test2 seconds
# memory limit per test256 megabytes
# Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

# Note, that during capitalization all the letters except the first one remains unchanged.

# Input
# A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.

# Output
# Output the given word after capitalization.

word = input()
upperChar = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

if word[0] in upperChar:
    print(word)
else:
    print(word[0].capitalize() + word[1::])
