import os

start_dir = input("Enter start directory : ")

for (dirname,dirs,files) in  os.walk(start_dir):
    print(f"{dirname:30s} -  {len(files)}")