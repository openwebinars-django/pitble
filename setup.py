# -*- coding: utf-8 -*-
# Copyright (c) 2014 by Pablo Martín <goinnn@gmail.com>


import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="pitble",
    version="0.0.2",
    author="Pablo Martin, Raul Sanchez, Alberto Vara",
    author_email="goinnn@gmail.com",
    description="Django microblog",
    long_description=(read('README.rst') + '\n\n' + read('CHANGES.rst')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    license="LGPL 3",
    keywords="django,microblog,pitble",
    url='https://github.com/openwebinars-django/pitble/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=('django-bootstrap3==4.3.0',),
)