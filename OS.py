import os
from datetime import datetime
import sys
import os
os.chdir("C:/Users/91738/Desktop/")
print(sys.executable)
# print(dir(os))  # to display or print the different os modules
print(os.getcwd())
os.chdir('C:/Users/91738/Desktop/')
print(os.getcwd())
# os.mkdir('ts')  # this will only create a single file
# os.makedirs('tp/gg/oslibpy')  # this will create a file in a folder hierarchy
# os.rmdir('tp.py')  # to remove a single file
# os.removedirs("V:/Python/tp/gg/oslibfunc.py")  # to remove the whole folder
# os.rename('org.txt', 'osfile.txt') #this is used to rename the file
# print("Filename changed !")
# print(os.stat('msg.txt'))  # to display stats of a file.
# print("Size of file :- ", os.stat('msg.txt').st_size)  # displays stat of a file
# print("Modification TimeStamp :- ", os.stat('msg.txt').st_mtime)
# mod_time = os.stat('msg.txt').st_mtime
# print("Modification Time :- ", datetime.fromtimestamp(mod_time))
print(os.listdir('C:/Users/91738/Desktop/'))
for dirpath, dirnames, filenames in os.walk('C:/Users/91738/Desktop/'):
    print('Directory Path :', dirpath)
    print('Directory Name :', dirnames)
    print('Files :', filenames)
    print()

# To get the location of JAVA_HOME environment variables
print(os.environ.get('JAVA_HOME'))
filepath = os.environ.get('JAVA_HOME')+'test.txt'
fileloc = os.path.join(os.environ.get('JAVA_HOME'), 'java.txt')
print(filepath)
print(fileloc)
print(os.path.basename(filepath))  # gets the basefile name from the path
print(os.path.split(filepath))  # splits the path
# checks whether the path actually exists or not
print("File exists : ", os.path.exists(fileloc))
print("Is file in a directory : ", os.path.isdir(fileloc))
print("is this a file : ", os.path.isfile(fileloc))
print("Splitting in text", os.path.splitext(fileloc))
print("OS Path :\n", dir(os.path))
