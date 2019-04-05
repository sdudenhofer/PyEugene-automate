import os
import glob

folder = input("Please enter directory to search:")
path = os.path.join(folder, '*')
files = sorted(glob.iglob(path), key=os.path.getctime, reverse=True)
print(files[0])