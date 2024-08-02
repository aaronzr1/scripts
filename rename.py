import os

PATH = "/Users/aaronliu/Documents/AP Physics C/Answers"
filenames = []
filenames += [os.path.join(PATH, fname) for fname in os.listdir(PATH) if os.path.join(PATH, fname).endswith('.png')]

cnt = 1
for fname in filenames:
    os.rename(fname, os.path.join(PATH, f"Answer Key Page {cnt}"))
    cnt += 1