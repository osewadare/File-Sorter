# script for py2exe
# run using following command: "python setup.py py2exe"

from distutils.core import setup
from glob import glob
import py2exe

data_files=[('images', glob('images\\*.*'))]

setup(
        windows=[{'script':'File Sorter v1.0.py'}],
        data_files=data_files,
        options={'py2exe':{
                    'optimize': 1,
                    'bundle_files': 3,'compressed':True}},zipfile = None
)
