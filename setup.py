import os
import sys

from setuptools import find_packages, setup


version = '0.3.0'


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    print('You probably want to also tag the version now:')
    print('  git tag -a %s -m "version %s"' % (version, version))
    print('  git push --tags')
    sys.exit()


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with open(filename) as fp:
        return fp.read()


tests_require = [
    'coverage',
    'pytest',
    'pytest-cov',
    'pytest-pep8',
    'pytest-flakes',
    'pytest-isort',
    'pytest-django',
    'factory-boy',
]


docs_requires = [
    'sphinx',
    'sphinx_rtd_theme'
]


setup(
    name='django-didadata',
    description='A Django app to collecto numeric data.',
    long_description=read('README.rst'),
    version=version,
    license='BSD',
    author='Stephan Jaekel, Benjamin Banduhn',
    author_email='steph@rdev.info',
    url='http://github.com/stephrdev/django-didadata/',
    packages=find_packages(exclude=[
        'didadata.tests',
        'didadata.tests.factories',
        'htmlcov',
        'build',
    ]),
    test_suite='.',
    tests_require=tests_require,
    install_requires=[
        'Django>=1.8.19,<2.0',
        'djangorestframework>=3.9.0,<3.10',
        'django-filter>=2.0.0,<2.1',
    ],
    extras_require={
        'docs': docs_requires,
        'tests': tests_require,
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Framework :: Django',
    ],
)
