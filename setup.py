from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='upc.genweb.meetings',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='UPCnet',
      author_email='plone.team@upcnet.es',
      url='https://devel.upcnet.es/moduls/simple',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['upc', 'upc.genweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Products.AJAXAddRemoveWidget',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
