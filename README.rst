What is vcs2l?
================

Vcs2l is a fork of Dirk Thomas's `vcstool <https://github.com/dirk-thomas/vcstool/>`_ which is a version control system (VCS) tool, designed to make working with multiple repositories easier.
This fork is created to continue the development of vcstool, as it is no longer actively maintained.

The commands provided by vcs2l have the same naming structure as the original fork, so it can be used as a drop-in replacement.
Therefore, the repository is renamed to `vcs2l` while maintaining the command names to `vcstool` to ensure compatibility with existing scripts and workflows.

Note:
  This tool should not be confused with `vcstools <https://github.com/vcstools/vcstools/>`_ (with a trailing ``s``) which provides a Python API for interacting with different version control systems.
  The biggest differences between the two are:

  * ``vcstool`` doesn't use any state beside the repository working copies available in the filesystem.
  * The file format of ``vcstool export`` uses the relative paths of the repositories as keys in YAML which avoids collisions by design.
  * ``vcstool`` has significantly fewer lines of code than ``vcstools`` including the command line tools built on top.

Python 3.5+ support
---------------------------

The latest version supports Python 3.5 and newer.
However, the CI is only run on Python 3.7 and newer, as there are no suitable GitHub Actions `runners <https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json/>`_ available for Python 3.5 and 3.6.


How does it work?
-----------------

Vcs2l operates on any folder from where it recursively searches for supported repositories.
On these repositories vcs2l invokes the native VCS client with the requested command (i.e. *diff*).


Which VCS types are supported?
------------------------------

Vcs2l supports `Git <http://git-scm.com>`_, `Mercurial <https://www.mercurial-scm.org/>`_, `Subversion <http://subversion.apache.org>`_, `Bazaar <http://bazaar.canonical.com/en/>`_.


How to use vcs2l?
-------------------

The script ``vcs`` can be used similarly to the VCS clients ``git``, ``hg`` etc.
The ``help`` command provides a list of available commands with an additional description::

  vcs help

By default vcs2l searches for repositories under the current folder.
Optionally one path (or multiple paths) can be passed to search for repositories at different locations::

  vcs status /path/to/several/repos /path/to/other/repos /path/to/single/repo


Exporting and importing sets of repositories
--------------------------------------------

Vcs2l can export and import all the information required to reproduce the versions of a set of repositories.
Vcs2l uses a simple `YAML <http://www.yaml.org/>`_ format to encode this information.
This format includes a root key ``repositories`` under which each local repository is described by a dictionary keyed by its relative path.
Each of these dictionaries contains keys ``type``, ``url``, and ``version``.
If the ``version`` key is omitted the default branch is being used.

This results in something similar to the following for a set of two repositories (`vcs2l <https://github.com/ros-infrastructure/vcs2l>`_ cloned via Git and `rosinstall <http://github.com/vcstools/rosinstall>`_ checked out via Subversion):

.. code-block:: yaml

  repositories:
    vcs2l:
      type: git
      url: git@github.com:ros-infrastructure/vcs2l.git
      version: main
    old_tools/rosinstall:
      type: svn
      url: https://github.com/vcstools/rosinstall/trunk
      version: 748


Export set of repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``vcs export`` command outputs the path, vcs type, URL and version information for all repositories in `YAML <http://www.yaml.org/>`_ format.
The output is usually piped to a file::

  vcs export > my.repos

If the repository is currently on the tip of a branch the branch is followed.
This implies that a later import might fetch a newer revision if the branch has evolved in the meantime.
Furthermore if the local branch has evolved from the remote repository an import might not result in the exact same state.

To make sure to store the exact revision in the exported data use the command line argument ``--exact``.
Since a specific revision is not tied to neither a branch nor a remote (for Git and Mercurial) the tool will check if the current hash exists in any of the remotes.
If it exists in multiple the remotes ``origin`` and ``upstream`` are considered before any other in alphabetical order.


Import set of repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``vcs import`` command clones all repositories which are passed in via ``stdin`` in YAML format.
Usually the data of a previously exported file is piped in::

  vcs import < my.repos

The ``import`` command also supports input in the `rosinstall file format <http://www.ros.org/doc/independent/api/rosinstall/html/rosinstall_file_format.html>`_.
Beside passing a file path the command also supports passing a URL.

Only for this command vcs2l supports the pseudo clients ``tar`` and ``zip`` which fetch a tarball / zipfile from a URL and unpack its content.
For those two types the ``version`` key is optional.
If specified only entries from the archive which are in the subfolder specified by the version value are being extracted.

