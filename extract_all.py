import os
import glob

types = ("mp4", "webm")
files = []
for t in types:
    files.append(glob.glob("/datadrive1/ChangeIt/test-full/**/*." + t, recursive=True))
print(files)

command = "python extract.py "
for video_paths in files:
    for path in video_paths:
        if "dMF-aIHP8sA.mp4" in path or "CRIdXVzlbvI.mp4" in path:
            continue
        command += path + " "

with open("./extract_broken.sh","w") as f:
    f.write(command)