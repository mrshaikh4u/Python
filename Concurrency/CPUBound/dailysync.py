#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os

src = "../data/prod/"
dest = "../data/prod_backup/"

def copy_files(source):
    for s in source:
        subprocess.call(["rsync", "-aq", s, dest])


if __name__ == "__main__":
    paths = []
    print('Hello')
    #print(os.walk(src,topdown=True))
    for root,dirs,files in os.walk(src,topdown=True):
        for i in dirs:
            paths.append(root+i)
            #print(dirs)
        break
    print(paths)
    #for p in paths:
     #   print(p)
    p=Pool(len(paths))
    p.map(copy_files,paths)



