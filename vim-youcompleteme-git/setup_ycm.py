#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="ycm",
      version=None,
      description="A code-completion engine for Vim",
      url="https://github.com/ycm-core/YouCompleteMe",
      license="GPL3",
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)
