import os
import sys
from setuptools import setup, find_packages

version = '0.1.8'

def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(name='ios2andres',
      version=version,
      description=('iOS to Android Resource Renamer'),
      long_description='\n\n'.join((read('README.md'), read('CHANGELOG'))),
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Intended Audience :: Developers',
          'Programming Language :: Python'],
      keywords='android resources ios convert',
      author='Jordan Jozwiak',
      author_email='support@jozapps.com',
      url='https://github.com/jordanjoz1/ios2androidres',
      license='MIT',
      py_modules=['ios2andres'],
      namespace_packages=[],
      install_requires = [],
      entry_points={
          'console_scripts': [
              'ios2andres = ios2andres:main']
      },
      include_package_data = False)