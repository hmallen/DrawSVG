from setuptools import setup, find_packages

try:
    with open('DESCRIPTION.rst', 'r') as f:
        longDesc = f.read()
except:
    print('Warning: Could not open DESCRIPTION.rst.  long_description will be set to None.')
    longDesc = None

setup(
    name = "drawSVG",
    packages = find_packages(),
    version = "1.0.0",
    description = ("A fork of Peter Collingridge's DrawSVG that works with Python 3."),
    author = "Hunter Allen",
    author_email = "allenhm@gmail.com",
)
