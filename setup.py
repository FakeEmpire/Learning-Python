try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'AmberG',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'tiedtothe90s@hotmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [('write package name here)(ie. hello.py)'],
    'scripts': [(write location of script here)(ie. bin/hello.py)],
    'name': 'projectname'
}

setup(**config)
