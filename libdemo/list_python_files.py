import os

start_dir = r"e:\classroom\python\oct10"

for (dirname,dirs,files) in  os.walk(start_dir):
     for file in files:
         if file.endswith(".py"):
             print(dirname + "\\"+ file)