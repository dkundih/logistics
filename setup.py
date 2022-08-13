from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Intended Audience :: Science/Research',
  'Intended Audience :: Customer Service',
  'Intended Audience :: Financial and Insurance Industry',
  'Operating System :: Microsoft :: Windows :: Windows 7',
  'Operating System :: Microsoft :: Windows :: Windows 8',
  'Operating System :: Microsoft :: Windows :: Windows 8.1',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: Apache Software License',
  'Programming Language :: Python',
   'Programming Language :: Python :: 3 :: Only',
   'Programming Language :: Python :: 3.5',
   'Programming Language :: Python :: 3.6',
   'Programming Language :: Python :: 3.7',
   'Programming Language :: Python :: 3.8',
   'Programming Language :: Python :: 3.9',
   'Programming Language :: Python :: 3.10',
    'Topic :: Database',
    'Topic :: Education',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Office/Business :: Financial :: Investment',
    'Topic :: Office/Business :: Financial :: Accounting',
    'Topic :: Office/Business :: Financial :: Point-Of-Sale',
    'Topic :: Office/Business :: Financial :: Spreadsheet'
]
 
#import current duality version. 
from logistics.misc._meta import __version__

setup(
  name = 'logistics',
  version = __version__,
  description = 'Vandal framework logistics library.',
  long_description_content_type = 'text/markdown',
  long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(), 
  author = 'David Kundih',
  author_email = 'kundihdavid@gmail.com',
  maintainer = 'David Kundih',
  maintainer_email = 'kundihdavid@gmail.com',
  url = 'http://github.com/dkundih/unin',
  download_url = f'https://github.com/dkundih/unin/archive/refs/tags/v{__version__}.tar.gz',
  license = 'Apache Software License', 
  project_urls = {
    'Documentation': 'https://github.com/dkundih/unin/blob/master/README.md',
    'Source Code': 'https://github.com/dkundih/unin/tree/master/unin'
  },
  classifiers = classifiers,
  keywords = 'data science, machine learning, data manipulation, artificial intelligence, logistics, AI, unin, vandal, vandal-py, vandal.py, duality, duality-py, duality.py',
  packages = find_packages(),
  install_requires = [
    'colorama',
]
  )