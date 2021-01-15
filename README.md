# video-archiver
This repo will focus on creating an automated way of archiving videos from mainstream sites to backups.

**Prerequisites**:
-
-Python 3.7+

Bitchute account for uploading

**Installation**:
-
`pip install -r REQUIREMENTS.txt`
`pip install .`

**Useage**:
-
```
import video_archiver
video_archiver.archive() #will prompt you for your bitchute user, password, and vidurl

#alternatively:

video_archiver.archive(bitchuteuser="myuser123", bitchutepassword="dontdothis",url="any youtube video, playlist or total channel video url")


```

`video_archiver` Will automatically download the video from youtube at the best quality and then upload them to Bitchute.

Currently it does not publish the video itself on Bitchute, you still have to manually publish, but it will upload and process the video there.

**Contributing**:
-
If you would like to contribute, fork this repo, make your changes, and make a PR to this repo.

