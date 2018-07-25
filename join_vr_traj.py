"""
    This script takes a directory where there are multiple VR trajectory files and joins them up in one huge trajectory.
    It does this by creating a list of all the file names that have the word "trajectory" in their name.
    Then it copies them all into one single file.
"""


import os



def list_files(dir):
    """
        This function walks through the directory "dir" and returns a list of files that contain in their name the word "trajectory"

        :param dir: string
    """
    
    r = []      # List of files to be joined together
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        files = next(os.walk(subdir))[2]
        
        for file in files:
            isTrajectory = file.find("trajectory")
            if isTrajectory >= 0:
                r.append(subdir + "/" + file)
    return r


if __name__ == "__main__":

    dir = "/Volumes/Transcend/data_sets/OH_squalane_model"
    fileList = list_files(dir)
    
    totalTraj = open("combinedTraj.xyz","w")

    for item in fileList:
        inputFile = open(item, "r")
        for line in inputFile:
            totalTraj.write(line)
        inputFile.close()

    totalTraj.close()



