import pytube

link = raw_input("Enter video link:")
tube = pytube.YouTube(link)
video = tube.streams.first()
video.download('/root/Desktop')
