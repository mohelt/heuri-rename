from setuptools import setup

setup(
    name='heuri-rename',
    version='1.0.0',
    description='heuri-rename is a ChRIS ds plugin, which copies files from an input directory to an output directory under different names, similar to pl-bulk-rename, but in a more user-friendly manner using heuristics',
    author='FNNDSC',
    author_email='dev@babyMRI.org',
    url='https://github.com/mohelt/heuri-rename',
    py_modules=['heuri-rename'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'heuri-rename = heuri-rename:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1',
            'pytest-mock~=3.8'
        ]
    }
)
