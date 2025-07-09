"""Setup script for the vcs2l package."""

import os

from setuptools import find_packages
from setuptools import setup
from vcstool import __version__

with open(
    os.path.join(os.path.dirname(__file__), 'README.rst'),
        'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vcs2l',
    version=__version__,
    requires_python='>=3.7',
    install_requires=[
        'PyYAML',
        'setuptools'],
    extras_require={
        'test': [
            'flake8',
            'flake8-docstrings',
            'flake8-import-order',
            'pycodestyle',
            'pyflakes',
            'pytest']
        },
    packages=find_packages(),
    author='Dirk Thomas',
    author_email='web@dirk-thomas.net',
    maintainer='ROS Infrastructure Team',
    project_urls={
        'Source code':
        'https://github.com/ros-infrastructure/vcs2l',
        'Issue tracker':
        'https://github.com/ros-infrastructure/vcs2l/issues',
    },
    url='https://github.com/ros-infrastructure/vcs2l',
    keywords=['vcs', 'version control', 'git', 'hg', 'svn', 'bzr'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Version Control',
                 'Topic :: Utilities'],
    description='vcs2l provides a command line tool to invoke vcs commands '
        'on multiple repositories.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license='Apache License, Version 2.0',
    data_files=[
        ('share/vcs2l-completion', [
            'vcs2l-completion/vcs.bash',
            'vcs2l-completion/vcs.tcsh',
            'vcs2l-completion/vcs.zsh',
            'vcs2l-completion/vcs.fish'
        ])
    ],
    entry_points={
        'console_scripts': [
            'vcs = vcstool.commands.vcs:main',
            'vcs-branch = vcstool.commands.branch:main',
            'vcs-bzr = vcstool.commands.custom:bzr_main',
            'vcs-custom = vcstool.commands.custom:main',
            'vcs-diff = vcstool.commands.diff:main',
            'vcs-export = vcstool.commands.export:main',
            'vcs-git = vcstool.commands.custom:git_main',
            'vcs-help = vcstool.commands.help:main',
            'vcs-hg = vcstool.commands.custom:hg_main',
            'vcs-import = vcstool.commands.import_:main',
            'vcs-log = vcstool.commands.log:main',
            'vcs-pull = vcstool.commands.pull:main',
            'vcs-push = vcstool.commands.push:main',
            'vcs-remotes = vcstool.commands.remotes:main',
            'vcs-status = vcstool.commands.status:main',
            'vcs-svn = vcstool.commands.custom:svn_main',
            'vcs-validate = vcstool.commands.validate:main',
        ]
    }
)
