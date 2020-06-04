from distutils.core import setup
from os import path # read the contents of your README file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'jupyslides',         
  packages = ['jupyslides'],
  version = '0.1',
  license = 'MIT',
  description = 'A jupyter notebook widget that allows you to create an embedded ppt slides',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Naili Ding',
  author_email = 'nding17@outlook.com',
  url = 'https://github.com/nding17/jupyslides',
  download_url = 'https://github.com/nding17/jupyslides/archive/v_011.tar.gz',
  keywords = [
    'jupyter notebook', 
    'embedded ppt', 
    'embedded slides'
  ],
  install_requires = [
    'ipywidgets',
    'natsort',
    'IPython',
  ],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)