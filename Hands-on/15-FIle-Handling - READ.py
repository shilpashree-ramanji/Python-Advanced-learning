"""
=========================================================
Topic 14 : File Handling
File      : 14_file_handling.py
Author    : Shilpa
=========================================================

Objective:
- Understand File Handling
- Learn how to read a file
"""

print("\n========== Example 1 : Read File ==========\n")

file = open('/Users/shilpashreeraj/Desktop/GitHubClone/Python-Advanced-learning/Input-files/Text-Files/sample.txt', 'r')
content = file.read()
print(content)
file.close()


print("\n========== Example 2 : Read One Line ==========\n")


file = open('/Users/shilpashreeraj/Desktop/GitHubClone/Python-Advanced-learning/Input-files/Text-Files/sample.txt', 'r')
content = file.readline()
print(content)
file.close()



print("\n========== Example 3 : Read All Line ==========\n")


file = open('/Users/shilpashreeraj/Desktop/GitHubClone/Python-Advanced-learning/Input-files/Text-Files/sample.txt', 'r')
content = file.readlines()
print(content)
file.close()


print("\n========== Example 4 : Loop ==========\n")

file = open('/Users/shilpashreeraj/Desktop/GitHubClone/Python-Advanced-learning/Input-files/Text-Files/sample.txt', 'r')
for line in file:
    print(line.strip())

file.close()

print("\n========== Example 5 : with open() ==========\n")

with open("/Users/shilpashreeraj/Desktop/GitHubClone/Python-Advanced-learning/Input-files/Text-Files/sample.txt", "r") as file:
    content = file.read()
    print(content)