Import with extends functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``vcs import`` command supports an ``extends`` key at the top level of the YAML file. The value of that key is a path or URL to another YAML file which is imported first.
This parent file can itself also contain the key to chain multiple files. The child is given precedence over the parent in case of duplicate repository entries.
In order to avoid infinite loops in case of circular imports the tool detects already imported files and raises an error if such a file is encountered again.

.. code-block:: yaml

  # parent_repos.yaml
  repositories:
    vcs2l:
      type: git
      url: https://github.com/ros-infrastructure/vcs2l.git
      version: main

  # child_repos.yaml
  extends: parent_repos.yaml
  repositories:
    vcs2l:
      type: git
      url: https://github.com/ros-infrastructure/vcs2l.git
      version: 1.1.3


Validate repositories file
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``vcs validate`` command takes a YAML file which is passed in via ``stdin`` and validates its contents and format.
The data of a previously-exported file or hand-generated file are piped in::

  vcs validate < my.repos

The ``validate`` command also supports input in the `rosinstall file format <http://www.ros.org/doc/independent/api/rosinstall/html/rosinstall_file_format.html>`_.


Advanced features
-----------------

Show log since last tag
~~~~~~~~~~~~~~~~~~~~~~~

The ``vcs log`` command supports the argument ``--limit-untagged`` which will output the log for all commits since the last tag.


Parallelization and stdin
~~~~~~~~~~~~~~~~~~~~~~~~~

By default ``vcs`` parallelizes the work across multiple repositories based on the number of CPU cores.
In the case that the invoked commands require input from ``stdin`` that parallelization is a problem.
In order to be able to provide input to each command separately these commands must run sequentially.
When needing to e.g. interactively provide credentials all commands should be executed sequentially by passing:

  --workers 1

In the case repositories are using SSH ``git@`` URLs but the host is not known yet ``vcs import`` automatically falls back to a single worker.


Run arbitrary commands
~~~~~~~~~~~~~~~~~~~~~~

The ``vcs custom`` command enables to pass arbitrary user-specified arguments to the vcs invocation.
The set of repositories to operate on can optionally be restricted by the type:

  vcs custom --git --args log --oneline -n 10

If the command should work on multiple repositories make sure to pass only generic arguments which work for all of these repository types.


How to install vcs2l?
=======================

On Debian-based platforms the recommended method is to install the package *python3-vcs2l*.
On Ubuntu this is done using *apt-get*:

If you are using `ROS <https://www.ros.org/>`_ you can get the package directly from the ROS repository::

  sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
  sudo apt install curl # if you haven't already installed curl
  curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
  sudo apt-get update
  sudo apt-get install python3-vcs2l

On other systems, use the `PyPI <https://pypi.org/project/vcs2l/>`_ package::

  pip3 install vcs2l


Setup auto-completion
---------------------

For the shells *bash*, *tcsh* and *zsh* vcs2l can provide auto-completion of the various VCS commands.
In order to enable that feature the shell specific completion file must be sourced.

For *bash* append the following line to the ``~/.bashrc`` file::

  source /usr/share/vcs2l-completion/vcs.bash

For *tcsh* append the following line to the ``~/.cshrc`` file::

  source /usr/share/vcs2l-completion/vcs.tcsh

For *zsh* append the following line to the ``~/.zshrc`` file::

  source /usr/share/vcs2l-completion/vcs.zsh

For *fish* append the following line to the ``~/.config/fishconfig.fish`` file::

  source /usr/share/vcs2l-completion/vcs.fish

How to contribute?
==================

How to report problems?
-----------------------

Before reporting a problem please make sure to use the latest version.
Issues can be filled on `GitHub <https://github.com/ros-infrastructure/vcs2l/issues>`_ after making sure that this problem has not yet been reported.

Please make sure to include as much information, i.e. version numbers from vcs2l, operating system, Python and a reproducible example of the commands which expose the problem.


How to try the latest changes?
------------------------------

Sourcing the ``setup.sh`` file prepends the ``src`` folder to the ``PYTHONPATH`` and the ``scripts`` folder to the ``PATH``.
Then vcs2l can be used with the commands ``vcs-COMMAND`` (note the hyphen between ``vcs`` and ``command`` instead of a space).

Alternatively the ``-e/--editable`` flag of ``pip`` can be used::

  # from the top level of this repo
  pip3 install --user -e .
