from setuptools import setup, Extension

setup(
    ext_modules=[Extension("foo", ["foo.c"])],
)
