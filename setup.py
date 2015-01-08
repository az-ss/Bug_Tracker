from setuptools import setup, find_packages
from os.path import join, dirname

NAME = 'BugTracker'
VERSION = '1.0'
AUTHOR = 'Aleksandr'
DESCRIPTION = 'Bug Tracker system'
AUTHOR_EMAIL = 'zelinskiialeksandr@gmail.com'

setup(
    name=NAME,
    version=VERSION,
    description= DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),

    entry_points={
        'console_scripts':
            ['hd = start_application.py']
    }, requires=['pymongo', 'tornado', 'tornadotools']
)