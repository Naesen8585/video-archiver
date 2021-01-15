"""
https://github.com/mps-youtube/pafy

we need to determine if there are any cues in a url which will tell us if this is a playlist or just a single video and act appropriately

"""

import youtube_dl

#this will pull down all the links on a given youtube channel page or playlist if properly specified.
def getLinks(yt_url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet': True, })
    vidlist=[]
    with ydl:
        result = ydl.extract_info \
            (yt_url,
             download=False)  # We just want to extract the info
        if 'entries' in result:
            for i, item in enumerate(result['entries']):
                finalurl = result['entries'][i]
                vidlist.append(finalurl)
        else:
            vidlist.append(result)


    return vidlist
    #return mylinks