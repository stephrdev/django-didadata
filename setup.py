import os
from codecs import open

from setuptools import find_packages, setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('didadata').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


prod_require = [
    'Django>=2.2,<3.2',
    'djangorestframework>=3.12.1,<3.13',
    'django-filter>=2.4.0,<2.5',
]

dev_require = [
    'pytest',
    'pytest-black',
    'pytest-isort',
    'pytest-django',
    'pytest-cov',
    'pytest-flake8',
    'sphinx',
    'sphinx-rtd-theme',
    'factory-boy',
]


setup(
    name='django-didadata',
    version=VERSION,
    description='A Django app to collect numeric data.',
    long_description=long_description,
    url='https://github.com/stephrdev/django-didadata/',
    project_urls={
        'Bug Reports': 'https://github.com/stephrdev/django-didadata/issues',
        'Source': 'https://github.com/stephrdev/django-didadata',
    },
    author='Stephan Jaekel, Benjamin Banduhn',
    author_email='steph@rdev.info',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[prod_require],
    extras_require={'dev': dev_require},
    include_package_data=True,
    keywords='django didadata',
    license='BSD',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
