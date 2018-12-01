#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  OSD2jpg.py
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
from PIL import Image,ImageFont,ImageDraw

POS_X = 1700#2448-1700=748;3264-748=2516
POS_Y_START = 0


def OSD(filename):
    print(filename)
    EXIF_DEV = 'Image Model'
    EXIF_ISO = 'EXIF ISOSpeedRatings'
    EXIF_EXPOSURE="EXIF ExposureTime"
    EXIF_IMAGE_WIDTH="EXIF ExifImageWidth"# x axis
    EXIF_IMAGE_HEIGHT="EXIF ExifImageLength"# y axis
    EXIF_FLASH ="EXIF Flash"
    EXIF_CAPDATE ="EXIF DateTimeOriginal"
    fd = open(filename, 'rb')
    tags = exifread.process_file(fd)
    fd.close()

    POS_X = int(str(tags[EXIF_IMAGE_WIDTH]))-748
    exp_time_s=int(str(tags[EXIF_EXPOSURE]).split('/')[0])/int(str(tags[EXIF_EXPOSURE]).split('/')[1])
    e_ms=exp_time_s*1000
    TEXT_DEV="设备: "+str(tags[EXIF_DEV])
    TEXT_ISO="ISO: "+str(tags[EXIF_ISO])
    TEXT_EXP="曝光时间: "+str(e_ms)[:5]+"ms"
    TEXT_DPI=str(tags[EXIF_IMAGE_WIDTH])+" x "+str(tags[EXIF_IMAGE_HEIGHT])
    TEXT_FLASH="闪光灯: "+str(tags[EXIF_FLASH])
    TEXT_DATE="拍摄日期: "+str(tags[EXIF_CAPDATE])

    im=Image.open(filename)
    exif = im.info['exif']
    draw=ImageDraw.Draw(im)
    newfont=ImageFont.truetype('simkai.ttf',40)
    draw.text((POS_X,POS_Y_START+50),TEXT_DEV,(0,255,0),font=newfont)
    draw.text((POS_X,POS_Y_START+100),TEXT_EXP,(0,255,0),font=newfont)
    draw.text((POS_X,POS_Y_START+150),TEXT_ISO,(0,255,0),font=newfont)
    draw.text((POS_X,POS_Y_START+200),TEXT_DPI,(0,255,0),font=newfont)
    draw.text((POS_X,POS_Y_START+250),TEXT_FLASH,(0,255,0),font=newfont)
    draw.text((POS_X,POS_Y_START+300),TEXT_DATE,(0,255,0),font=newfont)
    new_name = os.path.splitext(filename)[0] + "_OSD" + os.path.splitext(filename)[1]
    im.save(new_name,quality=95,exif=exif)
    #~ im.save('osd_'+filename,quality=95,exif=exif)

for filename in os.listdir('.'):
    if os.path.isfile(filename):
        if filename.endswith('.jpg'):
            try:
                OSD(filename)
            except Exception as e:
                print("E:",e)
                pass
