from setuptools import setup


with open('README.md') as f:
    long_description = f.read()


setup(
    name='pakm',
    version='0.1.0',
    author='Dylan Stephano-Shachter',
    author_email='dylan@theone.ninja',
    description='Universal Package Manager',
    long_description=long_description,
    url='https://github.com/dstathis/pakm',
    packages=['pakm'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX',
        'Topic :: System'
    ],
    entry_points = {'console_scripts': ['pakg = pakg.main:main']}
)
