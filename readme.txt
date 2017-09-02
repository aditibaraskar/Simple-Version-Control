Problem 4:
Simple Version Control

Functionalities :
- Display a particular version of the file.
- Commit changes made to a file in a new version.

Constraints :
- A new line can only be appended ie. added at the end of file.
- Any line can be deleted from the file.
- Only one of the above two operations can be done at a time.
- After each operation, the file must be commited.

usage: 
python run.py [-h] [-v VER] filepath

positional arguments:
  filepath           relative path of file from the './local/' or './repo/'
                     directory that has to be commited or displayed

optional arguments:
  -h, --help         show this help message and exit
  -v VER, --ver VER  displays the VER version of the file

Example : 
python run.py text.txt 			commits file to ./repo/
python run.py -v 0 text.txt 	displays version 0 of the file ./repo/text.txt

Working:
Initally text.txt is created in the ./local/ directory. The file is the then 
commited and a copy (v. 0) is created in ./repo/ directory. Differences between
subsequent versions are then store in .dif file in the repo. To view a 
particular version the changes are traced by back from the current version of
the file available in the repo.