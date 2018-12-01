#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Char2jpg.py
#  
#  Copyright 2018 11091098 <11091098@SZ-11091098>
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
#~ 如可以使用EXIF中图片原来的时间（DateTimeOriginal）对图片重命名
import os
import exifread

def getExif(filename):
    FIELD = 'EXIF DateTimeOriginal'
    fd = open(filename, 'rb')
    tags = exifread.process_file(fd)
    fd.close()
    print('=== ', filename)
    if FIELD in tags:
        new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + os.path.splitext(filename)[1]
        tot = 1
        while os.path.exists(new_name):
            new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + '_' + str(tot) + os.path.splitext(filename)[1]
            tot += 1
        print(new_name)
        os.rename(filename, new_name)
    else:
        print('No {} found'.format(FIELD))

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        getExif(filename)
