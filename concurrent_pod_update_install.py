#!/usr/bin/env python3

import os
import sys
import time
from pathlib import Path

def main():

    path_to_cocoa_pods_update_dir = str(Path.home()) + "/" + sys.argv[1]                        #the path to folder that is to be created.
    time_to_wait = 300                                                                          #the maximal time to wait for another process to finish updating pods

    if sys.argv[1] in os.listdir(str(Path.home())):                                             #if the folder is found in the Home directory than another pod update process is running.
        print("CocoaPods update already in progress, waiting up to 5 minutes for it to finish.")

        while os.path.isdir(path_to_cocoa_pods_update_dir):                                     #while the folder exists
            if os.path.isdir(path_to_cocoa_pods_update_dir) == False or time_to_wait == 0:      #check if it still exists or if the time has run out
                break                                                                           #and break the loop
            else:
                time.sleep(1)
                time_to_wait = time_to_wait - 1
                print(time_to_wait)

        print("5 minutes passed or second process finished, updating CocoaPods.")
        os.mkdir(path_to_cocoa_pods_update_dir)                                                 #create the directory, so another process cannot start the pod update operations and fail yours
        os.system("pod repo update && pod update")                                              #do the pod update after the above loop has ended

        if sys.argv[1] in os.listdir(str(Path.home())):                                         #if the folder still exists, remove it
            os.rmdir(path_to_cocoa_pods_update_dir)

    else:                                                                                       #if no other cocoapods process was running, create the folder
        os.mkdir(path_to_cocoa_pods_update_dir)
        os.system("pod repo update && pod update")                                              #update the pods
        os.rmdir(path_to_cocoa_pods_update_dir)                                                 #and remove the directory

    os.system("pod install")                                                                    #install the pods after they have been updated

if __name__ == '__main__':
    main()
