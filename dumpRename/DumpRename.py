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

import os
import exifread
org_filename_first = "***"
new_first_name ="***"
def getExif(filename):
    global org_filename_first
    global new_first_name
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
    org_filename_first=filename.split('-')[0]

    if EXIF_CAPDATE in tags:
        new_first_name = "IMG_" + str(tags[EXIF_CAPDATE]).replace(':', '').replace(' ', '_')
        new_name=new_first_name+os.path.splitext(filename)[1]
        print('新文件名：', new_name)
        print("-"*50)
        os.rename(filename, new_name)
    else:
        print('No {} found'.format(EXIF_ISO))

def SetnonejpgName(filename):
    global org_filename_first
    global new_first_name
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            if not filename.endswith('.jpg'):
                if filename.split('-')[0] == org_filename_first:
                    try:
                        #~ print("old name:",filename)
                        new_name=filename.replace(org_filename_first,new_first_name)
                        print("new name:",new_name)
                        os.rename(filename, new_name)
                        print("~"*50)
                    except Exception as e:
                        pass

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        if filename.endswith('.jpg'):
            try:
                getExif(filename)
                SetnonejpgName(filename)
                print("*"*100)
            except Exception as e:
                print("E:",e)
                pass
