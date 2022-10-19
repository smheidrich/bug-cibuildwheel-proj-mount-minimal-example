from setuptools import setup, Extension

setup(
    ext_modules=[Extension("ext", ["ext.c"])],
)
