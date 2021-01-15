"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/

"""
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

# Always prefer setuptools over distutils
import setuptools

keywords = ['archival','bitchute','youtube-dl','youtube','censorship','archive','backup','video']

setuptools.setup(
    name="video_archiver",
    version="0.1",
    author="naesen8585",
    author_email="notghostpolitics@gmail.com",
    description="video_archiver provides a simple interface to archive any video or set of videos from youtube to bitchute",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://www.github.com/naesen8585/video-archiver",
    keywords = keywords,
    install_requires=['youtube-dl', 'selenium', 'asyncio', 'moviepy', 'pillow'],
    packages = setuptools.find_packages(),
    classifiers=['Development Status :: 4 - Beta',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: Developers',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: MIT License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Communications :: Email',
              'Topic :: Office/Business',
              'Topic :: Software Development :: Bug Tracking',
              ],
)
