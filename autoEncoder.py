import os
import subprocess
from mutagen.easymp4 import EasyMP4

ffmpegPath = 'D:\\_userData\\Programs\\ffmpeg\\bin\\ffmpeg.exe'

print("Drop the dir.")
dir = input()
fileList = os.listdir(dir)

try:
	encodedList = os.listdir(dir+"\\encoded")
except:
	os.mkdir(dir+"\\encoded")
	encodedList = []

logList = []

for fileName in fileList:
	_, ext = os.path.splitext(fileName)
	ext = ext.lower()

	if(((ext == ".mp4") or (ext == ".mov")) and (fileName not in encodedList)):
		fullPath = dir + "\\" + fileName
		dstPath = dir + "\\encoded\\" + fileName

		info = EasyMP4(fullPath)
		size = os.path.getsize(fullPath)

		try:
			comment = info["comment"][0]
		except:
			comment = ""

		#コメントがない
		if(comment != "compressed by ffmpeg"):
			length = info.info.length

			#無音
			if(length == 0):
				info["comment"] = "compressed by ffmpeg"
				info.save()
				logList.append((fileName, "no sound"))
				continue
			else:
				bitrate = int(size*8 / length / 1000)
				#ビットレートが約2500以下
				if(bitrate <= 2500):
					info["comment"] = "compressed by ffmpeg"
					info.save()
					logList.append((fileName, "bitrate is less than about 2500Kb/s"))
					continue
				else:
					subprocess.run([ffmpegPath, "-i", fullPath, "-vcodec", "libx264", "-acodec", "copy", dstPath])
					dstSize = os.path.getsize(dstPath)
					mtime = os.stat(fullPath).st_mtime
					atime = os.stat(fullPath).st_atime
					dstatime = os.stat(dstPath).st_atime

					if(dstSize <= size):
						dstinfo = EasyMP4(dstPath)
						dstinfo["comment"] = "compressed by ffmpeg"
						dstinfo.save()

						os.utime(dstPath, (dstatime, mtime))
						logList.append((fileName, "compressed"))
					else:
						#エンコードしたらサイズが大きくなった場合
						info["comment"] = "compressed by ffmpeg"
						info.save()
						os.remove(dstPath)

						os.utime(fullPath, (atime, mtime))
						logList.append((fileName, "original is smaller"))
					
		else:
			logList.append((fileName, 'has "compressed by ffmpeg" comment'))
	else:
		if(ext==".mp4" or ext == ".mov"):
			logList.append((fileName, 'already in "encoded" dir'))

print("\nSummary\n")
for (l1, l2) in logList:
	print(l1, "\t", l2)

print("\nPress enter to exit.")
_ = input()