import pytube
import urllib.request
import urllib.parse
import re

print("Enter the video name: ")
song = input()

query_string = urllib.parse.urlencode({"search_query" : song})
html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

yt = pytube.YouTube("https://www.youtube.com/watch?v=" + search_results[0])
videos = yt.get_videos()

s = 1
for v in videos:
	print(str(s) + ". " + str(v))
	s += 1

print("Enter the number of the video: ")
n = int(input())
vid = videos[n-1]

destination = 'Path to download folder'
vid.download(destination)

print(yt.filename + "\nHas been successfully downloaded.")
