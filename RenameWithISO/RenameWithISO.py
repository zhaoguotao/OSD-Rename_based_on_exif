#  RenameWithISO.py
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

#~ rename pic with the ISO value
import os
import exifread

def getExif(filename):
    EXIF_ISO = 'EXIF ISOSpeedRatings'
    fd = open(filename, 'rb')
    tags = exifread.process_file(fd)
    fd.close()
    print('原文件名：', filename)
    if EXIF_ISO in tags:
        #~ print(str(tags[EXIF_ISO]))
        new_name = "ISO-" + str(tags[EXIF_ISO]) + os.path.splitext(filename)[1]
        tot = 1
        while os.path.exists(new_name):
            new_name = "ISO-" + str(tags[EXIF_ISO]) + '_' + str(tot) + os.path.splitext(filename)[1]
            tot += 1
        print('新文件名：', new_name)
        print("----------------------------")
        os.rename(filename, new_name)
    else:
        print('No {} found'.format(EXIF_ISO))


for filename in os.listdir('.'):
    if os.path.isfile(filename):
        if filename.endswith('.jpg'):
            try:
                getExif(filename)
            except Exception as e:
                print("E:",e)
                pass