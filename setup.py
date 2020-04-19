#!/usr/bin/env python
import os
import sys

from setuptools import find_packages, setup


def get_version():
    from subdomains import __version__
    return '.'.join(map(str, __version__))

try:
    version = get_version()
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__, 'subdomains')))
    version = get_version()


# Hack: The Django version pin needs to match the Django version in the project
# that is using this library, or else you get build error when installing as an
# external Github depencency via pipenv:
# pipenv install -e git+https://github.com/GetResQ/django-subdomains.git@3.0#egg=django-subdomains
# Seems to be a bug in pipenv, but I haven't looked too deeply into it. Just
# getting the build working for now.
install_requires = ['django==2.2.12']

tests_require = install_requires + ['mock']

setup(name='django-subdomains',
    version=version,
    url='http://github.com/tkaemming/django-subdomains/',
    author='ted kaemming',
    author_email='ted@kaemming.com',
    description="Subdomain tools for the Django framework, including "
        "subdomain-based URL routing.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='subdomains.tests.run',
    zip_safe=False,
    license='MIT License',
)
