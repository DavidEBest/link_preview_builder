import os
from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r","")
except:
    print('Long desc failure')
    long_description = open('README.md').read()

setup(
    name = 'link_preview_builder', # name of package
    packages = ['link_preview_builder'],
    version = '1.0',
    description = 'Python package to get elements necessary for generating a rich link preview. Uses requests to retrieve data.',
    long_description=long_description,
    license='MIT',
    author = 'Dave Best',
    author_email = 'dave.e.best@gmail.com',
    url = 'https://github.com/DavidEBest/link_preview_builder', # url of git repo
    download_url = 'https://github.com/DavidEBest/link_preview_builder/archive/v0.1.tar.gz', # git tagged tar.gz
    keywords = ['preview', 'link'],
    platforms='all',
    classifiers = []
)
