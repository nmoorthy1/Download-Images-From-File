# Download Images From File
Given a file with URLs separated by lines, the script will attempt to download the webpage(intended for images) to a folder with the current date.

## Requirements

Python >= 3.3

## Usage

Download images listed in file if supplied

    >>> dl.py [optional file argument]

Download images listed in example.txt

    >>> dl.py example.txt

Download images from default file a.txt if found

    >>> dl.py


## Example
    >>> dl.py
    No args
    Trying to open a.txt
    
    Can't find a.txt, enter file name: example.txt
    
    Downloading 3 image(s)
    Downloading 2xjKoEZ.png
    Downloading S0OLuhO.mp4
    Downloading 08pNXmr.jpg
    
    Done!
    

It checks if the user supplies an argument and attempts to open the file if there is one. If it cannot find the file or no arguments are given, it will attempt to open a file with the name "a.txt". If it cannot find "a.txt", it will prompt the user for a file name. If that file is not found either, the program will exit. After reading through a file and downloading everything, it will automatically delete the file it read from.
