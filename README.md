# Download-images-from-file
Given a file with URLs separated by lines, the script will attempt to download the webpage(intended for images) to a folder with the current date.

Run the script with "dl.py [optional file argument]"

Example: dl.py example.txt

Example 2: dl.py

It checks if the user supplies an argument and attempts to open the file if there is one. If it cannot find the file or no arguments are given, it will attempt to open a file with the name "a.txt". If it cannot find "a.txt", it will prompt the user for a file name. If that file is not found either, the program will exit.
