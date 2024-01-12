import os
import shutil
import time

path = input("Insert a path") 
seconds = 2592000


if(os.path.exists(path)):
    for files in os.walk(path):
            pathFile = files[0]
            Time = os.stat(files[0]).st_ctime
            if Time > seconds:
                  if(os.path.isfile(pathFile)):
                        os.remove(pathFile)
                  elif(os.path.isdir(pathFile)):
                        shutil.rmtree(pathFile)
                  else:
                        print("Error Message")
                  
        
