#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Char2jpg.py
#
#  Copyright 2018 赵国涛 <guotao.zhao@vivo.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import exifread
import os
import json
from PIL import Image,ImageFont,ImageDraw

def getExif(filename):
    EXIF_ISO = 'EXIF ISOSpeedRatings'
    EXIF_EXPOSURE="EXIF ExposureTime"
    fd = open(filename, 'rb')
    tags = exifread.process_file(fd)
    #~ print(tags)
    fd.close()
    print(tags[EXIF_ISO])
    print(str(tags[EXIF_ISO]))
    print(tags[EXIF_EXPOSURE])


def get_exif(file_path):
    f = open(file_path, 'rb')
    tag1 = exifread.process_file(f, details=False, strict=True) #只返回常用的exif信息
    #~ print(tag1)
    tag = {}
    for key, value in tag1.items():
        tag[key] = str(value)
        print("%s: %s" % (key, value))
    tags = json.dumps(tag) #dumps为json类型
    return tags

get_exif('gps.jpg')
#~ getExif('a.jpg')