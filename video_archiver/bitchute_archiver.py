"""
This will focus on transferring all of the existing TGS shows from the archive to bitchute


"""

from vidDownloader import *
import hashlib
import glob
import uploader
import time
import os

def archivetoBitChute(urlList,myuser,mypass):
    for url in urlList:
        while True:
            try:
                viddata = downloader(url['webpage_url'])
                filestring = viddata.hookdata['filename'].split('.')[0]
                break
            except Exception as e:
                print(e)
                time.sleep(10)

        finalfilename = None
        for file in glob.glob("./" + filestring + "*"):
            finalfilename = file
        hash = hashlib.md5(open(finalfilename, 'rb').read()).hexdigest()

        thumbnailpath = uploader.generateThumbnail(finalfilename)
        vidname = filestring.replace("_", " ")
        uploader.executeUpload(myuser, mypass, finalfilename, thumbnailpath, url['title'], url['description'])
        #os.remove(finalfilename)