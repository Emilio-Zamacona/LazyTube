import os

path = input("que video querés editar?")
file = path.split("\\")[-1]
print(file)
threshold = -45
duration = 0.5

os.chdir(path)
os.system("ffmpeg -i "+path+" -af silencedetect=n="+str(threshold)+"dB:d="+str(duration)+" -f null - 2> ok.txt")
input()