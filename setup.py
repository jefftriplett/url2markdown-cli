#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.4.1"

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        raise ImportError("Fix: pip install wheel")
    os.system('python setup.py sdist bdist_wheel upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

install_requires = [
    'click',
    'requests',
    'requests-cache',
]

extras_require = {
    'requests-cache': ['requests-cache'],
}

setup(
    name='url2markdown-cli',
    version=version,
    description="""Fetch a url and translate it to markdown in one command.""",
    long_description=readme + '\n\n' + history,
    author='Jeff Triplett',
    author_email='jeff.triplett@gmail.com',
    url='https://github.com/jefftriplett/url2markdown-cli',
    include_package_data=True,
    py_modules=[
        'url2markdown_cli',
    ],
    install_requires=install_requires,
    extras_require=extras_require,
    license="BSD",
    zip_safe=False,
    keywords='url2markdown, url2markdown-cli',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={'console_scripts': [
        'url2markdown = url2markdown_cli:main',
    ]},
)
