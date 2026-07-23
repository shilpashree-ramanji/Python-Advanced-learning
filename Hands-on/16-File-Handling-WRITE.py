"""
=========================================================
Topic 15 : Writing to a File
File      : 15_file_write.py
Author    : Shilpa
=========================================================

Objective:
- Learn how to write data into a file.
- Understand Write (w) mode.
"""

print("\n========== Example 1 : Write to a File ==========\n")

with open ("/Users/shilpashreeraj/Desktop/GitHubClone/Python-Advanced-learning/Sample-Files/Output-Files/sample-output.txt", "w") as file:
    file.write("Hello Shilpa and am doing sample write as a text file \n")

print("Data is wrriten successfully...!!!")