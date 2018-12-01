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

from PIL import Image

image1_path = 'a.jpg'
image2_path = 'b.jpg'
im = Image.open(image1_path)
exif = im.info['exif']
print(exif)
im = Image.open(image2_path)
im.save(image2_path, exif=exif)
