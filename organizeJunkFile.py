# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:48:15 2020

@author: Roushan
"""


import os
import shutil
from pathlib import Path
import sys

class Organize: 
    # Storing The Different Type Of Extensions In Dictionary.     
    DIRECTORIES = {
        "HTML": [".html5", ".html", ".htm", ".xhtml"],
        "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
        ".heif", ".psd"],
        "VIDEOS": [".mkv", ".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
        ".qt", ".mpg", ".mpeg", ".3gp"],
        "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
        ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
        ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
        "pptx"],
        "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
        ".dmg", ".rar", ".xar", ".zip"],
        "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
        ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
        "PLAINTEXT": [".txt", ".in", ".out"],
        "PDF": [".pdf"],
        "PYTHON": [".py"],
        "XML": [".xml"],
        "EXE": [".exe"],
        "SHELL": [".sh"]
    }
    # You  can use this below approach  or dictionary comprehension .
    """
    FILE_FORMATS = {}
    for key,value in DIRECTORIES.items(): 
        for k in value :   
            FILE_FORMATS[k] = key
    """          
    # Using Dictionary Comprehension   
    FILE_FORMATS = {file_format: directory
        for directory, file_formats in DIRECTORIES.items()
        for file_format in file_formats}       
    # Instance Method To Organize  The Files With Respect To Extensions .
    def organize_By_Extension(self):
        # Finding The Current Working Directory (cwd) Of Each File. 
        cwd = os.getcwd()      
        for entry in os.scandir():       
            if not entry.is_dir():
                # Finding The Path Of The File.
                file_path = os.path.abspath(entry)
                # To Know The Extension Of The File.
                file_format = os.path.splitext(file_path)[1].lower()
                # Checking If That Extension Is Present or Not .              
                if file_format in self.FILE_FORMATS:
                    parent_directory_path = os.path.join(cwd, "organized") 
                    # Checking If The Directory Is Present or Not , If Not Than creating Directory.                 
                    if not os.path.exists(parent_directory_path):
                        os.mkdir(parent_directory_path)                      
                    new_destination_folder = os.path.join(parent_directory_path, self.FILE_FORMATS[file_format])                 
                    if not os.path.exists(new_destination_folder):
                        os.mkdir(new_destination_folder) 
                    # Copying The Files To The Respective Directory.                     
                    shutil.copy2(file_path, new_destination_folder)                 
                    destination = os.path.join(new_destination_folder, entry)
                    if os.path.exists(destination):
                        # Removing The Copied File.
                        os.remove(file_path)                  
        try:
            os.mkdir("OTHER FILES")
        except BaseException:
            pass   
        for entry in os.scandir():    
            try:
                # Checking If Any Directory Are Present In Junk Area.
                if entry.is_dir():
                    # Removing Junk Directory.
                    os.rmdir(entry)  
                else:
                    # If Some Unknown Extension Comes Then It Will Create OTHER FILES Named Directory,
                    # And Will Move All That Files Inside OTHER FILES  Directory.
                    os.rename(os.getcwd() + '/' + str(Path(entry)), os.getcwd() + '/OTHER FILES/' + str(Path(entry)))
            except BaseException:
                pass
    # Instance Method To Organize The Files With Respect To Sizes .
    def organize_By_Size(self):
        cwd = os.getcwd() 
        for entry in os.scandir():
            if not entry.is_dir():
                file_path = os.path.abspath(entry)             
                # Storing Size Of The Files .
                size = os.stat(entry).st_size            
                parent_destination_folder = os.path.join(cwd, "Organized")
                if not os.path.exists(parent_destination_folder):
                    os.mkdir(parent_destination_folder)      
                # Compairing The Files Size in Bytes .
                if size >= 0 and size <= 1000:
                    new_destination_folder = os.path.join(parent_destination_folder, "BYTES")
                    if not os.path.exists(new_destination_folder):
                        # Creating The Directory .
                        os.mkdir(new_destination_folder) 
                    # Coping The Files.                   
                    shutil.copy2(file_path, new_destination_folder)
                    old_destination = os.path.join(new_destination_folder, entry)
                    if os.path.exists(old_destination):
                        # Removing The Junk File.
                        os.remove(file_path)                  
                # For The Files Size in Kb .
                elif size > 1000 and size <= 1000000:
                    new_destination_folder = os.path.join(parent_destination_folder, "KB")
                    if not os.path.exists(new_destination_folder):
                        os.mkdir(new_destination_folder)           
                    shutil.copy2(file_path, new_destination_folder)                 
                    old_destination = os.path.join(new_destination_folder, entry)
                    if os.path.exists(old_destination):
                        os.remove(file_path)         
                # For The Files Size Upto 100Mb .
                elif size > 1000000 and size <= 100000000:
                    new_destination_folder = os.path.join(parent_destination_folder, "UPTO 100MB")
                    if not os.path.exists(new_destination_folder):
                        os.mkdir(new_destination_folder)                       
                    shutil.copy2(file_path, new_destination_folder)                  
                    old_destination = os.path.join(new_destination_folder, entry)
                    if os.path.exists(old_destination):
                        os.remove(file_path)               
                # For The Files Size Upto 500Mb .
                elif size > 100000000 and size <= 500000000:
                    new_destination_folder = os.path.join(parent_destination_folder, "UPTO 500MB")
                    if not os.path.exists(new_destination_folder):
                        os.mkdir(new_destination_folder)                     
                    shutil.copy2(file_path, new_destination_folder)                    
                    old_destination = os.path.join(new_destination_folder, entry)
                    if os.path.exists(old_destination):
                        # Removing The Junk File
                        os.remove(file_path)                      
                # For The Files Size More Than 500Mb .
                elif size > 500000000:
                    new_destination_folder = os.path.join(parent_destination_folder, "MORE THAN 500MB")
                    if not os.path.exists(new_destination_folder):
                        os.mkdir(new_destination_folder)                       
                    shutil.copy2(file_path, new_destination_folder)                  
                    old_destination = os.path.join(new_destination_folder, entry)
                    if os.path.exists(old_destination):
                        os.remove(file_path)
def main():
    ref = Organize()
    # Taking Input From Command Line Using Command Line Parsing .
    if len(sys.argv) == 1:
        ref.organize_By_Extension()       
    elif len(sys.argv) == 2:
        user_input = sys.argv[1]      
        if user_input == "ext":
            ref.organize_By_Extension()         
        elif user_input == "size":
            ref.organize_By_Size()         
        else:
            print("Please Enter Correct Option Either 'ext' or 'size' ")             
if __name__ == '__main__':
    main()