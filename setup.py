from distutils.core import setup

setup(
  name = 'jupyslides',         
  packages = ['jupyslides'],
  version = '0.1',
  license='MIT',
  description = 'A jupyter notebook widget that allows you to create an embedded ppt slides',
  author = 'Naili Ding',
  author_email = 'nding17@outlook.com',
  url = 'https://github.com/nding17/jupyslides',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['jupyter notebook', 'embedded ppt', 'embedded slides'],   # Keywords that define your package best
  install_requires=[
    'ipywidgets',
    'os',
    'natsort',
    'IPython',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)