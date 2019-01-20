import os
from codecs import open

from setuptools import find_packages, setup


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('didadata').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-didadata',
    version=VERSION,
    description='A Django app to collecto numeric data.',
    long_description=long_description,
    url='https://github.com/stephrdev/django-didadata/',
    project_urls={
        'Bug Reports': 'https://github.com/stephrdev/django-didadata/issues',
        'Source': 'https://github.com/stephrdev/django-didadata',
    },
    author='Stephan Jaekel, Benjamin Banduhn',
    author_email='steph@rdev.info',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['Django>=1.8.19,<2.2'],
    include_package_data=True,
    keywords='django didadata',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
