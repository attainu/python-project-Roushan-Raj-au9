# Junk File Organizer

Junk File Organizer is a python program that helps to reduce the manual effort for the user by organizing all files in appropriate folder within seconds.

## Module Used 

• Os : The OS module in python provides functions for interacting with 
        the operating system.

To know more about Os module go through the given link :-
```bash
https://www.geeksforgeeks.org/os-module-python-examples/
```

• Sys : The sys module in Python lets us access system-specific parameters and functions.

To know more about Sys module go through the given link :-
```bash
 https://data-flair.training/blogs/python-sys-module/
```

• Path : This helps to Know the path.

• Shutil : This module helps in automating process of copying and removal of files and directories .


## How The Program Works 


• To Organize The Junk File On The Basis Of Size :- I have used a variable(size) to store the size of the file and then checking the file size by  putting some conditions and then arranging the files into their specific folders by creating new directories as per the size of the files. All the files are first moved into "Organized Directory" then inside this folder all the other directories are created accordingly. The files which are in Bytes are stored inside a new directory called BYTES and just like that all the different files are arranged in the subsequent folders( BYTES, KB, MB, GB).

• To Organize The Junk File On The Basis Of Extension :- I have created a dictionary and saved all the possible extensions i can think of. After that checking the extension of the junk file in the computer directory and then compairing it with my created dictionary  and checking is that extension in present in dictionary ,if matched then creating the new directory named "Organized" and inside it again creating new directory  with respect to the extension name and then moving the different files in the respective directory and in case if the unknown extension is encountered than automatically a new directory named "OTHER FILES" will be created and inside that all the unknown extension files will be moved.



## Prerequisite
• Need junk files and their location .


## Instructions To Run
To run this program in command prompt ,you have to paste the "organizeJunkFile.py"
inside the folder where all junk files are present and then open the command prompt and
pass the following commands :-

• If you want to organize by extension :
```bash
python organizeJunkFile.py ext
```

• If you want to organize by size : 
```bash
python organizeJunkFile.py size
```

• If you do not pass any argument by default it will organize the files with respect to
their extensions.