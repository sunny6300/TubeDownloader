import pytube
print """
   / \ / \ / \ / \ 
  ( T | u | b | e )
   \_/ \_/ \_/ \_/ 
    / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
   ( D | o | w | n | l | o | a | d | e | r )
    \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
   An Ultimate YouTube Video Downloader
   By Sunny Singh
"""
link = raw_input("Enter video link:")
tube = pytube.YouTube(link)
video = tube.streams.first()
video.download('/root/Desktop')
