import os

file_path = "test.log"

if os.path.exists(file_path):
    print("File exists")
else:
    print("File not found")
    