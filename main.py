import os
import time

path = "E:/GitHub/LazyTube/prueba.mp4"
file = path.split("/")[-1]
directory = path.rsplit("/",1)[0]
print(file)
threshold = -35
duration = 0.1
silences_start = []
silences_end = []

os.chdir(directory)
print(directory)
os.system("ffmpeg -i "+path+" -af silencedetect=n="+str(threshold)+"dB:d="+str(duration)+" -f null - 2> ok.txt")

txt_output = open("ok.txt","r")

for i in txt_output.readlines():
	if "silence" in i:
		if "|" not in i:
			silences_start.append((i.split(": ")[-1]).replace("\n",""))
		else:
			silences_end.append(((i.split(": ")[-2]).split(" ")[0]).replace("\n",""))

trim_arguments = ""
trim_paste = ""
trim_end = ""
for i in range(len(silences_end)-1):
	if i ==0:
		trim_arguments = trim_arguments+"[0:v]trim=start=0:end="+silences_start[i]+",setpts=PTS-STARTPTS,format=yuv420p["+str(i)+"v];[0:a]atrim=start=0:end="+silences_start[i]+",asetpts=PTS-STARTPTS["+str(i)+"a];"
	elif i<len(silences_end)-1:
		trim_arguments = trim_arguments+"[0:v]trim=start="+silences_end[i]+":end="+silences_start[i+1]+",setpts=PTS-STARTPTS,format=yuv420p["+str(i)+"v];[0:a]atrim=start="+silences_end[i]+":end="+silences_start[i+1]+",asetpts=PTS-STARTPTS["+str(i)+"a];"
	trim_paste = trim_paste+"["+str(i)+"v]["+str(i)+"a]"

	trim_end = "concat=n="+str(i+1)+":v=1:a=1[outv][outa] -map [outv] -map [outa] out.mp4"


print(len(silences_end)-1)
print(silences_start)
print(silences_end)
print("ffmpeg -y -i prueba.mp4 -filter_complex "+trim_arguments+trim_paste+trim_end)
os.system("ffmpeg -y -i prueba.mp4 -filter_complex "+trim_arguments+trim_paste+trim_end)



input()