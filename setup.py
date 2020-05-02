'''
Created on 2 may. 2020

@author: escri
'''
# setup.py
from distutils.core import setup
import py2exe
 
#-------------------------------------------- setup(console=['ip_blacklist.py'])
 
setup(
    console = ['ip_blacklist.py'],
    options = {
        'py2exe': {
            'packages' : ['bs4', 'selenium', 'email']
            }
        }
)

