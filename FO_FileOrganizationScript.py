import os
import shutil

'''
- 1st script

This is a simple script that organizes files in a folder by their extension. 
For example, if you have a folder with a bunch of files in it, and some of them are .txt files, some are .py files, some are .jpg files, etc.
This script will create a folder for each extension and move the files with that extension to the folder with the same name as the extension❗
'''
target_folder = 'C:/Users/Raffp/Desktop/snippets'
extensions = {file.split('.')[-1] for file in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, file))}
# This code creates a set of file extensions in a target folder using a set comprehension.
# It goes through each file in the target folder and checks if it's a file and not a folder. If it's a file, it splits the file name by the period (.) and takes the last element, which is the extension. 
# Then, it adds the extension to the set of extensions in the target folder.
# After that, for each extension in the set of extensions, it creates a folder with the same name as the extension 
# and moves the files with that extension to the folder with the same name. 
# For instance, if the set of extensions is {txt, py, jpg}, it will create three folders with the names txt, py, and jpg and move the files with the extensions txt, py, and jpg to the folders with the corresponding names.



for extension in extensions:
    os.mkdir(os.path.join(target_folder, extension))
    # this creates a folder for each extension
    # for file in os.listdir(target_folder):
    #     if file.endswith(extension):
    #         shutil.move(os.path.join(target_folder, file), os.path.join(target_folder, extension))
            # this moves the file to the folder with the same name as the extension
            # it does this by joining the target folder path and the file name and then joining the target folder path and the extension
            # this is then passed to the move function which moves the file from the first path to the second path






'''
- 2nd script

This is a simple script that checks if a folder exists, and if it doesn't, it creates the folder. 
If the folder already exists, it will display a message indicating that the folder is already present❗
'''
#folder = 'c:/Users/raffp/Desktop/PythonProjects' # folder path to create or check if it exists already 

# try: # try to create the folder using the path above by using the mkdir function from the os module for example os.mkdir('c:/Users/raffp/Downloads/pyFolder')
#     os.mkdir(folder) # create the folder if it doesn't exist already 
#     print("Folder created")
# except FileExistsError: # if the folder already exists then print this message 
#     print("Folder already exists")


'''
- 3rd script

This is a straightforward script that checks if a folder or a file exists, and if it does, it removes it. 
You just need to provide the correct path to the file or folder you want to delete. 
Remember to use the os.remove() function to delete a file❗
'''

if os.path.exists('C:/Users/Raffp/Downloads/pythonHandwriting'): 
    shutil.rmtree('C:/Users/Raffp/Downloads/pythonHandwriting') 
    print("The folder has been deleted")
else: 
    print("The folder does not exist")


# print(os.chdir('C:/Users/Raffp/Downloads')) # change the current working directory
# print(os.getcwd()) # get the current working directory



'''
- 4th script

Creating a File or Folder

'''
#newFolder = os.mkdir('C:/Users/Raffp/Desktop/PythonTestFolder') # create a folder in the path above
# try:
#     print(newFolder) 
#     # create a folder in the path above
#     print("Folder created")

# except ValueError:
#     print("Folder already exists")

# file = open('C:/Users/Raffp/Desktop/React Native Projects/SportsApp/SportsApp/components/screens/contact.js', 'w')
# file.write("Hello World")
# print(file, "File created")
# file.close()
# create a file in the folder with the path above









# Tips --------------------------------------------------------------------------------------------------------------
# - You can use the os module to get the current working directory by using the getcwd function for example os.getcwd()

# - You can use the os module to change the current working directory by using the chdir function for example os.chdir('c:/Users/raffp/Desktop')

# - You can use the os module to get the list of files in a folder by using the listdir function for example os.listdir('c:/Users/raffp/Desktop')

# - You can use the os module to get the path of the current file by using the __file__ variable for example os.path.abspath(__file__)

# - You can use the shutil module to move files from one folder to another by using the move function for example shutil.move('c:/Users/raffp/Desktop/test.txt', 'c:/Users/raffp/Desktop/test2.txt')

# - You can use the os module to check if a file exists by using the path.exists function for example os.path.exists('c:/Users/raffp/Desktop/test.txt')

# - Create a folder using the os module by using the mkdir function for example os.mkdir('c:/Users/raffp/Desktop/testFolder')

# - Delete a folder using the os module by using the removedirs function for example os.removedirs('c:/Users/raffp/Desktop/testFolder')




