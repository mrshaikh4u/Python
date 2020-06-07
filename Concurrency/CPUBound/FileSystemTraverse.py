import os
import subprocess
import multiprocessing


dest = "/Users/seera/Documents/Rahil/learning_notes/bk_folder" # replace <destination-path> with the destination directory

def copyFiles(srcLocation):
    print(multiprocessing.current_process().name)
    # for i in range(len(srcLocation)):
    #     subprocess.call(["rsync", "-arq", srcLocation[i], dest])


def triggerProcess(paths:list):
    # copyFiles(paths)
    with multiprocessing.Pool() as pool:
        pool.map(copyFiles,paths)
    # pass

src = "/Users/seera/Documents/Rahil/learning_notes/orig_folder/" # replace <source-path> with the source directory
paths = []
for root, dirs, files in os.walk(src,topdown=True,followlinks=False):
    for i in dirs:
        paths.append(root+i)
    break
print(paths)
for p in paths:
    print(p)
# triggerProcess()
# triggerProcess(paths)
