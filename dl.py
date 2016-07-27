import urllib.request
import os
import sys
from bs4 import BeautifulSoup
import requests
import re
import time
import zipfile

dir = "./Images " + time.strftime("%m-%d-%Y") + "/"
a = 0
b = 0
c = 0
d = 0
try:
	if len(sys.argv) == 2:
		c = 1
		try:
			print("Trying to open ", sys.argv[1])
			f = open(sys.argv[1], "r")
		except OSError as e:
			print("Could not find ", sys.argv[1])
			c = 2
	else:
		print("No args")
	if len(sys.argv) == 1 or c == 2:
		print("Trying to open a.txt\n")
		f = open("a.txt", "r")

except OSError as e:
	arg = input("Can't find a.txt, enter file name: ")
	try:
		
		f = open(arg, "r")
		b = 1
	except OSError as e:
		print("\nCould not find file\nExiting...")
		a = 1

if a == 0:
	os.makedirs(os.path.dirname(dir), exist_ok=True)
	numlines = str(len(f.readlines()))
	print("\nDownloading "+numlines+" image(s)")
	f.seek(0)
	i = 1
	temp = ""
	for line in f:
		if line != "\n":
			try:
				# img = urllib.request.urlopen(line)
				hdr = {'User-Agent': 'Mozilla/5.0'}
				if "https://danbooru.donmai.us/posts?page=" in line:
					continue
				if "danbooru.donmai.us/posts?tags=" in line:
					continue
				if "https://yande.re/post?tags=" in line:
					continue
				if "danbooru.donmai.us/posts/" in line:
					respose = requests.get(line)
					data = respose.text
					soup = BeautifulSoup(data, "html.parser")
					for link in soup.find_all('a', href=re.compile('^/data/')):
						line = "http://danbooru.donmai.us/" + link.get('href')

				req = urllib.request.Request(line, headers=hdr)
				img = urllib.request.urlopen(req)
				temp = line.rpartition('/')[2]
				temp = temp.strip('\n')
				print("Downloading file {}/{} {}".format(i,numlines,temp))
				out = open(dir+temp, "wb")
				out.write(img.read())
				out.close()
				i = i + 1
			except urllib.error.HTTPError as err:
				d = 1
				print("{} Could not download file {}/{} {}".format(err.code, i, numlines, temp))
				i = i + 1
				pass

				
				
				
				
	f.close()
	if c == 1:
		os.remove(sys.argv[1])
	else:
		if d == 0:
			if b == 1:
				os.remove(arg)
			else:
				os.remove("a.txt")
	print("\nDone!")