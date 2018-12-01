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
    EXIF_DEV = 'Image Model'
    EXIF_ISO = 'EXIF ISOSpeedRatings'
    EXIF_CAPDATE ="EXIF DateTimeOriginal"
    EXIF_EXPOSURE="EXIF ExposureTime"
    EXIF_IMAGE_WIDTH="EXIF ExifImageWidth"# x axis
    EXIF_IMAGE_HEIGHT="EXIF ExifImageLength"# y axis
    EXIF_FLASH ="EXIF Flash"

    fd = open(filename, 'rb')
    tags = exifread.process_file(fd)
    fd.close()
    print('原文件名：', filename)

    exp_time_s=int(str(tags[EXIF_EXPOSURE]).split('/')[0])/int(str(tags[EXIF_EXPOSURE]).split('/')[1])
    e_ms=exp_time_s*1000
    TEXT_EXP="EXP-"+str(e_ms)[:5]+"ms"

    if EXIF_ISO in tags:
        new_name = str(tags[EXIF_DEV]).replace(' ', '_') + "#" + TEXT_EXP + "_ISO-" + str(tags[EXIF_ISO]) + os.path.splitext(filename)[1]
        tot = 1
        while os.path.exists(new_name):
            new_name = str(tags[EXIF_DEV]).replace(' ', '_') + "#" + TEXT_EXP + "_ISO-" + str(tags[EXIF_ISO]) + '_' + str(tot) + os.path.splitext(filename)[1]
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