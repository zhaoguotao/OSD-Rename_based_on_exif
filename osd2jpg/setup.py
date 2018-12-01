from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

py2exe_options = {
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 2,#not 1
        }

setup(
      name = 'OSD2jpg',
      version = '1.0',
      windows = ['OSD2jpg.py',],
      zipfile = None,
      options = {'py2exe': py2exe_options}
      )
