import shutil

total, used, free = shutil.disk_usage("/")

print("Total:", total // (2**30), "GB")
print("Used:", used // (2**30), "GB")
print("Free:", free // (2**30), "GB")



