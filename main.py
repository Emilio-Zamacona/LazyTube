import os
import time

path = "E:/GitHub/LazyTube/prueba.mp4"
file = path.split("/")[-1]
directory = path.rsplit("/",1)[0]
print(file)
threshold = -30
duration = 0.5
silences = []

os.chdir(directory)
print(directory)
os.system("ffmpeg -i "+path+" -af silencedetect=n="+str(threshold)+"dB:d="+str(duration)+" -f null - 2> ok.txt")

txt_output = open("ok.txt","r")
"""for i in txt_output.readlines():
	if "silence" in i:
		print(i)"""
for i in txt_output.readlines():
	if "silence" in i:
		if "|" in i:
			print((i.split(": ")[-2]).split(" ")[0])
		else:
			print(i.split(": ")[-1])
input()