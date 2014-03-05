from setuptools import setup, find_packages
import os

version = '2.0'
maintainer = 'Gerhard Weis'

setup(name='collective.js.uix.multiselect',
      version=version,
      description='Integrates the jquery.uix.multiselect widget into plone.',
      long_description=open('README.rst').read() + '\n' + \
          open(os.path.join('docs', 'HISTORY.txt')).read(),

      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],

      keywords='jquery uix multiselect plone',
      author='Gerhard Weis',
      author_email='mailto:eresearch-services@griffith.edu.au',
      maintainer=maintainer,
      url='http://eresearch.griffith.edu.au',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js', 'collective.js.uix'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        ],

      entry_points='''
# -*- Entry points: -*-
[z3c.autoinclude.plugin]
target = plone
''',
      )
