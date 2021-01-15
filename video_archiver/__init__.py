import videoFinder
import time
import random
import bitchute_archiver
import getpass


class archive:
    def __init__(self,bitchuteuser=None,bitchutepass=None,url=None):
        if bitchuteuser is None:
            self.bitchuteuser = input("Enter bitchute username > ")
        if bitchutepass is None:
            self.bitchutepass = getpass.getpass("Enter bitchute password >")
        if url is None:
            self.url = input("Please enter the video, playlist or whole channel videos URL for archival: >")
        vidlist=videoFinder.getLinks(url)
        bitchute_archiver.archivetoBitChute(vidlist,bitchuteuser,bitchutepass)