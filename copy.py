
import os
import shutil

for root, dirs, files in os.walk("path"):  # replace the . with your starting directory
   for file in files:
      path_file = os.path.join(root,file)
      shutil.copy2(path_file,"path") # change you destination dir
