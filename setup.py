"""
file3
    Copyright (C) 2021 Israel Cunha (israelcunhamail@gmail.com)

    This program is free software; you can redistribute it and/or modify
    it under the terms of the Python Packaging Authority License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Python Packaging Authority License for more details.
"""
import setuptools

_PACKAGE_VERSION = '0.1.7'
_PACKAGE_NAME = 'file3'
_KEYWORDS = "file files file3"
_SET_DESCRIPTION = "Converting Files and Types"

def get_long_description():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description

setuptools.setup(
    name=_PACKAGE_NAME,
    version=_PACKAGE_VERSION,
    author="Israel Cunha",
    author_email="israelcunhamail@gmail.com",
    keywords=_KEYWORDS,
    description=_SET_DESCRIPTION,
    license="MIT License",
    platforms=["Linux", "Windows", "MacOS"],
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/israeljcunha/file3",
    packages=setuptools.find_packages(exclude=["venv", "file-test-env"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)
