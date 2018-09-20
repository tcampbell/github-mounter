#!/usr/bin/env python
"""
Read the latest version of a github repo by downloading the tarball.
"""

import tempfile

import click
from fs import open_fs
from fs.memoryfs import MemoryFS
from fs.zipfs import ZipFS
import requests

# What I want to see
REPO = 'PyFilesystem/pyfilesystem2'

# memoize (to disk?) a cache of this results
zip_data = requests.get('https://github.com/%s/archive/master.zip' % (REPO,)).content

try:
    t = tempfile.NamedTemporaryFile(mode='w+b', suffix='.zip', dir='.')
    t.write(zip_data)
    t.seek(0L)
    projects_fs = open_fs('zip://' + t.name)
    for path in projects_fs.walk.files(filter=['*.md']):
        print path
finally:
    t.close()
    pass

