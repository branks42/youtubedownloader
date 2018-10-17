import pytube

print("Enter the video link: ")
link = input()

yt = pytube.YouTube(link)
videos = yt.get_videos()

s = 1
for v in videos:
	print(str(s) + ". " + str(v))
	s += 1

print("Enter the number of the video: ")
n = int(input())
vid = videos[n-1]

destination = 'Path to video folder'
vid.download(destination)

print(yt.filename + "\nHas successfully downloaded.")
