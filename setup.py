from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

APP_VERSION = "1.0"
APP_AUTHOR = "Jed Glazner"
APP_AUTHOR_EMAIL= "jglazner@coldcrow.com"
APP_NAME = "daemon"

setup(
    name=APP_NAME,
    version=APP_VERSION,
    description="Simple class for creating linux based daemons",
    long_description="",
    url="https://github.com/jglazner/daemon",
    author=APP_AUTHOR,
    author_email=APP_AUTHOR_EMAIL,
    license="Apache 2.0",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Daemon Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: Apache 2.0 License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],

    keywords='daemons',

    packages=['daemon'],

    package_data={'daemon': ['*']},

    install_requires=[],

    entry_points={},
)
