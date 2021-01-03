#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="ycmd",
      version=None,
      description="A code-completion & code-comprehension server",
      url="https://github.com/ycm-core/ycmd",
      license="GPL3",
      packages=find_packages(exclude=["examples", "*.tests", "*.tests.*", "tests.*", "tests"]),
      package_data={"ycmd": ['../ycm_core*.so', 'default_settings.json', 'CORE_VERSION']},
)
